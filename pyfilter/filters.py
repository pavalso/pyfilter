import os


class Paths:
    
    @staticmethod
    def contains(path: os.PathLike | str, root: os.PathLike | str):
        pathd, bpath = os.path.splitdrive(os.path.abspath(path))
        rootd, broot = os.path.splitdrive(os.path.abspath(root))
        brelative = os.path.normpath(os.path.join(broot, os.path.relpath(bpath or os.path.sep, broot)))
        _, real = os.path.splitdrive(brelative)
        return pathd == rootd and os.path.isabs(broot) == os.path.isabs(real) and os.path.commonpath([broot, real]).startswith(broot)
