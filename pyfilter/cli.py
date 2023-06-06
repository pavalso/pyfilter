import pyfilter
import flask
import os
import argparse
import werkzeug.exceptions
import jinja2.exceptions


app = flask.Flask(__name__)
root = os.getcwd()

render = True
block_by_default = False

def get_dir(path):
    if not os.path.isdir(path):
        flask.abort(404)

    if render and (res := render_index(path)):
        flask.abort(res)

    if block_by_default:
        flask.abort(404)

    walk = next(os.walk(path, onerror=lambda _: flask.abort(403)))

    relative = os.path.relpath(path, root)
    relative = '' if relative == '.' else '%s%c' % (relative.replace(os.path.sep, os.path.altsep), os.path.altsep)

    try:
        return flask.render_template(
            'index.html',
            path = relative,
            dirs = walk[1],
            files = walk[2])
    except jinja2.exceptions.TemplateNotFound:
        flask.abort(404)

def get_file(path):
    if not os.path.isfile(path):
        flask.abort(404)

    try:
        return flask.send_file(path)
    except PermissionError:
        flask.abort(403)

def render_index(dir):
    index_path = os.path.join(os.path.abspath(dir), 'index.html')

    try:
        return get_file(index_path)
    except werkzeug.exceptions.HTTPException:
        pass
    return None

@app.get('/', defaults={'path': '%c%c' % (pyfilter.Paths.curdir, pyfilter.Paths.altsep)})
@app.route('/<path:path>', strict_slashes=False)
def on_request(path: str):
    print('on_request(%s)' % path)
    _, request_path = os.path.splitdrive(pyfilter.Paths.traversal_filter(path))
    filtered_path = os.path.join(root, pyfilter.Paths.contains(request_path, root) or flask.abort(404))
    return get_dir(filtered_path) if path.endswith(pyfilter.Paths.altsep) else get_file(filtered_path)

def main():
    global root
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
    root = args.path

    if isinstance(port, int):
        if port < 0 or port > 65535:
            parser.error('port must be between 0 and 65535')

    if not os.path.isdir(root):
        parser.error('path must be a directory')

    app.run(
        host = host, 
        port = port)
