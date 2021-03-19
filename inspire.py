import random
import glob
import textwrap
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from image_utils import ImageText


def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale



imagefiles = glob.glob('images/*.jpg')
fontfiles = glob.glob('fonts/**/*.otf')

with open('text/phrases.txt', encoding="utf8") as phrase_file:
    phrase_list = phrase_file.readlines()

    with open('text/answers.txt', encoding="utf8") as answers_file:
        answers_list = answers_file.readlines()

        caption = random.choice(phrase_list).replace("{replace}", random.choice(answers_list), 1).replace(
            "{replace}", random.choice(answers_list), 1).replace('\n', '').replace('\r', '')

        rand_image = Image.open(random.choice(imagefiles))

        font = random.choice(fontfiles)

        brightness = calculate_brightness(rand_image)

        print(brightness)

        color = (0, 0, 0) if brightness > 0.35 else (255, 255, 255)

        img = ImageText(rand_image, mode='RGBA', background=(0, 0, 0, 0), encoding='utf8')  # 200 = alpha

        place = random.choice(['right', 'center', 'justify'])

        img.write_text_box((25, 25), caption, box_width=600, font_filename=font,
                           font_size=65, color=color, place=place)

        img.save('result.png')
        print(caption)
