from klein import Klein

from api.policy import route as policy_route
from api.object import route as object_route

app = Klein()

with app.subroute("/api") as app:
    policy_route(app)
    object_route(app)