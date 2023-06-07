import os

from werkzeug.exceptions import HTTPException

from pyfilter.server import BaseServer
from pyfilter.utils import BaseConfig


class Config(BaseConfig):
    list_directories : bool
    render_index : bool

class HttpServer(BaseServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config = Config(**{
            'list_directories': True,
            'render_index': False
        })

    def get_dir(self, dir):
        if self.config.render_index and (ret := self.render_index(dir)):
            self.abort(ret)

        if not self.config.list_directories:
            self.abort(404)

        return super().get_dir(dir)
    
    def get_file(self, file):
        if not self.config.list_directories and os.path.isdir(file):
            self.abort(404)

        return super().get_file(file)

    def render_index(self, dir):
        index_path = os.path.join(os.path.abspath(dir), 'index.html')

        try:
            return self.get_file(index_path)
        except HTTPException:
            pass
        return None
