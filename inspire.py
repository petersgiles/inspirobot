import random
import glob
import textwrap
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from image_utils import ImageText

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

        color = (250, 250, 250)

        img = ImageText(rand_image, mode='RGBA', background=(
            0, 0, 0, 0), encoding='utf8')  # 200 = alpha

        place = random.choice(['right', 'center', 'justify'])

        #write_text_box will split the text in many lines, based on box_width
        #`place` can be 'left' (default), 'right', 'center' or 'justify'
        #write_text_box will return (box_width, box_calculed_height) so you can
        #know the size of the wrote text
        # img.write_text_box((300, 50), caption, box_width=200, font_filename=font,
        #                 font_size=60, color=color)
        img.write_text_box((25, 50), caption, box_width=600, font_filename=font,
                           font_size=60, color=color, place=place)
        # img.write_text_box((300, 200), caption, box_width=200, font_filename=font,
        #                 font_size=15, color=color, place='center')
        # img.write_text_box((300, 275), caption, box_width=200, font_filename=font,
        #                 font_size=15, color=color, place='justify')

        #You don't need to specify text size: can specify max_width or max_height
        # and tell write_text to fill the text in this space, so it'll compute font
        # size automatically
        #write_text will return (width, height) of the wrote text
        # img.write_text((25, 60), caption, font_filename=font,
        #                font_size='fill', max_width=600, color=color)

        img.save('result.png')
        print(caption)
