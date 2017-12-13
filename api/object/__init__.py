from .network import route as network_route


def route(app):
    with app.subroute("/object") as app:
        network_route(app)
