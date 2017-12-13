from .forward_v4 import route as forward_v4_route
from .forward_v6 import route as forward_v6_route


def route(app):
    with app.subroute("/forward") as app:
        forward_v4_route(app)
        forward_v6_route(app)
