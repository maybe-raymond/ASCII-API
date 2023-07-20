# ASCII Art API in FastAPI

## Introduction
In this tutorial, you will learn how to create an ASCII art API that can convert both text and images to ASCII. You will start by learning what an image file really is, and then you will build an API that will generate ASCII ART for you given the required image or text. By the end of this tutorial, you will have a working API that you can use to create ASCII art from any image or text.

### Requirements
To create this API, we'll need:
* [Python](https://www.python.org/) 3.6+ installed
* [Git](https://git-scm.com/)

### Setting Up Our Environment
We will create a virtual Python environment using Venv. Firstly, lets create a local directory. This directory will be called ASCII Art, then you should open the terminal in this directory. To create the Virtual Environment enter the command:

```
python -m venv env
```
__note__ : Depending on how you set up your Enviroment variables when you installed python the above command might not work. If the above command does not work switch the `python` part with `python`.  If this change fails then plaese go to this [link](https://docs.python.org/3/library/venv.html) or [this one](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) for extra information

To activate the virtual environment using the following command for your operating system

* **Linux/MacOSX:**  
```
source env/bin/activate
```

* **Windows:**  
```
source env\Scripts\activate.bat
```

if the virual environment activated correctly, you should see (env) to the left of your name in the terminal. It should look something like this:

![terminal](Env.png)

### Installing Dependencies
Now that we've got our virtual environment set up, we can look at the packages we're gonna use:

* [FastAPI](https://fastapi.tiangolo.com/) is a web development framework that provides tools that make it easy for building, documenting and maintaining APIS
* [NumPy](https://numpy.org/) is a library used for scientific computing which will come in handy manipulating images.
* [unicorn](https://pypi.org/project/unicorn/) is a server that will help serve our API 

```
pip install numpy
pip install fastapi
pip install "uvicorn[standard]"
```

__note__ : if pip does not work you can try `pip3` instead.

## What really is a digitial image ?
Computers interpert visual images in formats such as `.png, jpeg and webp` as a two dimensinal(2d) array or a matrix. Some image formats represent images as three arrays were the value of the inner array is another array of RGB vaules. The best way to understand all this is by doing and us visually seeing 

