from rembg import remove


def remove_background(input_image_bytes: bytes) -> bytes:
    """
    Remove the background from an image using rembg library.
    :param input_image_bytes: The image data in bytes.
    :return: bytes: The image data with the background removed in bytes.
    """
    output_image = remove(input_image_bytes)
    return output_image
