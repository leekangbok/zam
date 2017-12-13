from twisted.internet import defer

from api.utils import refine_twisted_web_request


class Service:
    def __init__(self):
        self._items = {}

    @refine_twisted_web_request
    @defer.inlineCallbacks
    def policy_forward_v6(self, request):
        message = yield defer.succeed('policy forward v6')
        defer.returnValue(message)


def route(app):
    service = Service()
    app.route('/v6')(service.policy_forward_v6)
