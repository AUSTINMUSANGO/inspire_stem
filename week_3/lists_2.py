friends = ["ryan","hildad","victor","ronn","peter"]

for friend in friends:
    print(friend)


    enemies = friends[:] # to copy one list to another
    print(enemies)

    fruits = ["guava","mango","apple","strawberry","orange","blueberry"]

    # slice the list

    print(fruits[0:3])

    del fruits[0]

    print(fruits)

    squares = [] # initializes an empty list

for x in range(0,11):
    squares.append(x**2)

    print(squares)

    