import wsgi


class ControllerTest(object):
    def __init__(self):
        print "openstack.router:ControllerTest.init"

    def test(self, req):
        print "openstack.router:ControllerTest.test", "req:", req
        return {
            'name': "test",
            'properties': "test"
        }


class Router(wsgi.Router):
    def __init__(self, mapper):
        print "openstack.router:Router.init", "req:"
        controller = ControllerTest()
        mapper.connect('/test',
                       controller=wsgi.Resource(controller),
                       action='test',
                       conditions={'method': ['GET']})
        super(Router, self).__init__(mapper)
