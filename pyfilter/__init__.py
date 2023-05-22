try:
    from filters import Paths
except ImportError:
    from .filters import Paths

__all__ = ['Paths']

__program__ = 'pyfilter'
__version__ = '1.0'
__author__ = 'Pavalso'

if __name__ == '__main__':
    import cli
    cli.main()
