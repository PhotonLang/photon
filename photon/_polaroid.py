from polaroid import Image
from io import BytesIO
from typing import Union, Optional

def _save_to_buffer(image: Union[Image, bytes, BytesIO], *, buffer: Optional[BytesIO] = None) -> BytesIO:
    # allow for buffer kwarg for consistency among libraries
    if isinstance(image, BytesIO):
        return image
    elif isinstance(image, Image.Image):
        return BytesIO(image.save_bytes())
    elif isinstance(image, bytes):
        return BytesIO(image)

def _prepare_for_process(image: Union[bytes, BytesIO]) -> Image:
    if isinstance(image, BytesIO):
        return Image(image.getvalue())
    elif isinstance(image, bytes):
        return Image(image)
    

def run_image_method(image: Image, method: str, *args, **kwargs):
    method = getattr(image, method)
    result = method(*args, **kwargs)
    return result if result is not None else image