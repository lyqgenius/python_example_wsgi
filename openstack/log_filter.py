class LogFilter():
    def __init__(self, app):
        self.app = app
        pass

    def __call__(self, environ, start_response):
        print "filter:LogFilter is called."
        print 'app:', self.app
        return self.app(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in LogFilter.factory", global_conf, kwargs
        return LogFilter
