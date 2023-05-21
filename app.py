import pyfilter
import flask
import os

from werkzeug.routing import PathConverter


class SanitizedPathConverter(PathConverter):

    def to_python(self, value):
        abs_path = os.path.abspath(value)

        if not pyfilter.Paths.contains(abs_path):
            flask.abort(flask.redirect('/'))

        return abs_path

app = flask.Flask(__name__)
app.url_map.converters['Path'] = SanitizedPathConverter

@app.get('/', defaults = {'path': '.'})
@app.get('/<Path:path>/')
def get_dir(path):
    if not os.path.isdir(path):
        flask.abort(404)

    walk = next(os.walk(path, onerror=lambda _: flask.abort(403)))
    return flask.render_template(
        'index.html',
        dirs = walk[1],
        files = walk[2])

@app.get('/<Path:path>')
def get_file(path):
    if not os.path.isfile(path):
        flask.abort(404)

    try:
        return flask.send_file(path, mimetype='text/plain')
    except PermissionError:
        flask.abort(403)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 80)
