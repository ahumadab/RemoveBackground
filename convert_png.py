import io
from io import BytesIO

from PIL import Image


def convert_png(output_image_bytes: bytes) -> BytesIO:
    """
    Converts an image to png using PIL.
    :param output_image_bytes: The image to convert.
    :return: The converted image.
    """
    image = Image.open(io.BytesIO(output_image_bytes))
    output_io = io.BytesIO()
    image.save(output_io, format='PNG')
    output_io.seek(0)
    return output_io
