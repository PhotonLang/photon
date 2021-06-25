from PIL import Image # base PIL image class
from io import BytesIO # for safe bytes management
from typing import Tuple, Union, Optional, Any


def _save_to_buffer(image: Union[Image.Image, bytes, BytesIO], *, buffer: Optional[BytesIO] = None) -> BytesIO:
    buffer = buffer or BytesIO()
    if isinstance(image, BytesIO):
        return image
    elif isinstance(image, Image.Image):
        return image.save(buffer, image.format)
    elif isinstance(image, bytes):
        return BytesIO(image)



def _prepare_for_process(image: Union[bytes, BytesIO]) -> Image.Image:
    return Image.open(image)


def run_image_method(image: Image.Image, method: str, *args, **kwargs) -> Any:
    method = getattr(image, method)
    result = method(*args, **kwargs)
    return result



