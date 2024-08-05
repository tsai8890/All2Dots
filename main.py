import sys
from numpy import asarray
import numpy as np
from PIL import Image

if len(sys.argv) < 2:
    print('''
Usage:
    python3 main.py <filepath> [output_env]

output_env:
   # This parameter is not case-sensitive
   terminal         for terminal windows, default option
   line             for the LINE chatting window
''')
else:
    # Commandline parameters parsing
    file_path = sys.argv[1]
    output_env = sys.argv[2].lower() if len(sys.argv) >= 3 else 'terminal'

    # Output config setting
    config_options = {
        'terminal': {
            'MAX_R': 100,
            'dot_white': True,
            'threshold': 132,
        },
        'line': {
            'MAX_R': 37,
            'dot_white': True,
            'threshold': 132,
        }
    }
    config = config_options[output_env]

    MAX_R = config['MAX_R']
    threshold = config['threshold']
    dot_white = config['dot_white']

    # Resize the image
    image = Image.open(f'{sys.argv[1]}').convert('L')
    R, C = image.size
    image = image.resize([R // (R // MAX_R), C // (R // MAX_R)])


    def point2brail(brailList) -> str:
        if len(brailList) != 8:
            return ''
        else:
            brailList.reverse()
            brailHelperList=[0x80,0x40,0x20,0x10,0x8,0x4,0x2,0x1]
            brailNum=0x2800

            dots = 0
            for i in range(8):
                if brailList[i] == 1:
                    brailNum += brailHelperList[i]
                    dots += 1
            
            return chr(brailNum) if dots > 0 else ' '


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