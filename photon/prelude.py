import requests
import aiohttp
import asyncio

from typing import Dict, Union, Callable, Any
from io import BytesIO
from concurrent import futures

class Env:
    def __init__(self) -> None:
        self._images: Dict[str, BytesIO] = {} # likely config: IMAGE_IDENTIFIER: BytesIO
        self._sync_http_session: requests.Session = None # this is filled in the first request
        self._async_http_session: aiohttp.ClientSession = None # this is filled in the first async request
        self._loop = asyncio.get_event_loop()

    def __repr__(self) -> str:
        return "<Env images={}>".format(str(self._images))


    def _insert(self, identifier: str, image: BytesIO):
        self._images[identifier] = image # we cannot have 2 identifiers with the same name however one identifier can switch what values it holds

    def _remove(self, identifier: str):
        self._images.pop(identifier, None) # remove an identifier, silently failing if it does not exist

    
    def get(self, identifier: str, *, kv: bool = False) -> Union[Dict[str, BytesIO], BytesIO, None]:
        result = self._images.get(identifier)
        if kv is True:
            return {identifier, result}
        else:
            return result

    def update(self, identifier: str, image: BytesIO):
        self._images[identifier] = image

    async def _request_async(self, url: str, method: str = "GET", *args, **kwargs) -> aiohttp.ClientResponse:
        if self._async_http_session is None or self._async_http_session.closed is True:
            self._async_http_session = aiohttp.ClientSession(raise_for_status = True)
        
        resp = await self._async_http_session.request(method, url, *args, **kwargs)
        return resp

    def _request_sync(self, url: str, method: str = "GET", *args, **kwargs) -> requests.Response:
        if self._sync_http_session is None:
            self._sync_http_session = requests.Session()
        
        resp = self._sync_http_session.request(method, url, *args, **kwargs)
        return resp

    def exec(self, func: Callable, *args, **kwargs) -> Any:
        # easy subclass for AsyncEnv
        if asyncio.iscoroutinefunction(func):
            return self._loop.run_until_complete(func(*args, **kwargs))

        return func(*args, **kwargs)
        




class AsyncEnv(Env):
    def __init__(self, *, max_workers: int) -> None:
        super().__init__()
        self._executor = futures.ThreadPoolExecutor(max_workers)

    async def exec(self, func: Callable, *args, **kwargs) -> Any:
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        else:
            return await self._loop.run_in_executor(self._executor, func(*args, **kwargs))

    
    

    




