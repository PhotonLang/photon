from typing import Union
from lark import Transformer, v_args

from . import helpers
from .statements import *



@v_args(inline = True)
class PhotonTransformer(Transformer):
    def open_stmt(self, fp: str, vnr: str) -> Open:
        # vnt - variable name representation
        # opens an image and returns a simple 'Open' object to represent the open statement pythonically
        io = helpers.safe_read(fp)
        return Open(io, vnr)

    def apply_stmt(self, effect: str, identifier: str) -> Apply:
        return Apply(effect, identifier)

    def save_stmt(self, identifier: str, fp: str) -> Save:
        return Save(identifier, fp)

    def close_stmt(self, identifier: str) -> Close:
        return Close(identifier)

    def string(self, value: str) -> str:
        # parses the regexed string into a pythonic string
        return value.strip("'").strip('"')

    def integer(self, value: Union[str, int]) -> int:
        # parses the regexed string into a pythonic integer
        return int(value)

    def NAME(self, value: str) -> str:
        return self.string(value)

    def start(self, *statements) -> CompileState:
        return CompileState(statements)


    



    


    


