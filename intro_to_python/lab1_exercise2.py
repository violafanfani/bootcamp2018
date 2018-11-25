#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Viola Fanfani

### WELCOME TO THE FIRST LAB ####

"""

## Lists, Tuples and Dictionaries
#%%

"""
Examples 2: Lists and tuples
"""

#Fundamental operations with lists

list_a = [1,2,3,4,5]
list_a.append(6)
# ???:  What do you expect to find in list_a?
print(list_a)
# ???: Is it different from the following? 
list_range=range(1,7)

list_a.insert(0,20)
list_a.remove(5)
# ???:  What do you expect to find in list_a?
print(list_a)
#%%
#Operations with lists
list_b=list((0,10,100,1000))
print(list_a+list_b)
print(3*list_b)

# Slicing
print(list_b[0],list_b[2])
print(list_b[2:])
list_b[1]=0
print(list_b)

# !!!: Pay attention here!
list_c1=list_a
list_c2=list_a.copy()

list_a.extend(["a","b","c"])
# ???:  What are list_c1 and list_c2 now?

#%%
## Slightly more complicated lists
power2=[[1,1,1,1,1],[1,2,4,8,16],[1,3,9,27,81]]
# power of 1
print(power2[0])
# 2**3
print(power2[1][3])

#%%
"""
Lists and tuples
"""

singers=[("Amy","Winehouse"),("David","Bowie"),("Elton","John"),("Freddie","Mercury")]
names,surnames=zip(*singers)

print(names)
print(surnames)

# Add an element to the list

singers.append(("Adele",""))
print(singers)
singers.insert(1, ("Damon","Albarn"))
print(singers)
singers.remove(("Adele",""))
# ???: How many singers are now in the list?
#%%
#Slicing

sorted_surnames=sorted(surnames) # Surnames ordered alphabetically
print(sorted_surnames[0]) #First surname
print(sorted_surnames[-1]) #Last one
print(sorted_surnames[0:2]) #First 3 surnames

# Obtain only the entry for Elton John
ej=singers.index(("Elton","John"))
print(singers[ej])
#%%
"""
Examples 3: Sets
"""
# I tend to forget things and wrote two grocery lists for my today shopping

groceries1=["banana","pasta","kiwi","sauce","garlic"]
groceries2=["banana","apple","brussel sprouts","bacon","eggs"]

#how long are my grocery lists?
print(len(groceries1))
print(len(groceries2))

# ???:  Did I include something twice?
repeated=set(groceries1).intersection(set(groceries2))

#Final list
groceries=set(groceries1).union(set(groceries2))

groceries_list=list(groceries)
print(groceries)

groceries.update(["orange", "mango", "grapes","banana"])
# ???: How many elements are in groceries now?


#%%
"""
Examples 4: Dictionaries
"""

university =	{
  "name": "University of Essex",
  "year": "1964",
  "number_of_students": 14585 
}

print(university["name"])

# ???: Did I specify how many undergrads?
under=university.get("undergrads")
print(type(under))

# Let's add it 
university["Undergrads"]=11285
under=university.get("Undergrads")
print(type(under))

#%%
## What can I add to a dictionary?
university["campus"]=["Colchester","Southend","Loughton"]
print(university)
university["buildings"]={}
university["buildings"]["STEM"]=["Science","CSEE","Biology"]
university["buildings"]["SQUARE2"]=["CSEE","Maths","Biology","Carreer Hub"]

print(university["buildings"])
#%%
# How is the dictionary structure now?

print(university.keys())
print(university.items())
print(university.values())

#%%
# !!! Let's save this dictionary, we are going to use it later

import pickle #This commands are usually added at the beginning of the code

with open("university.pickle","wb") as f:
    pickle.dump(university,f)
    
# And now we read it again

with open("university.pickle","rb") as f:
    university_dictionary=pickle.load(f)

#%%
"""
TODO: Exercise 1 

Let's create a calendar! Something Like:

January: [(1,"monday")] : "play piano",
	[(2,"tuesday")] : "volley" ...

HINT: lookup "dict.fromkeys()" 

"""




