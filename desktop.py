from PIL import Image
import ctypes
from pathlib import Path
import time


i = 0;
while i < 10:

	ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\Certa\\Documents\\PythonStuff\\image2.jpg" , 0)

	time.sleep(10)

	ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\Certa\\Documents\\PythonStuff\\image.jpg" , 0)

	time.sleep(10)
	i+=1;
	print(i)
