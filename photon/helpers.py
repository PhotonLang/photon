import time
import json

from io import BytesIO

def unsafe_save(image: bytes, path: str) -> None:
    with open(path, "wb+") as temp:
        temp.write(image)

    
def safe_save(image: BytesIO, path: str) -> None:
    # we call this "safe" as we give this an IO handler rather than raw bytes
    # our IO retrieves these bytes safely locally in our function
    with open(path, "wb+") as temp:
        raw_bytes = image.getvalue()
        temp.write(raw_bytes)

def read_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def safe_read(path: str) -> BytesIO:
    with open(path, "rb") as temp:
        raw_bytes = temp.read()
    # exit from our context manager to close our file
    # we no longer need it open

    buffer = BytesIO(raw_bytes)
    return buffer


def read_lark_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

def read_photon_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


class TimerHelper:
    def __init__(self):
        self._start = None
        self._end = None
    
    def start(self) -> None:
        self._start = time.perf_counter()
    
    def end(self) -> None:
        self._end = time.perf_counter()
    
    def time(self) -> float:
        if self._start is None:
            raise ValueError("_start is None")
        elif self._end is False:
            raise ValueError("_end is None")
        return self._end - self._start



