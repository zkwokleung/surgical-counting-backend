import base64
from sys import argv

if __name__ == "__main__":
    # The path to the image
    file = argv[1]
    # Open the image
    with open(file, "rb") as img_file:
        # Encode the image to base64
        img_str = base64.b64encode(img_file.read())

    # Decode the image from base64
    img = base64.b64decode(img_str)
    # Open the image
    with open("output.jpg", "wb") as img_file:
        # Write the image to a file
        img_file.write(img)
