import sys
from numpy import asarray
import numpy as np
from PIL import Image

from text2image import text2image

manual_str = '''
Usage:
    python3 main.py <target> [options]

Target:
    -f <filepath>       Convert any image to dot-based text
    -t <text>           Convert any text to vertically-aligned dot-based text
    
Options:
    -s <style>          Output style, other format-related params will be ignored if this option is specified. 
                        ['terminal', 'line']
                        
    -w <width>          Maximal width for each line
                        (default: 100)

    -b <background>     Light or dark background mode
                        ['dark', 'light']
                        (default: 'dark')
    
    -T <threshold>      Threshold for converting grayscale image to binary image
                        (default: 132)
'''


if len(sys.argv) < 2:
    print(manual_str)
else:
    # Commandline parameters parsing
    param_dict = dict()
    for i in range(1, len(sys.argv) - 1, 2):
        if '-' != sys.argv[i][0] or len(sys.argv[i]) != 2:
            print(manual_str)
            exit(-1)
        else:
            param_dict[sys.argv[i][1:]] = sys.argv[i+1]

    # All customized parameters
    MAX_R = None
    threshold = None
    dot_white = None
    image = None

    # Parse the target
    if 'f' in param_dict:
        image = Image.open(f'{sys.argv[1]}').convert('L')
    elif 't' in param_dict:
        filepath = 'text.png'
        text2image(param_dict['t'], font_size=50, output_path=filepath)
        image = Image.open(filepath).convert('L')
    else:
        print(manual_str)
        exit(-1)

    # Parse other arguments
    if 's' in param_dict:
        config_options = {
            'terminal': {
                'MAX_R': 100,
                'dot_white': True,
                'threshold': 132,
            },
            'line': {
                'MAX_R': 37,
                'dot_white': False,
                'threshold': 132,
            }
        }
        config = config_options[param_dict['s']]

        MAX_R = config['MAX_R']
        dot_white = config['dot_white']
        threshold = config['threshold']
    else:
        default_config = {
            'MAX_R': 100,
            'dot_white': True,
            'threshold': 132,
        }
        MAX_R = int(param_dict['w']) if 'w' in param_dict else default_config['MAX_R']
        dot_white = param_dict['b'] == 'dark' if 'b' in param_dict else default_config['dot_white']
        threshold = int(param_dict['T']) if 'T' in param_dict else default_config['threshold']

    # Resize the image
    R, C = image.size
    if MAX_R <= R:
        image = image.resize([MAX_R, int(C * (MAX_R / R))])
    else:
        ratio = MAX_R // R
        image = image.resize([R * ratio, C * ratio])


    def point2brail(brailList) -> str:
        if len(brailList) != 8:
            return ''
        else:
            brailList.reverse()
            brailHelperList=[0x80,0x40,0x20,0x10,0x8,0x4,0x2,0x1]
            brailNum=0x2800

            for i in range(8):
                if brailList[i] == 1:
                    brailNum += brailHelperList[i]
            return chr(brailNum)


    image_arr = asarray(image)
    R, C = image_arr.shape
    res = ''
    for r in range(0, R-4, 4):
        for c in range(0, C-2, 2):
            brailList = [0] * 8
            brailList[0] = 1 - int(dot_white) if image_arr[r][c] < threshold else int(dot_white)
            brailList[1] = 1 - int(dot_white) if image_arr[r+1][c] < threshold else int(dot_white)
            brailList[2] = 1 - int(dot_white) if image_arr[r+2][c] < threshold else int(dot_white)
            brailList[3] = 1 - int(dot_white) if image_arr[r][c+1] < threshold else int(dot_white)
            brailList[4] = 1 - int(dot_white) if image_arr[r+1][c+1] < threshold else int(dot_white)
            brailList[5] = 1 - int(dot_white) if image_arr[r+2][c+2] < threshold else int(dot_white)
            brailList[6] = 1 - int(dot_white) if image_arr[r+3][c] < threshold else int(dot_white)
            brailList[7] = 1 - int(dot_white) if image_arr[r+3][c+1] < threshold else int(dot_white)

            res += point2brail(brailList)
        res += '\n'
        
    print(res)