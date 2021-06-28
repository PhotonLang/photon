from lark import Transformer, v_args
from .prelude import Env
from . import helpers
from .statements import *

@v_args(inline = True)
class PhotonTransformer(Transformer):
    def __init__(self, environment: Env):
        self._env = environment
        super().__init__()
    def open_stmt(self, fp: str, vnr: str) -> Open:
        # vnt - variable name representation
        # opens an image and returns a simple 'Open' object to represent the open statement pythonically
        io = helpers.safe_read(fp)
        self._env._insert(vnr, io)
        return Open(io, vnr)

    def string(self, value: str) -> str:
        # parses the regexed string into a pythonic string
        return value.strip("'").strip('"')

    


