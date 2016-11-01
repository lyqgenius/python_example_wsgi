class ShowVersion():
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        print "app:ShowVersion is called."
        start_response("200 OK", [("Content-type", "text/plain")])
        return ["Paste Deploy LAB: Version = 1.0.0", ]

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in ShowVersion.factory", global_conf, kwargs
        return ShowVersion()
