import zmq
import traceback
import json
import time
import sys
from PIL import Image
import numpy as np
import colormath

import collections
import functools

############## CONFIGURATION

# filename of the target image
filename = 'mondrian.png'

############################

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)
print("Bound at port {}".format(port))

target_image = Image.open(filename)
target_pixels = np.asarray(target_image)
# segments = get_superpixels(filename)

def log_likelihood(rectangle):
    difference = 0
    (x, y, width, height, rgb) = rectangle
    guess_pixels = np.zeros((height, width, 3))
    guess_pixels[:,:,:] = rgb
    # used to include black borders of rectangles like a real mondrian
    # guess_pixels[0,:,:] = [0, 0, 0]
    # guess_pixels[-1,:,:] = [0, 0, 0]
    # guess_pixels[:,-1,:] = [0, 0, 0]
    # guess_pixels[:,0,:] = [0, 0, 0]
    image_section = target_pixels[y:y+height, x:x+width, :3]

    return np.sum(-((image_section - guess_pixels)**2))

while True:
   #  Wait for next request from client
   message = json.loads(socket.recv().decode("utf-8"))
   try:
       total = 0
       for rectangle in message:
           total += log_likelihood(rectangle)
       # print(total)
       socket.send_string(str(total))
   except Exception as e:
       print("Something went wrong.")
       print(e)
       traceback.print_exc()
       socket.send_string("EVERYTHING IS WRONG AND BAD")
