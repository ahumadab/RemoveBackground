from remove_background import remove_background
from PIL import Image
import io


def main():
    input_path = 'image.jpg'  # le chemin de l'image que vous souhaitez traiter
    output_path = 'image_rem.png'  # Chemin où l'image traitée sera sauvegardée

    with open(input_path, 'rb') as file:
        input_image_bytes = file.read()

    output_image_bytes = remove_background(input_image_bytes)

    output_image = Image.open(io.BytesIO(output_image_bytes))
    output_image.save(output_path)

    print(f"Processed image saved to {output_path}")


if __name__ == '__main__':
    main()

