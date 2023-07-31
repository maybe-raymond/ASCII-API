from fastapi import FastAPI, File
from PIL import Image
import io
import numpy as np


app = FastAPI()


def matchToASCII(symbol):
    chars = ["!", "#", "$", "%", "&"]           #the ASCII characters to be used 

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
 
    for vec in array:
        for i in vec:
            string += matchToASCII(i)
        string += "\n" 
    
    return string 



#an API endpoint 
@app.post("/upload")
async def makeASCII(file: bytes = File()):
    if not file:
        return {"message": "No file sent"}
    else:
        with Image.open(io.BytesIO(file)) as img:
            array = np.asarray(img)
            ascii = convertToAscii(array)
        return {"data":ascii} 
    



