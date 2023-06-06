import os
import pyfilter

from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import abort, HTTPException
from werkzeug.utils import send_from_directory, redirect
from werkzeug.local import Local, LocalManager
from jinja2 import Environment, FileSystemLoader, exceptions as jinja2_exceptions


class PyfilterHttpServer(object):

    @property
    def request(self):
        return self.local.request

    def __init__(self, **kwargs):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')

        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
        self.root = os.path.abspath(kwargs.get('path', os.getcwd()))

        self.local = Local()
        self.local_manager = LocalManager([self.local])

        self.url_map = Map([
            Rule('/', methods=['GET'], defaults={'path': '%c%c' % (pyfilter.Paths.curdir, pyfilter.Paths.altsep)}),
            Rule('/<path:path>', methods=['GET'])
        ])

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            _, values = adapter.match()
            return self.on_request(values['path'])
        except HTTPException as e:
            return e
        except Exception as e:
            self.abort(500)

    def on_request(self, path: str):
        _, request_path = os.path.splitdrive(pyfilter.Paths.traversal_filter(path))
        filtered_path = os.path.join(self.root, pyfilter.Paths.contains(request_path, self.root) or self.abort(404))
        return self.get_dir(filtered_path) if path.endswith(pyfilter.Paths.altsep) else self.get_file(filtered_path)

    def get_dir(self, path):
        if not os.path.isdir(path):
            self.abort(404)

        if (render := False) and (res := self.render_index(path)):
            self.abort(res)

        if block_by_default := False:
            self.abort(404)

        walk = next(os.walk(path, onerror=lambda _: self.abort(403)))

        relative = os.path.relpath(path, self.root)
        relative = '' if relative == '.' else '%s%c' % (relative.replace(pyfilter.Paths.sep, pyfilter.Paths.altsep), pyfilter.Paths.altsep)

        try:
            return self.render_template(
                'index.html',
                path = relative,
                dirs = walk[1],
                files = walk[2])
        except jinja2_exceptions.TemplateNotFound:
            self.abort(404)

    def get_file(self, path):
        if not os.path.isfile(path):
            return os.path.isdir(path) and \
                self.redirect(self.request.path + pyfilter.Paths.altsep) or \
                self.abort(404)

        try:
            return self.send_from_directory(self.root, path)
        except PermissionError:
            self.abort(403)

    def render_index(self, dir):
        index_path = os.path.join(os.path.abspath(dir), 'index.html')

        try:
            return self.get_file(index_path)
        except HTTPException:
            pass
        return None

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name, parent=__file__)
        return Response(t.render(context), mimetype='text/html')

    def abort(self, code):
        abort(code)

    def redirect(self, location):
        return redirect(location)

    def send_from_directory(self, directory, path):
        aux_path = os.path.relpath(path, self.root).replace(pyfilter.Paths.sep, pyfilter.Paths.altsep)
        return send_from_directory(directory, aux_path, self.request.environ)

    def wsgi_app(self, environ, start_response):
        self.local.request = request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

def create_app(**config):
    config = config or {}
    app = PyfilterHttpServer(**config)
    return app.local_manager.make_middleware(app)

def main():
    from werkzeug.serving import run_simple
    import argparse

    parser = argparse.ArgumentParser(
        prog = pyfilter.__program__,
        description = 'A simple web server for viewing files and directories.',
        epilog = 'Made by %s.' % pyfilter.__author__)
    
    parser.add_argument(
        '-v', '--version',
        action = 'version',
        version = '%(prog)s v' + pyfilter.__version__)
    
    parser.add_argument(
        '-H', '--host',
        metavar = 'HOST',
        default = 'localhost',
        help = 'the host to listen on (default: %(default)s)')

    parser.add_argument(
        'port',
        metavar = 'PORT',
        type = int,
        nargs='?',
        default = 5000,
        help = 'the port to listen on (default: %(default)s)')
    
    parser.add_argument(
        '-P', '--path',
        metavar = 'PATH',
        default = '.',
        help = 'the path to serve (default: %(default)s)')

    args = parser.parse_args()

    host = args.host
    port = args.port

    app = create_app(**vars(args))

    run_simple(host, port, app, threaded=True)
