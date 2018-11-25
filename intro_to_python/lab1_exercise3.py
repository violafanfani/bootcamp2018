#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Viola Fanfani

### WELCOME TO THE FIRST LAB ####

"""

import pickle

## COnditional statements and loops
#%%

"""
Examples 2: If ..., elif ..., else ...
"""

# !!!: Boolean values and conditional statements
a=[1,2,3,12]
print(a[0] == 1)
print(a[0] != 1)
print(len(a) >= 10)
print( 12 in a )

#%%

if (12 in a):
    print("a contains number 12")
else:
    print("number 12 not found in list a")

#%%

if len(a)>10:
    print("long list")
elif len(a)<5:
    print("short list")
else:
    print("list is between 5 and 10 elements")


#%%
"""
While Loops
"""

list_a=["Norman","John","Laura","Michelle"]

while len(list_a)>0:
    print(list_a)
    list_a.pop()


sequence=[1, 1.2, 1.5, 2, 3.5, 2.1, 5,2.8, 3.9, 3, 3.7, 5]

count=0
while sequence[count]<5:
    count+=1

# ???: what do you expect count to be?
print(count)

#%%
"""
For Loops
"""
list_for=[]
for i in range(10):
    list_for.append(i)

print(list_for)

list_name=["Norman","John","Laura","Michelle","John"]
list_surname=["Foster","F. Kennedy","Linney","Obama","Oliver"]
list_notorious=zip(list_name,list_surname)

Johns=[]
for name in list_notorious:
    if name[0] == "John":
        Johns.append(name)
print(Johns)

# !!! you can use indices as well

idx=0
Johns2=[]
for name in list_name:
    if name == "John":
        Johns2.append(list_surname[idx])
    idx+=1
print(Johns2)

#%% Lists Comprehension

list_double=[]
for i in range(10):
    list_double.append(2*i)
    
# !!!: you can perform the same operation inline
    
list_double2=[2*i for i in range(10)]
    
#%% for loops can iterate over every "iterable" type

with open("university.pickle","rb") as f:
    university=pickle.load(f)
    
buildings=[]
for key,item in university.items():
    print(key,item)
    if key=="buildings":
        for key_b in item.keys():
            buildings.append(key_b)

# ???: What do you expect to find in buildings?
print(buildings)
#%%
"""
TODO: Exercise 1
A machinery for voice recordings has saved a pickle containing the output data recorded.
Load the "recordings" data, look at what it contains
and create a dictionary with the following informations:
    - How is the list structured?
    - How many recordings has the machinery taken?
    - How many subjects have been recorded?
    - How many saples from Kelly are there?
    - For each recording and for each subject, count the number of positive samples
    - For each recording, save the location of the first value that is between -0.001 and 0.001
"""




