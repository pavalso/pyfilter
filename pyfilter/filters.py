import os
import re


class Paths:

    _traversal_rgx = r'\.{1,2}((\/|\\)|$)'

    @staticmethod
    def contains(path: os.PathLike | str, root: os.PathLike | str = ''):
        pathd, bpath = os.path.splitdrive(os.path.abspath(path))
        rootd, broot = os.path.splitdrive(os.path.abspath(root))
        brelative = os.path.normpath(os.path.join(broot, os.path.relpath(bpath or os.path.sep, broot)))
        _, real = os.path.splitdrive(brelative)
        return pathd.casefold() == rootd.casefold() and os.path.isabs(broot) == os.path.isabs(real) and os.path.commonpath([broot, real]).startswith(broot)

    @staticmethod
    def traversal_filter(path: os.PathLike | str):
        while re.search(Paths._traversal_rgx, path):
            path = re.sub(Paths._traversal_rgx, '', path)
        return path
