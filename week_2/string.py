# strings in ython
# Date : 15/02/2024
# Name : Austin Musango

city = "nairobi"

print(city[0]) #n
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[-1])
print(city[-2])


# convert to upper case


print(city)
print("\n") #prints a new line
print(city.upper())

name = "AUSTIN"
print(name)
print(name.lower()) # converts to lower case

town = "      Naivasha"

print(town)
print("\t") # new tab
print(town.strip())

# add two strings

f_name = "Austin"
s_name = "Musango"

full_name = f_name + s_name

print(full_name)
# write a program to reverse a string
# write a program that checks if astring is a palindrom


#replacing a character

fruit = "orange"

print(fruit.replace("o","y"))

subject = "physical,sciences"

print(subject.split(":"))

age = 30
height = 2.9
print("i am  {0} years old and {1} meters tall" .format (age,height))

activity = "dancing"
print("My hobby is &s" %(activity))

# printing a float

height = 1.2334909
print("My height is  %5.3f"% (height))

# printing an integer
age = 32
print("my age is %d" %(height))



name = "AUSTIN"
print(len(name))

print(f"My full name is {name}")

course= "Electrical"
school="Engeneering"
print("I am studying {0} in the school of {1}".format(course="medicine",school="Agakhan"))