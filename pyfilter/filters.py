import os


class Paths:
    
    @staticmethod
    def contains(path: os.PathLike | str, root: os.PathLike | str = ''):
        pathd, bpath = os.path.splitdrive(os.path.abspath(path))
        rootd, broot = os.path.splitdrive(os.path.abspath(root))
        brelative = os.path.normpath(os.path.join(broot, os.path.relpath(bpath or os.path.sep, broot)))
        _, real = os.path.splitdrive(brelative)
        return pathd.casefold() == rootd.casefold() and os.path.isabs(broot) == os.path.isabs(real) and os.path.commonpath([broot, real]).startswith(broot)

    @staticmethod
    def relative(path: os.PathLike | str, root: os.PathLike | str = ''):
        broot = os.path.abspath(root)
        if not Paths.contains(path, broot):
            return broot
        brelative = os.path.relpath(path or os.path.sep, broot)
        return os.path.abspath(os.path.join(broot, brelative))

if __name__ == '__main__':
    print(Paths.relative('D://test/dir/dir2', 'D://test/dir/'))
