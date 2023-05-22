import unittest
import os

from pyfilter import filters


class TestTraversalFilter(unittest.TestCase):

    def test_filter(self):
        self.assertEqual(filters.Paths.traversal_filter('dir'), 'dir')
        self.assertEqual(filters.Paths.traversal_filter('dir/'), 'dir/')
        self.assertEqual(filters.Paths.traversal_filter('dir\\'), 'dir\\')
        self.assertEqual(filters.Paths.traversal_filter('dir/.'), 'dir/')
        self.assertEqual(filters.Paths.traversal_filter('dir/..'), 'dir/')
        self.assertEqual(filters.Paths.traversal_filter('dir/../'), 'dir/')
        self.assertEqual(filters.Paths.traversal_filter('dir/./'), 'dir/')
        self.assertEqual(filters.Paths.traversal_filter('dir/./.'), 'dir/')
        self.assertEqual(filters.Paths.traversal_filter('dir/./..'), 'dir/')
        self.assertEqual(filters.Paths.traversal_filter('dir/./../'), 'dir/')

        self.assertEqual(filters.Paths.traversal_filter('dir\\.'), 'dir\\')
        self.assertEqual(filters.Paths.traversal_filter('dir\\..'), 'dir\\')
        self.assertEqual(filters.Paths.traversal_filter('dir\\..\\'), 'dir\\')
        self.assertEqual(filters.Paths.traversal_filter('dir\\.\\'), 'dir\\')
        self.assertEqual(filters.Paths.traversal_filter('dir\\.\\.'), 'dir\\')
        self.assertEqual(filters.Paths.traversal_filter('dir\\.\\..'), 'dir\\')

        self.assertEqual(first=filters.Paths.traversal_filter('.dir'), second='.dir')
        self.assertEqual(first=filters.Paths.traversal_filter('..dir'), second='..dir')
        self.assertEqual(first=filters.Paths.traversal_filter('/.dir'), second='/.dir')
        self.assertEqual(first=filters.Paths.traversal_filter('\\.dir'), second='\\.dir')
        self.assertEqual(first=filters.Paths.traversal_filter('../dir'), second='dir')
        self.assertEqual(first=filters.Paths.traversal_filter('../../dir'), second='dir')
        self.assertEqual(first=filters.Paths.traversal_filter('./dir'), second='dir')
        self.assertEqual(first=filters.Paths.traversal_filter('.././dir'), second='dir')

        self.assertEqual(first=filters.Paths.traversal_filter('./dir/.'), second='dir/')
        self.assertEqual(first=filters.Paths.traversal_filter('./dir/..'), second='dir/')
        self.assertEqual(first=filters.Paths.traversal_filter('./dir/../'), second='dir/')
        self.assertEqual(first=filters.Paths.traversal_filter('./dir/./'), second='dir/')

        self.assertEqual(first=filters.Paths.traversal_filter('../dir/.'), second='dir/')
        self.assertEqual(first=filters.Paths.traversal_filter('../dir/..'), second='dir/')

        self.assertEqual(first=filters.Paths.traversal_filter('....//dir'), second='dir')
        self.assertEqual(first=filters.Paths.traversal_filter('....\\\\dir'), second='dir')
        self.assertEqual(first=filters.Paths.traversal_filter('./..\\dir'), second='dir')
