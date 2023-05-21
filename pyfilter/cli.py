import pyfilter
import flask
import os


app = flask.Flask(__name__)

app.url_map.converters['path'].to_python = lambda _, value: pyfilter.Paths.relative(value)
app.url_map.strict_slashes = False

@app.get('/<path:path>')
def get_file(path):
    print('FILE', path)
    if not os.path.isfile(path):
        flask.abort(404)

    try:
        return flask.send_file(path)
    except PermissionError:
        flask.abort(403)

@app.get('/', defaults = {'path': '.'})
@app.get('/<path:path>/')
def get_dir(path):
    print('DIR', path)
    if not os.path.isdir(path):
        flask.abort(404)

    index_path = os.path.join(os.path.abspath(path), 'index.html')

    if os.path.isfile(index_path):
        flask.abort(get_file(index_path))

    walk = next(os.walk(path, onerror=lambda _: flask.abort(403)))

    relative = os.path.relpath(path)
    relative = '' if relative == '.' else '%s%c' % (relative.replace(os.path.sep, os.path.altsep), os.path.altsep)

    return flask.render_template(
        'index.html',
        path = relative,
        dirs = walk[1],
        files = walk[2])

def main(**kwargs):
    host = kwargs.get('host', 'localhost')
    port = kwargs.get('port', 80)

    app.run(
        host = host, 
        port = port)
