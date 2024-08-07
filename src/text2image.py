from PIL import Image, ImageDraw, ImageFont

def text2image(text, font_path='/System/Library/Fonts/PingFang.ttc', font_size=20, output_path='text.png'):
    font = ImageFont.truetype(font_path, font_size)

    max_width = max(font.getsize(char)[0] for char in text)
    total_height = sum(font.getsize(char)[1] for char in text)
    
    image = Image.new('RGB', (max_width + 5, total_height + 15), 'white')
    draw = ImageDraw.Draw(image)

    cur_x, cur_y = 2, 3
    for char in text:
        draw.text((cur_x, cur_y), char, font=font, fill='black')
        cur_y += font.getsize(char)[1]

    image.save(output_path)

text = "林芊妤"
text2image(text, font_size=50)
