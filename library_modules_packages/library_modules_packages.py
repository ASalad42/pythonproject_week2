# python library, modules, and packages
# syntax - key words

#how to use them
from random import random # from package
#import random module
#print(random()) #generates a random number everytime you run a program

import math

num_float = 23.66

#user requirement was to round the figure
# if amount was .50 or above round up
# if amount was .49 or less round down
#print(math.ceil(num_float))
#print(math.floor(num_float))

# check pypy docu - libray section

#print(math.pi) # already in library

## Modules - help us communicate with our OS

import os
import math, datetime, sys

# find out the current location - REALLY USEFUL
workin_dir = os.getcwd() # location of current working direct
#print(workin_dir)
#print(datetime.datetime.now()) # current date and time now

#print(os.cpu_count()) # how many cores my machine has
#print(sys.path) # absolute path

# what to do in other file/system - step 3 basically
#import os_info
#print(os_info.operating_systme_information())
# from filename import package (os_info)
# how to bring into other files
# step 2
class Os_Info: # can now import this class into other files
    @staticmethod
    #step 1
    def operating_systme_information(): # now we can make function to find cpu info out from available packages and libraries
        print(os.cpu_count())
Os_Info.operating_systme_information()

# print(os.uname()) # only works for mac and linux - so always check libaraies/packages compatibility
# if os windows dont run - developer hat on

#re usable 5hr32mins on teams recording
# step 1 - insert into function
# step 2 - insert that function into a class
# step 3 - class only avaible in one file > import into other file i.e import 0s_Info

# for functions create new files - new python file next to my old tasks
# procedural code > functions > class (so its available globally)
# refactor code using OOP (reduce line of code from 2000 by like 70%)