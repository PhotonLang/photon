from io import BytesIO
import functools

from typing import Union
from concurrent import futures

from .prelude import Env, AsyncEnv
from .errors import ConfigError, RunError

from . import _polaroid
from . import helpers


class Open:
    """
    Represents a generic OPEN statement. Can be subclassed later to represent advanced Open statements
    """
    def __init__(self, io: BytesIO, identifier: str):
        self.io = io
        self.identifier = identifier

    def _exec(self, env: Union[AsyncEnv, Env]):
        env._insert(self.identifier, self.io)

class Apply:
    """
    Represents a generic APPLY statement.
    """
    def __init__(self, effect: str, identifier: str):
        self.effect = effect
        self.identifier = identifier

    def _exec(self, env: Union[AsyncEnv, Env]):
        image = env.get(self.identifier)
        if image:
            polaroid_image = _polaroid._prepare_for_process(image)
            result_image = _polaroid.run_image_method(polaroid_image, self.effect)
            buffer = _polaroid._save_to_buffer(result_image)
            buffer.seek(0)
            env.update(self.identifier, buffer)


    
class Save:
    """
    Represents a generic SAVE statement.
    """
    def __init__(self, identifier: str, fp: str):
        self.identifier = identifier
        self.fp = fp

    def _exec(self, env: Env):
        image = env.get(self.identifier)
        helpers.safe_save(image, self.fp)


class Close:
    """
    Represents a generic CLOSE statement.
    """
    def __init__(self, identifier: str):
        self.identifier = identifier
    
    def _exec(self, env: Env):
        env._remove(self.identifier)

class CompileState:
    """
    Represents a compiled state containing all the transformed Statement Objects
    """
    def __init__(self, statements: Union[tuple, list]):
        self.statements = statements

    def run(self, env: Env, *, skip_check: bool = False):
        if env._async is not True and skip_check is False:
            for i in self.statements:
                i._exec(env)
        else:
            raise RunError("Async mode is enabled, cannot run with blocking function.")


    async def run_async(self, env: Env, *, executor: futures.ThreadPoolExecutor = None):
        if env._async is True:
            partial = functools.partial(self.run, env, skip_check = True)
            executor = executor or futures.ThreadPoolExecutor(env._async_config.max_workers)
            await env.loop.run_in_executor(executor, partial)




    
