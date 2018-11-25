#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Viola Fanfani

### WELCOME TO THE FIRST LAB ####

"""
## Data Types
#%%
"""
Examples 1: a few operations with numbers and strings
"""

# A school has 3 classrooms, each of them can contain 20 students.
# How many students can be enrolled in the school?

n_classrooms=3  # What data type is n_classrooms?
print(type(n_classrooms))

room_seats=20
max_total_students=3*20  # How many? 
print("Max number of students: %d" %max_total_students)
#%%
# At the beginning of the year there are 56 students enrolled.
# How many other application can the school accept?
enrolled=56
remaining=max_total_students - enrolled

# How many students in each class?
integer_division=enrolled // n_classrooms
remainder=enrolled % n_classrooms
print("Each class is going to have %d students and %d of them are remaining to assign to a class" %(integer_division,remainder))
#%%
# The first application is from 
app="Juana Martinez, born in Madrid, on the 16/05/2000"
# What are her name, birth place and DOB?
full_name=app.split(",")[0]
birth_place=app.split(",")[1].split(" ")[3]
DOB=app.split(",")[2].strip()[7:]

print(full_name,birth_place,DOB)
#%%
"""
Exercise 1
Martin Jones just arrived at the hospital and someone has collected his data as below.
You are required to extract the following information:
- name of the patient
- family name of the patient
- his year of birth
- his BMI (calculated as weight^2[kg]/height[cm])

"""
fill_name_patient="Martin Jones"
age_patient=25
today_date="05/11/2018"
weight_patient=90.8
height_patient=180