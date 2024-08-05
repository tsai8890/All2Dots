import sys
from numpy import asarray
import numpy as np
from PIL import Image

if len(sys.argv) != 2:
    print('enter the image\'s path')
else:
    MAX_R = 100

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

            for i in range(8):
                if brailList[i] == 1:
                    brailNum += brailHelperList[i]
            return chr(brailNum)


    image_arr = asarray(image)
    R, C = image_arr.shape
    threshold = 132
    res = ''

    for r in range(0, R-4, 4):
        for c in range(0, C-2, 2):
            brailList = [0] * 8
            brailList[0] = 0 if image_arr[r][c] < threshold else 1
            brailList[1] = 0 if image_arr[r+1][c] < threshold else 1
            brailList[2] = 0 if image_arr[r+2][c] < threshold else 1
            brailList[3] = 0 if image_arr[r][c+1] < threshold else 1
            brailList[4] = 0 if image_arr[r+1][c+1] < threshold else 1
            brailList[5] = 0 if image_arr[r+2][c+2] < threshold else 1
            brailList[6] = 0 if image_arr[r+3][c] < threshold else 1
            brailList[7] = 0 if image_arr[r+3][c+1] < threshold else 1

            res += point2brail(brailList)
        res += '\n'
        
    print(res)