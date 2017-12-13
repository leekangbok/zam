from .network_v4 import route as network_v4_route
from .network_v6 import route as network_v6_route


def route(app):
    with app.subroute("/network") as app:
        network_v4_route(app)
        network_v6_route(app)
