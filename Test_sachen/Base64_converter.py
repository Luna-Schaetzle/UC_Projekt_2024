import base64

def image_to_string(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

# Example usage
image_path = r"C:\Users\Admin\Desktop\Desk\Junior_Companies\1701424803087.png"
image_string = image_to_string(image_path)
with open("converted_picture.txt", "w") as file:
    file.write(image_string)