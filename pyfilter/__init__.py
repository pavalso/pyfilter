try:
    import filters
    import server
    import httpServer
except ImportError:
    from . import filters
    from . import server
    from . import httpServer

__all__ = ['filters', 'server', 'httpServer']

__program__ = 'pyfilter'
__version__ = '2.0'
__author__ = 'Pavalso'
