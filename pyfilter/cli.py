import pyfilter


def main():
    from werkzeug.serving import run_simple
    import argparse

    parser = argparse.ArgumentParser(
        prog = pyfilter.__program__,
        description = 'A simple web server for viewing files and directories.',
        epilog = 'Made by %s.' % pyfilter.__author__)

    parser.add_argument(
        '-v', '--version',
        action = 'version',
        version = '%(prog)s v' + pyfilter.__version__)

    parser.add_argument(
        '-H', '--host',
        metavar = 'HOST',
        default = 'localhost',
        help = 'the host to listen on (default: %(default)s)')

    parser.add_argument(
        'port',
        metavar = 'PORT',
        type = int,
        nargs='?',
        default = 5000,
        help = 'the port to listen on (default: %(default)s)')
    
    parser.add_argument(
        '-P', '--path',
        metavar = 'PATH',
        default = '.',
        help = 'the path to serve (default: %(default)s)')
    
    parser.add_argument(
        '-T', '--templates-folder',
        metavar = 'TEMPLATES_FOLDER',
        default = None,
        help = 'the path to the templates folder (default: %(default)s)')

    args = parser.parse_args()

    host = args.host
    port = args.port

    app = pyfilter.httpServer.HttpServer.create_app(**vars(args))

    run_simple(host, port, app, threaded=True)
