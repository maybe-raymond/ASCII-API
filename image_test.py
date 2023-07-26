from PIL import Image
import numpy as np 


def matchToASCII(symbol):
    chars = ["!", "#", "$", "%", "&"]           #the ASCII characters to be used 
    
    # adding a div so it makes it easier to mode the program. 
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


def convertToAscii(array):
    string = ""
    
    # helper function for 3d arrays  
    for vec in array:
        for i in vec:
            string += matchToASCII(i)
        string += "\n" 
    
    return string 





with Image.open("Test images/Zero.jpg") as img:
    data = np.asarray(img)
    result = convertToAscii(data)
    print(result)
