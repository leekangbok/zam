from twisted.internet import defer

from api.utils import refine_twisted_web_request


class Service:
    def __init__(self):
        self._items = {}

    @refine_twisted_web_request
    @defer.inlineCallbacks
    def object_network_v6(self, request):
        message = yield defer.succeed('object network v6')
        defer.returnValue(message)


def route(app):
    service = Service()
    app.route('/v6')(service.object_network_v6)
