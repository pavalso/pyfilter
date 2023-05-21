import unittest
import os

from pyfilter import filters


class TestContains(unittest.TestCase):

    def test_filter(self):

        root = 'D://test/dir'

        self.assertEqual(filters.Paths.relative('D://test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/dir2', root), os.path.abspath(f'{root}/dir2'))
        self.assertEqual(filters.Paths.relative('D://test/dir/dir2/', root), os.path.abspath(f'{root}/dir2'))

        self.assertEqual(filters.Paths.relative('D://test/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir2', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir2/', root), os.path.abspath(root)) 

    def test_traversal(self):

        root = 'D://test/dir/'

        self.assertEqual(filters.Paths.relative('D://test/dir/./', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/././', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/../', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/.././', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/.././../', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/../../', root), os.path.abspath(root))

        self.assertEqual(filters.Paths.relative('D://test/dir/./dir2', root), os.path.abspath(f'{root}/dir2'))
        self.assertEqual(filters.Paths.relative('D://test/dir/./dir2/', root), os.path.abspath(f'{root}/dir2'))
        self.assertEqual(filters.Paths.relative('D://test/dir/../dir2', root), os.path.abspath(f'{root}'))
        self.assertEqual(filters.Paths.relative('D://test/dir/../dir2/', root), os.path.abspath(f'{root}'))

        self.assertEqual(filters.Paths.relative('D://test/dir/./dir2/./', root), os.path.abspath(f'{root}/dir2'))
        self.assertEqual(filters.Paths.relative('D://test/dir/./dir2/../', root), os.path.abspath(f'{root}'))

        self.assertEqual(filters.Paths.relative('D://test/dir/./dir2/./dir3', root), os.path.abspath(f'{root}/dir2/dir3'))
        self.assertEqual(filters.Paths.relative('D://test/dir/./dir2/../dir3', root), os.path.abspath(f'{root}/dir3'))

        root = 'D://test/dir/../'

        self.assertEqual(filters.Paths.relative('D://test/dir/./', root), os.path.abspath(f'{root}/dir'))
        self.assertEqual(filters.Paths.relative('D://test/dir/../', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/../../', root), os.path.abspath(root))

        self.assertEqual(filters.Paths.relative('D://test/dir/./dir2', root), os.path.abspath(f'{root}/dir/dir2'))
        self.assertEqual(filters.Paths.relative('D://test/dir/./dir2/', root), os.path.abspath(f'{root}/dir/dir2'))

    def test_os_paths(self):

        root = 'D://test/dir'

        self.assertEqual(filters.Paths.relative('C://test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('C://test/dir', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('C://test/dir/dir2', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('C://test/dir/dir2/', root), os.path.abspath(root))

        self.assertEqual(filters.Paths.relative('test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('test/dir', root), os.path.abspath(root))

        root = 'C://test/dir'

        self.assertEqual(filters.Paths.relative('D://test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/dir2', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/dir2/', root), os.path.abspath(root))

        self.assertEqual(filters.Paths.relative('/test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('/test/dir', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('/test/dir/dir2', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('/test/dir/dir2/', root), os.path.abspath(root))

        self.assertEqual(filters.Paths.relative('test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('test/dir', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('test/dir/dir2', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('test/dir/dir2/', root), os.path.abspath(root))

    def test_drives(self):

        root = '//test/dir'

        self.assertEqual(filters.Paths.relative('D://test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/dir2', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('D://test/dir/dir2/', root), os.path.abspath(root))

        self.assertEqual(filters.Paths.relative('C://test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('C://test/dir', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('C://test/dir/dir2', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('C://test/dir/dir2/', root), os.path.abspath(root))

        self.assertEqual(filters.Paths.relative('//test/dir/', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('//test/dir', root), os.path.abspath(root))
        self.assertEqual(filters.Paths.relative('//test/dir/dir2', root), os.path.abspath(f'{root}/dir2'))
        self.assertEqual(filters.Paths.relative('//test/dir/dir2/', root), os.path.abspath(f'{root}/dir2'))
