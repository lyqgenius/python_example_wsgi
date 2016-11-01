import os

from paste.deploy import loadapp
from wsgiref.simple_server import make_server

import openstack.service as service


def main():
    server = service.WSGIService('example_wsgi')
    server.start()
    # url_map_test()


def show_version_test():
    path = os.path.join(os.getcwd(), 'api-paste.ini')
    wsgi_app = loadapp("config:%s" % os.path.abspath(path), 'show_version')
    server = make_server('0.0.0.0', 8888, wsgi_app)
    server.serve_forever()


def url_map_test():
    path = os.path.join(os.getcwd(), 'api-paste.ini')
    wsgi_app = loadapp("config:%s" % os.path.abspath(path), 'url_map')
    server = make_server('0.0.0.0', 8888, wsgi_app)
    server.serve_forever()


if __name__ == '__main__':
    # show_version_test()
    url_map_test()
