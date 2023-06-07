from pyfilter.utils import BaseConfig


class Config(BaseConfig):
    list_directories : bool
    render_index : bool

        self.config = Config(**{
            'list_directories': True,
            'render_index': False
        })

        if self.config.render_index and (ret := self.render_index(dir)):
            self.abort(ret)

        if not self.config.list_directories:
            self.abort(404)

        if not self.config.list_directories and os.path.isdir(file):
            self.abort(404)
