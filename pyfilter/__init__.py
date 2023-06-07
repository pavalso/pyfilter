try:
    import filters
    import baseServer
    import httpServer
except ImportError:
    from . import filters
    from . import baseServer
    from . import httpServer

__all__ = ['filters', 'baseServer', 'httpServer']

__program__ = 'pyfilter'
__version__ = '2.0'
__author__ = 'Pavalso'
