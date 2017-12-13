from .forward import route as forward_route


def route(app):
    with app.subroute("/policy") as app:
        forward_route(app)
