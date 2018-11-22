#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Viola Fanfani

### WELCOME TO THE FIRST LAB ####

"""
import pickle

## 
#%%

"""
Functions
"""

def square(x):
    return x**2

print(square(10))
print(square(2))

#%%

def cut_list(list_in,start,stop,both=False):
    
    if both:
        return list_in[start:stop]
    else:
        return list_in[start:]


with open("recordings.pickle","rb") as f:
    data=pickle.load(f)

# !!!: functions make your code cleaner, more compact, reusable!
first_10_samples=[]
for i in data:
    if i[0]=="Morgan":
        first_10_samples.append(cut_list(i[1],0,10,both=True))

print(first_10_samples)
print(list_in)   
# ???: why do I get an error here?        
        
#%%
"""
TODO: Exercise 1

Exercise 1
write fun_exercise_1
The function takes in input a number x and a list of numbers y, and returns a value as 
follows:
•If x is odd, fun_exercise_1 subtract 1 from all the elements of y and then returns its sum. 
•If x is even, fun_exercise_1 multiplies each element of yby 2 and then returns its sum. 
•If x is zero, fun_exercise_1 returns the sum of all the elements in y
"""


#%%
"""
TODO: Exercise 2
Solve again the previous script, but now write different functions to obtain each information

A machinery for voice recordings has saved a pickle containing the output data recorded.
Load the "recordings" data, look at what it contains
and create a dictionary with the following informations:
    - How is the list structured?
    - How many recordings has the machinery taken?
    - How many subjects have been recorded?
    - How many saples from Kelly are there?
    - For each recording and for each subject, count the number of positive samples
    - For each recording, save the location of the first value that is between -0.001 and 0.001

now load the recordings_2 file and try to do the same, isn't it easier?
"""

