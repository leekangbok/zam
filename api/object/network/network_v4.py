from twisted.internet import defer

from api.utils import refine_twisted_web_request


class Service:
    def __init__(self):
        self._items = {}

    @refine_twisted_web_request
    @defer.inlineCallbacks
    def object_network_v4(self, request):
        message = yield defer.succeed('object network v4')
        defer.returnValue(message)


def route(app):
    service = Service()
    app.route('/v4')(service.object_network_v4)
