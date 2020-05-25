from .engine import Code
from .auth import Auth


def init_routes(api):
    api.add_resource(Code, '/code')
    api.add_resource(Auth, '/auth/<string:username>')
