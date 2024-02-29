# Functions are a block of coderunning together as a unit
# eg sum(10,20) 10 and 20 are the parameters of the function
# we first initialize the function

def print_name():
    print("My name is Austin Musango")


# calling the function
print_name()
print_name()
print_name()
print_name()

def print_details(name,age,id,gender):
    print("I am {0} , {1} years old , My id no is {2} , gender is {3}".format(name,age,id,gender))

print_details("Austin Musango","18","1234567890","male")

def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)

def prod_nums(n,k):
    return n * k

print(prod_nums(10,4))

def print_odds(first_no,last_number):
    for i in range(first_no,last_number):
        print(i%2)


print_odds(0,15)


#write a function t print all prime numbers between 1 and 99
# write a function to print all the squares and cubes of numbers betwwe 1 to 10
# write a function to calculate s.a of cone,cylinder and sphere
