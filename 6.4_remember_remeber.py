import numpy as np
from PIL import Image


def read_secret_messages(file_path):
    """
    Reads a secret message encoded in an image file,
     where the message is hidden by the ascii code of row setting the pixel values to 1 (black).

    Args:
        file_path (str): The path to the image file containing the secret message.
    """
    msg = ""
    # Open the image file
    img = Image.open(file_path)
    img_array = np.array(img)
    height, width = img_array.shape
    # Loop over each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the pixel values at (x, y)
            value = img_array[y, x]

            # Check if the pixel is black
            if value == 1:
                msg += chr(y)
    print(msg)

if __name__ == "__main__":
    logo_path = "code.png"
    read_secret_messages(logo_path)
