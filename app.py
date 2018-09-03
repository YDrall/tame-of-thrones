import sys

import console_runner

supported_view = [
    'console',
]

version = '0.1.1'

if __name__ == '__main__':
    app_view = 'console'
    ruler_system = ''
    if len(sys.argv) > 1:
        app_view = sys.argv[1]
    if len(sys.argv) > 2:
        ruler_system = sys.argv[2]

    if app_view not in supported_view:
        print("{} view is not supported yet..".format(app_view))
        exit()
    if app_view == 'console':
        console_runner.run(ruler_system)
