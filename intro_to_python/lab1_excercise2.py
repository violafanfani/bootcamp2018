### WELCOME TO THE FIRST LAB ###

## Lists, Tuples and Dictionaries

"""
Examples 1 Lists and tuples
"""

singers=[("Amy","Winehouse"),("David","Bowie"),("Elton","John"),("Freddie","Mercury")]
names,surnames=zip(*singers)

print(names)
print(surnames)

# Add an element to the string

singers.append(("Adele",""))
print(singers)
singers.insert(1, ("Damon","Albarn"))
print(singers)
singers.remove(("Adele","0"))
print(singers)

#Slicing

sorted_surnames=sorted(surnames) # Surnames ordered alphabetically
print(sorted_surnames[0]) #First surname
print(sorted_surnames[-1]) #Last one
print(sorted_surnames[0:2]) #First 3 surnames

# Obtain only the entry for Elton John

ej=singers.index(("Elton","John"))
print(singers[ej])

"""
Examples 2: Lists of lists and slicing
"""

power2=[[1,1,1,1,1],[1,2,4,8,16],[1,3,9,27,81]]
# power of 1
print(power2[0])
# 2**3
print(power2[1][3])

"""
Examples 3: Sets
"""
# I tend to forget things and wrote two grocery lists for my today shopping

groceries1=["banana","pasta","kiwi","sauce","garlic"]
groceries2=["banana","apple","brussel sprouts","bacon","eggs"]

#how long are my grocery lists?
print(len(groceries1))
print(len(groceries2))

# Did I include something twice?

repeated=set(groceries1).intersect(set(groceries2))

#Final list

groceries=set(groceries1).union(set(groceries2))

groceries_set=set(groceries)
print(groceries)

groceries.update(["orange", "mango", "grapes","banana"])
print(groceries)

"""
Examples 4: Dictionaries
"""

university =	{
  "name": "University of Essex",
  "year": "1964",
  "number_of_students": 14585 
}

print(university["name"])

#Did I specify how many undergrads?

under=university.get("undergrads")

print(type(under))

# Let's add it 

university["Undergrads"]=11285
under=university.get("undergrads")
print(type(under))

## What can I add to a ditionary?
university["campus"]=["Colchester","Southend","Loughton"]
print(unviersity)
university["buildings"]={}
university["buildings"]["STEM"]=["Science","CSEE","Biology"]
university["buildings"]["SQUARE2"]=["CSEE","Maths","Biology","Carreer Hub"]

print(university["buildings"])

# How is the dictionary structure now?

print(university.keys())
print(university.items())
print(university.values())


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
