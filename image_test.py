from PIL import Image
import numpy as np 


def matchToASCII(symbol):
    chars = ["!", "#", "$", "%", "&"]
    
    if symbol < 50:
        return chars[0]
    elif symbol < 100 :
        return chars[1]
    elif symbol < 150:
        return chars[2]
    elif symbol < 200:
        return chars[3]
    else:
        return chars[4]




with Image.open("Test images/Zero.jpg") as img:
    data = np.asarray(img)
    print(data)
