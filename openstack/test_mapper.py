from routes import Mapper


def test_name():
    map = Mapper()
    map.connect(None, "/message/:name", controller='my_contro')
    result = map.match('/message/12')
    print result


def test_action():
    map = Mapper()
    map.connect(None, "error/{action}/{id}", controller="controller_obj")
    result = map.match('error/myapp/4')
    print result


if __name__ == '__main__':
    test_action()
    test_name()
