import PIL.Image

Chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize(image):
    new_width = 100
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image 

def conv_grey(image):
    gray_image = image.convert("L")
    return gray_image

def conv_ascii(image):
    pixels = image.getdata()

    if isinstance(pixels[0], tuple):
        pixels = [sum(p) // 3 for p in pixels]

    characters = "".join([Chars[pixel // 25] for pixel in pixels])
    return characters


path=input("Enter path")

try:
    image = PIL.Image.open(path)
    image_res = resize(image)
    image_conv = conv_grey(image_res)
    final_image = conv_ascii(image_conv)
    new_width = 100
    pixel_count = len(final_image)
    ascii_image = "\n".join([final_image[index:(index + new_width)] for index in range(0, pixel_count, new_width)])
    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
