
number=[]

number.append(10)
number.append(20)
number.append(30)

number.insert(1,15)

number.pop()

print(number)


def greetings():
    print("გამარჯობა, როგორ ხარ?")

numbers = []


numbers.append(10)
numbers.append(20)
numbers.append(30)


numbers.insert(1, 15)


numbers.pop()


print(numbers)


def repeat_word(count, word):
    for _ in range(count):
        print(word)


from turtle import *

def draw_square(x, y):
    penup()
    goto(x, y)
    pendown()
    for _ in range(4):
        forward(100)
        right(90)

draw_square(0, 0)
done()
