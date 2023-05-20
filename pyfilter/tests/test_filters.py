import unittest
import filters
import os


class TestFilters(unittest.TestCase):

    def test_filter(self):

        root = 'D://test/dir'

        self.assertTrue(filters.Paths.contains('D://test/dir/', root))
        self.assertTrue(filters.Paths.contains('D://test/dir', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/dir2', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/dir2/', root))

        self.assertFalse(filters.Paths.contains('D://test/', root))
        self.assertFalse(filters.Paths.contains('D://test', root))
        self.assertFalse(filters.Paths.contains('D://test/dir2', root))
        self.assertFalse(filters.Paths.contains('D://test/dir2/', root))

        self.assertFalse(filters.Paths.contains('C://test/dir/', root))
        self.assertFalse(filters.Paths.contains('C://test/dir', root))
        self.assertFalse(filters.Paths.contains('C://test/dir/dir2', root))
        self.assertFalse(filters.Paths.contains('C://test/dir/dir2/', root))

        self.assertTrue(filters.Paths.contains('/test/dir/', root))
        self.assertTrue(filters.Paths.contains('/test/dir', root))
        self.assertTrue(filters.Paths.contains('/test/dir/dir2', root))
        self.assertTrue(filters.Paths.contains('/test/dir/dir2/', root))

        self.assertFalse(filters.Paths.contains('test/', root))
        self.assertFalse(filters.Paths.contains('test', root))
        self.assertFalse(filters.Paths.contains('test/dir2', root))
        self.assertFalse(filters.Paths.contains('test/dir2/', root))

        root = 'C://test/dir'

        self.assertTrue(filters.Paths.contains('C://test/dir/', root))
        self.assertTrue(filters.Paths.contains('C://test/dir', root))
        self.assertTrue(filters.Paths.contains('C://test/dir/dir2', root))
        self.assertTrue(filters.Paths.contains('C://test/dir/dir2/', root))

        self.assertFalse(filters.Paths.contains('C://test/', root))
        self.assertFalse(filters.Paths.contains('C://test', root))
        self.assertFalse(filters.Paths.contains('C://test/dir2', root))
        self.assertFalse(filters.Paths.contains('C://test/dir2/', root))

        self.assertTrue(filters.Paths.contains('test/dir/', 'test/dir'))
        self.assertTrue(filters.Paths.contains('test/dir', 'test/dir'))

        self.assertFalse(filters.Paths.contains('test/dir/', 'test/dir/dir2'))
        self.assertFalse(filters.Paths.contains('test/dir', 'test/dir/dir2'))

        self.assertTrue(filters.Paths.contains('/test/dir/', '/test/dir/'))
        self.assertTrue(filters.Paths.contains('/test/dir', '/test/dir'))
        
        self.assertFalse(filters.Paths.contains('/test/dir/', '/test/dir/dir2'))
        self.assertFalse(filters.Paths.contains('/test/dir', '/test/dir/dir2'))

        self.assertTrue(filters.Paths.contains('D://test/dir/', 'D://test/dir/'))
        self.assertTrue(filters.Paths.contains('D://test/dir', 'D://test/dir'))

        self.assertFalse(filters.Paths.contains('D://test/dir/', 'D://test/dir/dir2'))
        self.assertFalse(filters.Paths.contains('D://test/dir', 'D://test/dir/dir2'))

        self.assertTrue(filters.Paths.contains('C://test/dir/', 'C://test/dir/'))
        self.assertTrue(filters.Paths.contains('C://test/dir', 'C://test/dir'))

        self.assertFalse(filters.Paths.contains('D://test/dir/', 'C://test/dir/'))
        self.assertFalse(filters.Paths.contains('D://test/dir', 'C://test/dir/'))

    def test_traversal(self):

        root = 'D://test/dir/./'

        self.assertTrue(filters.Paths.contains('D://test/dir/./', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/./dir2', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/.', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/././dir/../', root))

        self.assertFalse(filters.Paths.contains('D://test/dir/./../', root))
        self.assertFalse(filters.Paths.contains('D://test/dir/./../dir2', root))
        self.assertFalse(filters.Paths.contains('D://test/dir/../', root))
        self.assertFalse(filters.Paths.contains('D://test/dir/./.././dir/../', root))

        root = 'D://test/dir/./../'

        self.assertTrue(filters.Paths.contains('D://test/', root))
        self.assertTrue(filters.Paths.contains('D://test', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/', root))
        self.assertTrue(filters.Paths.contains('D://test/dir', root))

        self.assertTrue(filters.Paths.contains('D://test/dir/./../', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/./../dir2', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/../', root))
        self.assertTrue(filters.Paths.contains('D://test/dir/./.././dir/../', root))

        self.assertFalse(filters.Paths.contains('D://test/dir/./../../dir2', root))
        self.assertFalse(filters.Paths.contains('D://test/dir/./../../dir2/', root))
        self.assertFalse(filters.Paths.contains('D://test/dir/./../../', root))
        self.assertFalse(filters.Paths.contains('D://test/dir/./../.././dir/../', root))

    def test_os_paths(self):
    
        root = 'D://test/dir/'

        self.assertTrue(filters.Paths.contains(os.path.join('D://test/dir/', ''), root))
        self.assertTrue(filters.Paths.contains(os.path.join('D://test/dir/', 'dir2'), root))
        self.assertTrue(filters.Paths.contains(os.path.join('D://test/dir/', 'dir2/'), root))

        self.assertFalse(filters.Paths.contains(os.path.join('D://test/', ''), root))
        self.assertFalse(filters.Paths.contains(os.path.join('D://test/', 'dir2'), root))
        self.assertFalse(filters.Paths.contains(os.path.join('D://test/', 'dir2/'), root))

        self.assertFalse(filters.Paths.contains(os.path.join('C://test/dir/', ''), root))
        self.assertFalse(filters.Paths.contains(os.path.join('C://test/dir/', 'dir2'), root))
        self.assertFalse(filters.Paths.contains(os.path.join('C://test/dir/', 'dir2/'), root))

        self.assertTrue(filters.Paths.contains(os.path.join('/test/dir/', ''), root))
        self.assertTrue(filters.Paths.contains(os.path.join('/test/dir/', 'dir2'), root))
        self.assertTrue(filters.Paths.contains(os.path.join('/test/dir/', 'dir2/'), root))

        self.assertFalse(filters.Paths.contains(os.path.join('test/dir/', ''), root))
        self.assertFalse(filters.Paths.contains(os.path.join('test/dir/', 'dir2'), root))
        self.assertFalse(filters.Paths.contains(os.path.join('test/dir/', 'dir2/'), root))

        root = os.path.join('D://test/dir/', '')

        self.assertTrue(filters.Paths.contains(os.path.join('D://test/dir/', ''), root))
        self.assertTrue(filters.Paths.contains(os.path.join('D://test/dir/', 'dir2'), root))
        self.assertTrue(filters.Paths.contains(os.path.join('D://test/dir/', 'dir2/'), root))

        self.assertFalse(filters.Paths.contains(os.path.join('D://test/', ''), root))
        self.assertFalse(filters.Paths.contains(os.path.join('D://test/', 'dir2'), root))
        self.assertFalse(filters.Paths.contains(os.path.join('D://test/', 'dir2/'), root))

        self.assertFalse(filters.Paths.contains(os.path.join('C://test/dir/', ''), root))
        self.assertFalse(filters.Paths.contains(os.path.join('C://test/dir/', 'dir2'), root))
        self.assertFalse(filters.Paths.contains(os.path.join('C://test/dir/', 'dir2/'), root))

        self.assertTrue(filters.Paths.contains(os.path.join('/test/dir/', ''), root))
        self.assertTrue(filters.Paths.contains(os.path.join('/test/dir/', 'dir2'), root))
        self.assertTrue(filters.Paths.contains(os.path.join('/test/dir/', 'dir2/'), root))

    def test_drives(self):
        
        root = '//test/dir/'

        self.assertTrue(filters.Paths.contains('//test/dir/', root))
        self.assertTrue(filters.Paths.contains('//test/dir', root))
        self.assertTrue(filters.Paths.contains('//test/dir/dir2', root))
        self.assertTrue(filters.Paths.contains('//test/dir/dir2/', root))
        
        self.assertFalse(filters.Paths.contains('//test/', root))
        self.assertFalse(filters.Paths.contains('//test', root))
        self.assertFalse(filters.Paths.contains('//test/dir2', root))
        self.assertFalse(filters.Paths.contains('//test/dir2/', root))

        root = '//test/dir'

        self.assertTrue(filters.Paths.contains('//test/dir/', root))
        self.assertTrue(filters.Paths.contains('//test/dir', root))

        self.assertFalse(filters.Paths.contains('//test/', root))
        self.assertFalse(filters.Paths.contains('//test', root))

        root = '//test/D:/dir/'

        self.assertTrue(filters.Paths.contains('//test/D:/dir/', root))
        self.assertTrue(filters.Paths.contains('//test/D:/dir', root))
        self.assertTrue(filters.Paths.contains('//test/D:/dir/dir2', root))
        self.assertTrue(filters.Paths.contains('//test/D:/dir/dir2/', root))

        self.assertFalse(filters.Paths.contains('//test/D:/', root))
        self.assertFalse(filters.Paths.contains('//test/D:', root))
        self.assertFalse(filters.Paths.contains('//test/D:/dir2', root))
        self.assertFalse(filters.Paths.contains('//test/D:/dir2/', root))

        root = '//test/../'

        self.assertFalse(filters.Paths.contains('//test/', root))
