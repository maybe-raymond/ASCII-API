# ASCII Art API in FastAPI

## Introduction

In this tutorial, you will learn how to create an ASCII art API that can convert both text and images to ASCII. You will start by learning what an image file really is, and then you will build an API that will generate ASCII ART for you given the required image. By the end of this tutorial, you will have a working API that you can use to create ASCII art from any image.

### Requirements

To create this API, we'll need:

* [Python](https://www.python.org/) 3.6+ installed
* [Git](https://git-scm.com/)

### Setting Up Our Environment

We will create a virtual Python environment using Venv. Firstly, lets create a local directory. This directory will be called ASCII Art, then you should open the terminal in this directory. To create the Virtual Environment enter the command:

``` python
python -m venv env
```

__note__ : Depending on how you set up your Enviroment variables when you installed python the above command might not work. If the above command does not work switch the `python` part with `python`.  If this change fails then plaese go to this [link](https://docs.python.org/3/library/venv.html) or [this one](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) for extra information

To activate the virtual environment using the following command for your operating system

* __Linux/MacOSX:__  

``` Bash
source env/bin/activate
```

* __Windows:__  

``` batch
source env\Scripts\activate.bat
```

if the virual environment activated correctly, you should see (env) to the left of your name in the terminal. It should look something like this:

![terminal](Images/env.png)

### Installing Dependencies

Now that we've got our virtual environment set up, we can look at the packages we're gonna use:

* [Pillow](https://pillow.readthedocs.io/en/) is a fantastic Python package that allows us to process and manipulate images.
* [FastAPI](https://fastapi.tiangolo.com/) is a web development framework that provides tools that make it easy for building, documenting and maintaining APIS
* [NumPy](https://numpy.org/) is a library used for scientific computing which will come in handy manipulating images.
* [unicorn](https://pypi.org/project/unicorn/) is a server that will help serve our API
* [python-multipart](https://pypi.org/project/python-multipart/) this package will help use with dealing with form data

``` bash
pip install numpy, pillow, fastapi , "uvicorn[standard], python-multipart
```

__note__ : if pip does not work you can try `pip3` instead.

### Downloading test images

we will also need some test images to help us convert and test our API. Please create a new folder in your project directory called Test images. After this we need to download the images from our [Github respository](https://github.com/maybe-raymond/ASCII-API) in the folder called Test images.


## What the Devil is ASCII art ?

ASCII art is just representing pictures as letters and symbols. The ASCII part of the name just represents the character set we are going to us to make our images.

Here's an example of a simple cat in ASCII:

``` bash
 /\_/\
( o.o )
 > ^ <
```


As we can see the image is just made up of letters and symbols. we are going to be doing something like this but we will be converting actual images to ASCII art text.

Now that we know what ASCII art is we can move to the coding section, but first neeed to answer an important question.


## What really is a digitial image ?

Computers interpert visual images in formats such as `.png, jpeg and webp` as a two dimensional(2D) array or a matrix.These matrix's store the value of every pixel.Some image formats represent images as three dimensional(3D) arrays were the value of the inner array is another array of RGB vaules. The best way to understand all this is by doing.

Let's create a file called `image_test.py`. we will first import the Image class from the Pillow package and then we import numpy. We then open an image in out `Test images` folder using the Image class. The function np.asarray just converts an image into it's representation as an array. We then print this array.

``` python
from PIL import Image
import numpy as np 


with Image.open("Test images/Zero.jpg") as img: # opening image
    data = np.asarray(img) # converting img to array
    print(data)

```

When we run the file, we should some output which looks like this

![2d Array output](Images/2dArray.png)

As we can see the image is just an array of array with numbers. These numbers will represent a values between 0 and 255. The image we converted is grayscale and so is not in the RGB format. so the images represent the brightness or intensity of the value, where 0 is black and 255 is white. if it was in RGB the values would become an an array and be in the format of (R, G, B) were each number represents the colour of the pixel. For example the colour of orange of a singular pixel will be (255, 165, 0) which represents the intensity of the colours Red, Green and Blue.

## Let's convert our Image to ASCII

As we learned above the ASCII art is just making an image out of letters and symbols. We also just learnt that an image is just a bunch of pixel values in an array of arrays. So to convert an iamge to ASCII we just need to convert each pixel value into some value that corresponds to an ASCII symbol

Open up `image_test.py` and create a new function called `matchToASCII` that will match a pixel value to an ASCII value. it should look something like this


```python
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

```

The condtional statement in the code above just breaks up the pixel values in ranges of 50's and assigns a certain ASCII characcter to that particular value. We are gonna improve on this code later but this is just to show us how the logic is supposed to work.


Now let's create the actual function that converts the array to ASCII art. We are gonna call this new function `convertToAscii`, the code should look something like this.

```python
def convertToAscii(array):
    string = ""
    
    for vec in array:
        for i in vec:
            string += matchToASCII(i)
        string += "\n" 
    
    return string 
```

The code just loops through both arrays and converts every pixel value into it's equivalent ASCII character. We will come back to this code and add some modifications that will make it more robust. Now lets modify the code that opens the image so that it incorporates our new function.

```python
with Image.open("Test images/Zero.jpg") as img:
    data = np.asarray(img)
    result = convertToAscii(data)
    print(result)

```

Our code should now look something like this 

``` python
from PIL import Image
import numpy as np 


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



with Image.open("Test images/Zero.jpg") as img:
    data = np.asarray(img)
    result = convertToAscii(data)
    print(result)

```

When you run the aboove code we should see some output that looks like the following.

![zero output](Images/zeroOutput.png)

## Creating our API

Now we'll get into creating our API in [FastAPI](https://fastapi.tiangolo.com/). We are going to be creating our API endpoint called `/upload`


### Setting up FastAPI

First, we need to create two new files which will be called `__init__.py` and `app.py`. The `__init__.py` file is a special python directory and used to strucutre python code but for this tutorial it will remian empty. The `app.py` is were we will create our API.

The code below is a basic FastAPI API

```python
from fastapi import FastAPI

app = FastAPI()



#an API endpoint 
@app.get("/")
def Hello():
    return {"Hello": "World"}

```

To run the above code type in the command below 


``` bash 
uvicorn app:app --reload
```

you should get some output that looks like the following. 

![FastAPI output](Images/FastApi.png)

if you click the 127.0.0.1:8000 URL, it should open your web browser and see some JSON output. 

### creating our /upload endpoint

The first thing we need to do is to create a new function called `makeASCII` that should handle image file uploads from form data. The function should look like this

``` python
from fastapi import FastAPI, file

@app.post("/upload")
async def makeASCII(file: bytes = File()):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"data":"file uploaded sucessfuly"}  
```

Files are uploaded through html forms and so our API needs to handle this type of data. The file variable just states that the incoming file is going to be the type `bytes`.

lets test out our endpoint by running the program with the unicorn command used previously. Now go to `http://127.0.0.1:8000/docs` to test out our code. Press the try out button and upload a file, if the output looks like this then the code works.

Now we know that the endpoint works, we can copy our code from earlier let's copy our `matchToASCII` and `convertToAscii` functions from `image_test.py` into `app.py`. 

Let's modify our `makeASCII` function so that it takes in a file, processes it and converts it to ASCII art. The function should now look like this:


```python
from PIL import Image
import io
import numpy as np


#Upload API endpoint 
@app.post("/upload")
async def makeASCII(file: bytes = File()):
    if not file:
        return {"message": "No file sent"}
    else:
        with Image.open(io.BytesIO(file)) as img:
            array = np.asarray(img)
            ascii = convertToAscii(array)
        return {"data":ascii} 
```

Our `app.py` should now look like:

``` python
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
```

When we run this code and go to `http://127.0.0.1:8000/docs` and try top upload an image and excute it we should see something interesting in the josn. The json data shoild look like the following:

![json output](Images/json.png)

Don't be alarmed ! The FastAPI docs output for API request show all the non printable characters such as `\n` (newline) and so our image will not show propery as text for testing but the text image is fine.

Now that's our ASCII art API!'
