import os
import re


class Paths:

    _traversal_rgx = r'\.{1,2}((\/|\\)|$)'

    @staticmethod
    def contains(path: os.PathLike | str, root: os.PathLike | str = ''):
        rootd, broot = os.path.splitdrive(os.path.abspath(root))
        pathd, bpath = os.path.splitdrive(os.path.abspath(os.path.join(root, path)))
        brelative = os.path.normpath(os.path.join(broot, os.path.relpath(bpath or os.path.sep, broot)))

        if pathd.casefold() != rootd.casefold() or os.path.isabs(broot) != os.path.isabs(brelative) or not os.path.commonpath([broot, brelative]).startswith(broot):
            return None

        return os.path.join(rootd, brelative)

    @staticmethod
    def traversal_filter(path: os.PathLike | str):
        while re.search(Paths._traversal_rgx, path):
            path = re.sub(Paths._traversal_rgx, '', path)
        return path
