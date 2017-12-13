import json

from google.protobuf import json_format
from twisted.internet import defer

from api.utils import refine_twisted_web_request
from app import common
from grpc_service.ipObject import IpObjectServ


class Service:
    def __init__(self):
        self._items = {}

    @refine_twisted_web_request
    @defer.inlineCallbacks
    def policy_forward_v4(self, request):
        success, item = yield common.fetch_objects(IpObjectServ, uids=[])
        if success:
            i = [json_format.MessageToDict(i) for i in item]
            defer.returnValue(json.dumps(i, indent=4))
        defer.returnValue('failure')


def route(app):
    service = Service()
    app.route('/v4')(service.policy_forward_v4)
