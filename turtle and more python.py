#triangle
import turtle
melinda = turtle.Turtle()
melinda.color("gray")
melinda.forward(100)
melinda.left(120)
melinda.forward(100)
melinda.left(120)
melinda.forward(100)


import turtle
amy = turtle.Turtle()
amy.color("yellow")

amy.width(2)
amy.speed(0)
amy.forward(100)
amy.right(90)
amy.penup()
amy.forward(100)
amy.right(90)
amy.pendown()
amy.forward(100)
amy.right(90)
amy.forward(100)


#hexagon
import turtle
manas=turtle.Turtle()
manas.color("yellow")
manas.forward(120)
manas.right(60)
manas.forward(120)
manas.right(60)
manas.forward(120)
manas.right(60)
manas.forward(120)
manas.right(60)
manas.forward(120)
manas.right(60)
manas.forward(120)

# four (royg) coloured square
import turtle
amy = turtle.Turtle()

amy.color("red")
amy.forward(100)
amy.right(90)
amy.color("orange")
amy.forward(100)
amy.right(90)
amy.color("yellow")
amy.forward(100)
amy.right(90)
amy.color("green")
amy.forward(100)



#using variables
import turtle
mary=turtle.Turtle()
bangani="purple"
mary.color(bangani)
for side in [1,2,3,4,5]:
    mary.forward(100)
    mary.right(72)



import Turtle
mary=turtle.Turtle()
color="purple"
sides=[1,2,3,4,5]
distance=100
angle=72
mary.color(color)
for side in sides:
    mary.forward(distance)
    mary.right(angle)



#triangle using for loop
import turtle
juno = turtle.Turtle()
juno.color("white")
for side in [1,2,3]:
  juno.forward(100)
  juno.left(120)



#assigning lists to variable
import turtle
amy = turtle.Turtle()
amy.color("cyan")
some_list=[1,2,3,4,5,6,7,8,9,10,11,12]

for item in some_list:
    amy.forward(50)
    amy.right(30)


#designs square shaped spiral
import turtle

lengths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

dizzy = turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for length in lengths:
    dizzy.forward(length)
    dizzy.right(90)
# here length represents as a variable
#in the 7th lne length shows repeating the numbers above in a loop like 10
# then 20 and so on.



#making chain of hexagons
import turtle

links = [1, 2, 3, 4, 5, 6, 7, 8]
sides = [1, 2, 3, 4, 5, 6]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(80)
weaver.pendown()

for link in links:
    # Draw a hexagon.
    for side in sides:
        weaver.forward(10)
        weaver.right(60)

    # Scoot over to the next link.
    weaver.penup()
    weaver.forward(20)
    weaver.pendown()

weaver.hideturtle()


#practicing
import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three red lines, with space in between
amy.color("red")

amy.forward(50)
amy.penup()
amy.forward(50)
amy.pendown()

amy.forward(50)
amy.penup()
amy.forward(50)
amy.pendown()

amy.forward(50)
amy.penup()
amy.forward(50)
amy.pendown()




#drawing sqares with different colors
import turtle

amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
    amy.color(prettycolor)
    for side in [1, 2, 3, 4]:
        amy.forward(50)
        amy.right(90)
    amy.penup()
    amy.forward(100)
    amy.pendown()



#drawing a hexagon with rainbow colours
import turtle
riya=turtle.Turtle()
rainbow=["red", "orange", "yellow", "green", "blue", "purple"]

riya.width(5)
riya.penup()
riya.back(50)
riya.pendown()

for pretty_color in rainbow:
    riya.color(pretty_color)
    riya.forward(100)
    riya.right(60)
riya.hideturtle()



#drawing rainbow stars
import turtle
stars=turtle.Turtle()
rainbow=["red", "orange", "yellow", "green", "blue", "purple"]

stars.width(5)
stars.speed(0)
for color in rainbow:
    stars.color(color)
    for side in [1, 2, 3, 4, 5]:
        stars.forward(50)
        stars.right(144)
    stars.right(60)
    stars.penup()
    stars.forward(50)
    stars.pendown()
stars.hideturtle()




#range
import turtle
sides = range(100)

t = turtle.Turtle()
t.color("magenta")
t.width(5)

for side in sides:
    t.forward(5)
    t.right(360 / 100)



#spirangle
import turtle
t = turtle.Turtle()
t.color("cyan")

for side in range(19):
    t.forward(side*10)
    t.right(120)



#division
import turtle

# Set the number of sides here.
sides = 5

# Set the length of a side here.
length = 90

t = turtle.Turtle()
t.color("orange")
for side in range(sides):
    t.forward(length)
    t.right(360/sides)


#creating own function
#by usinf def
import turtle

def spirals():

    t = turtle.Turtle()
    t.color("cyan")
    for n in range(100):
        t.forward(n)
        t.right(20)

spirals()


#using parameters
import turtle
jack = turtle.Turtle()



def draw_shape(length,color,sides):
    jack.color(color)
    for side in range (sides):
        jack.speed(0)
        jack.forward(length)
        jack.right(360/sides)



for square in range(80):
    draw_shape(100,"cyan",10)
    jack.forward(5)
    jack.left(5)
    jack.speed(0)


#more examples
import Turtle
# Write a function here that creates a
# turtle and draws a shape with it.
jack=turtle.Turtle()

def triangle_colorfull (color,length):
    jack.color(color)
    for side in range(3):
        jack.speed(0)
        jack.forward(length)
        jack.right(360/3)
    jack.hideturtle()

# Call the function multiple times.
for triangle in range(80):
    triangle_colorfull("cyan",100)
    jack.forward(5)
    jack.left(5)
    jack.speed(0)
    triangle_colorfull("orange",120)
    jack.forward(5)
    jack.left(5)
    jack.speed(0)
    triangle_colorfull("red",140)
    jack.forward(5)
    jack.left(5)
    jack.speed(0)



import turtle

# Write a function here that creates a
# turtle and draws a shape with it.
def triangle_boogie(color, start):
  t = turtle.Turtle()
  t.color(color)
  t.speed(0)
  t.width(5)
  t.right(start)
  for shape in range(6):
    for side in range(3):
      t.forward(100)
      t.right(120)
    t.right(15)
  t.hideturtle()

# Call the function multiple times.
triangle_boogie("red", 0)
triangle_boogie("orange", 120)
triangle_boogie("blue", 240)



#balloons
import turtle

# This code doesn't work!
# The indentation is broken.
# Fix it!
def balloon(t, color):
    t.speed(0)
    t.color(color)

    # Draw balloon body.
    for side in range(30):
        t.forward(10)
        t.left(12)

    # Draw balloon knot.
    t.right(60)
    for side in range(3):
        t.forward(10)
        t.right(120)

    # Draw balloon string.
    t.color("gray")
    t.right(30)
    t.forward(100)


t = turtle.Turtle()

t.penup()
t.back(100)
t.pendown()
balloon(t, "red")

t.penup()
t.home()
t.pendown()
balloon(t, "blue")

t.penup()
t.home()
t.forward(100)
t.pendown()
balloon(t, "purple")

t.hideturtle()




#creting multiple turtles
import turtle
romeo=turtle.Turtle()
juliet=turtle.Turtle()


romeo.color("red")
romeo.width(5)

juliet.color("white")
juliet.width(5)



romeo.forward(150)
romeo.right(90)
romeo.forward(100)


juliet.forward(100)
juliet.right(90)
juliet.forward(100)



#assigning different names to the same turtle
import turtle
romeo = turtle.Turtle()
montague = romeo

montague.color("red")
montague.width(5)

montague.forward(100)
montague.right(90)
montague.forward(100)
montague.right(90)
romeo.color("white")
montague.forward(100)
montague.right(90)
montague.forward(100)
montague.right(90)


#creating petals
import turtle

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

romeo = turtle.Turtle()
romeo.color("violet")
romeo.speed(8)
for petal in range(6):
    draw_square(romeo)
    romeo.right(60)

romeo.hideturtle()



#creating petals with 2 turtles
import turtle

romeo = turtle.Turtle()
romeo.color("violet")
romeo.width(5)
romeo.speed(8)

juliet = turtle.Turtle()
juliet.color("misty rose")
juliet.speed(8)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_flower(some_turtle):
    for petal in range(6):
        draw_square(some_turtle)
        some_turtle.right(60)
    some_turtle.hideturtle()

draw_flower(romeo)
draw_flower(juliet)



#drawing shapes using if loops and for loops
import turtle

romeo = turtle.Turtle()
juliet = turtle.Turtle()

juliet.color("misty rose")
juliet.width(3)

romeo.color("violet")
romeo.width(3)

romeo_last_name = "montague"

romeo.left(40)
romeo.forward(100)
for side in range(185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()

if romeo_last_name == "montague":
    juliet.left(140)
    juliet.forward(100)
    for side in range(185):
        juliet.forward(1)
        juliet.right(1)
    juliet.hideturtle()


#practice
import turtle
jack = turtle.Turtle()
jack.width(5)

jack.color("yellow")
for side in range(4):
    if side==1:
        jack.color("blue")
    if side==2:
        jack.color("yellow")
    jack.forward(100)
    jack.right(90)



import turtle
jack = turtle.Turtle()
jack.width(5)

jack.color("yellow")
for side in range(4):
    if side==2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)



#use of if else statement in turtle
import turtle
jack = turtle.Turtle()
jack.width(5)


for side in range(4):
    if side == 1:
        jack.color("blue")
    else:
        jack.color("yellow")
    jack.forward(100)
    jack.right(90)



import turtle

def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.penup()
t.back(200)
t.pendown()

for n in range(10):
    if n%2 == 0:
        t.color("blue")
    else:
        t.color("red")
    bead(t)
    t.forward(40)


#creating dodecagon shape using multiple if's to create is colourful
import turtle

t = turtle.Turtle()
t.width(5)
t.speed(0)

for n in range(12):
    t.color("gray")
    if n % 3==0:
        t.color("red")
    if n % 3==1:
        t.color("orange")
    if n % 3 ==2:
        t.color("yellow")
    t.forward(50)
    t.right(360/12)
    t.hideturtle()



import turtle
t = turtle.Turtle()
t.color("white")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return (number*number)

for n in range(540):
    angle = square(n)
    t.right(angle + .5)
    t.forward(5)




import turtle

def super_reptile():
    t=turtle.Turtle()
    t.width(3)
    t.color("lightblue")
    return t

clark =super_reptile()
clark.forward(100)
clark.left(45)
clark.forward(100)




import turtle

def bead_color(num):
    if num % 3 == 0:
        return "red"
    if num % 3 == 1:
        return "green"
    else:
        return "blue"

def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)

t = turtle.Turtle()
t.speed(0)
t.width(2)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

# Draw ten beads.
for n in range(10):
    t.color(bead_color(n))
    bead(t)
    t.forward(40)




import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(5)  # visible!
    galileo.speed(8)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star

for angle in [180, 135, 90, 45, 0]:
    star("red", 5, 50, angle, 100)

for angle in [180, 135, 90, 45, 0]:
    star("blue", 5, 30, angle, 60)



import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(5)  # visible!
    galileo.speed(0)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star

for angle in [315, 270, 225, 180, 135, 90, 45, 0]:
    star("violet", 5, 50, angle, 100)

for angle in [315, 270, 225, 180, 135, 90, 45, 0]:
    star("white", 5, 30, angle, 60)




import turtle

def polygon(sides, length):
  t = turtle.Turtle()
  t.color("lime")
  t.speed(0)
  angle = 360 / sides
  for side in range(sides):
    t.forward(length)
    t.right(angle)
  t.hideturtle()


for sides in [3,4,5,6,7,8,9,10,11,12,13,14]:
    polygon(sides, 35)


import turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t = turtle.Turtle()
t.width(20)

for step in range(100):
    # Change this to use a random number.
    angle =random.randint(-90, 90)

    # Change this to use a random color.
    color = random.choice(colors)

    t.color(color)
    t.right(angle)
    t.forward(10)



import turtle

def temperature_color(temp):
    # Change this code!
    if temp < 20:
        return "blue"
    if temp < 50:
        return "purple"
    if temp >= 50:
        return "red"
    return "green"

def draw_temperature(temp):
    t = turtle.Turtle()
    t.penup()
    t.back(100)
    t.width(20)
    t.pendown()
    for n in range(temp):
        t.color(temperature_color(n))
        t.forward(1)

def draw_therm_box():
    t = turtle.Turtle()
    t.speed(0)
    t.color("gray")
    t.penup()
    t.back(120)
    t.pendown()
    t.left(90)
    for side in [20, 240, 40, 240, 20]:
        t.forward(side)
        t.right(90)
    t.hideturtle()

draw_therm_box()
draw_temperature(120)


import turtle
t = turtle.Turtle()
t.width(100)

coins = 1000
rich = coins >= 1000

if rich:
    t.color("gold")
else:
    t.color("silver")

t.forward(0)



import random
import turtle
riley = turtle.Turtle()
riley.width(5)
mood=random.choice(["happy", "sad", "angry", "chill"])
if mood == "happy":
   riley.color("yellow")
elif mood == "sad":
    riley.color("blue")
elif mood == "angry":
    riley.color("red")
elif mood == "chill":
    riley.color("pink")
else:
    riley.color("gray")
# Add your code here.

for side in range(5):
    riley.forward(100)
    riley.right(144)



import turtle

t = turtle.Turtle()
t.color("lime")
t.width(3)
t.penup()
t.shape("turtle")

for step in range(2000):
    t.forward(1)
    if t.xcor() < -170 or t.xcor() > 170:
       t.right(180)



import turtle
import random

def draw_box(length):
    tur = turtle.Turtle()
    tur.speed(0)
    tur.color("gray")
    tur.penup()
    tur.back(length/2)
    tur.left(90)
    tur.forward(length/2)
    tur.right(90)
    tur.pendown()
    for side in range(4):
        tur.forward(length)
        tur.right(90)
    tur.hideturtle()

draw_box(200)

t = turtle.Turtle()
t.shape("turtle")
t.color("olive")
t.penup()
t.speed(1)

for e in range(2000):
    t.right(random.randint(-10, 10))
    t.forward(10)
    out_of_bounds = t.xcor() < -80 or t.xcor() > 80 or t.ycor() < -80 or t.ycor() > 80
    if out_of_bounds:
        t.right(180)
        t.forward(10)



message = input("What do you have to say, hm?\n")

for ch in message:
    if ch == "?":
        print("Sense much curiosity in you, I do.")
    if ch == "!":
        print("Enthusiastic, you are.")


count = 0

for ch in "bonobos":
    if ch == "o":
        count = count + 1

print(count)



def count_character(string, target):
    count = 0
    for ch in string:
        if ch == target:
            count = count + 1
    return count



def start_K(s):
    if s[0] == "K":
        return True
    else:
        return False



def word_triangle(word):
  length = len(word)
  for n in range(length):
    print(word[:length - n])



def adverbly(s):
    return s + 'ly'


name = input("What's your name?\n\n")
print("\nHi, " + name + "! It's very nice to meet you.\n")
color = input("What's your favorite color?\n\n")
print("\nAh, " + color + ", what a lovely color!")



name = input("What's your name?\n\n")
print(f"\nHi, {name}! It's very nice to meet you.\n")
color = input("What's your favorite color?\n\n")
print(f"\nAh, {color}, what a lovely color!")



n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
n3 = input("Enter a third number: ")
sum = int(n1) + int(n2) + int(n3)
print(f"{n1} + {n2} + {n3} = {sum}")


n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
n3 = input("Enter a third number: ")
sum = int(n1) + int(n2) + int(n3)
print(n1 + ' + ' + n2 + ' + ' + n3 + ' = ' + str(sum)



def starts_with(long, short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True



def good_length(s):
    return len(s) > 8 and len(s) < 64


def total_length(list_of_strings):
    total = 0
    for string in list_of_strings:
        total = total + len(string)
    return total


n = 10
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print("Blastoff!")



n = 10
while n > 0:
    print(n)
    n -= 1
print("Blastoff!")



s = "abracadabra"
index = len(s)
while index > 0:
    print(s[:index])
    index -= 1


index = 0
while index < len(word):
    print(word[index])
    index += 1

def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total


def until_dot(s):
    index = 0
    while index < len(s) and s[index] != '.':
        # No dots yet, keep going.
        index += 1
    # We either found a dot or ran out of string.
    return s[:index]


def until_dot(s):
    for index in range(len(s)):
        if s[index] == '.':
            # A dot! Return everything up to here.
            return s[:index]
    # We ran out of string without seeing any dots.
    # Return the whole string.
    return s


def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False


def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
        index += 1
    return total


def locate_first(string, sub):
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            return index
        else:
            index += 1
    return -1


>>> locate_all('cookbook', 'ook')
[1, 5]
>>> locate_all('yesyesyes', 'yes')
[0, 3, 6]
>>> locate_all('the upside down', 'barb')
[]



 def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches



def breakify(strings):
    return "<br>".join(strings)


def remove_substring(string, substring):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replacement)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


import random
import words


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    while index < len(template):
        if template[index:index+8] == '{{noun}}':
            # Add a random noun to the output.
            output.append(random.choice(nouns))
            index += 8
        elif template[index:index+8] == '{{verb}}':
            # Add a random verb to the output.
            output.append(random.choice(verbs))
            index += 8
        else:
            # Copy a character to the output.
            output.append(template[index])
            index += 1

    # Join the output into a single string.
    output = ''.join(output)

    return output


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))



while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Waffles it is!")
        break
    elif "pancakes" in response:
        print("Pancakes it is!")
        break
    else:
        print("Sorry, I don't understand.")




print("Hello! I am Bob, the Breakfast Bot.") # All of these are outside the loop.
print("Today we have two breakfasts available.")
print("The first is waffles with strawberries and whipped cream.")
print("The second is sweet potato pancakes with butter and syrup.")
while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Waffles it is!")
        break
    elif "pancakes" in response:
        print("Pancakes it is!")
        break
    else:
        print("Sorry, I don't understand.")
print("Your order will be ready shortly.") # This one is also outside the loop!



print("Hello! I am Bob, the Breakfast Bot.") # All of these are outside the loop.
print("Today we have two breakfasts available.")
print("The first is waffles with strawberries and whipped cream.")
print("The second is sweet potato pancakes with butter and syrup.")
while True:
    response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Waffles it is!")
        break
    elif "pancakes" in response:
        print("Pancakes it is!")
        break
    else:
        print("Sorry, I don't understand.")
print("Your order will be ready shortly.") # This one is also outside the loop!





import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(2)
print("Today we have two breakfasts available.")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(2)

while True:
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(2)
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    print("Your order will be ready shortly.")
    time.sleep(2)
    while True: # We want to loop until they enter a valid response.
        order_again = input("Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
        if 'no' in order_again:
            print("OK, goodbye!")
            time.sleep(2)
            break # Note that this will only break out of the inner loop.
        elif 'yes' in order_again:
            print("Very good, I'm happy to take another order.")
            time.sleep(2)
            break # Again, this only breaks out of the inner loop.
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    if 'no' in order_again:
        break # We need this last break statement to exit the outer loop.



import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")


while True:
    while True:
        response = input("Please place your order.  Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print_pause("Waffles it is!")
            break
        elif "pancakes" in response:
            print_pause("Pancakes it is!")
            break
        else:
            print_pause("Sorry, I don't understand.")
    print_pause("Your order will be ready shortly.")
    while True:
        order_again = input("Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
        if "no" in order_again:
            print_pause("OK, goodbye!")
            break
        elif "yes" in order_again:
            print_pause("Very good, I'm happy to take another order.")
            break
        else:
            print_pause("Sorry, I don't understand.")
    if "no" in order_again:
        break




import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response
        else:
            print_pause("Sorry, I don't understand.")


print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")


while True:

    response = valid_input("Please place your order. "
                           "Would you like waffles or pancakes?\n",
                           "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")

    print_pause("Your order will be ready shortly.")

    order_again = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in order_again:
        print_pause("OK, goodbye!")
    elif "yes" in order_again:
        print_pause("Very good, I'm happy to take another order.")



def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("Sorry, I don't understand.")



import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def get_order():
    response = valid_input("Please place your order. "
                           "Would you like waffles or pancakes?\n",
                           "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")

intro()
while True:

    get_order()
    print_pause("Your order will be ready shortly.")
    order_again = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in order_again:
        print_pause("OK, goodbye!")
        break
    elif "yes" in order_again:
        print_pause("Very good, I'm happy to take another order.")


def order_again():
    response = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
        break
    elif "yes" in response:
        print_pause("Very good, I'm happy to take another order.")

intro()
while True:
    get_order()
    order_again()



import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def get_order():
    response = valid_input("Please place your order. "
                           "Would you like waffles or pancakes?\n",
                           "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")


def order_again():
    response = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()


intro()
get_order()
order_again()


import time



def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def get_order():
    response = valid_input("Please place your order. "
                           "Would you like waffles or pancakes?\n",
                           "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")


def order_again():
    response = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()



  def order_breakfast():
      intro()
      get_order()
      order_again()

order_breakfast()


def guess_color():
    response = input("Can you guess what my favorite color is?\n")
    if response == 'blue':
        print("That's right! My favorite color is blue.")
    else:
        print("Sorry, that's not my favorite color. Try again!")
        guess_color()

guess_color()


def green_room():
    print("You are in the green room.")
    choose_room()

def blue_room():
    print("You are in the blue room.")
    choose_room()

def choose_room():
    choice = input("Would you like to go to the green room or the blue room?\n")
    if choice == 'green':
        green_room()
    elif choice == 'blue':
        blue_room()
    else:
        print("I don't know what that is.")
        choose_room()

choose_room()




import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find "
                    "yourself in the lobby.")
    elif floor == '2':
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself "
                    "in the human resources department.")
    elif floor == '3':
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself "
                    "in the engineering department.")

    print_pause("Where would you like to go next?")




import time
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find "
                    "yourself in the lobby.")
        if "ID card" in items:
            print_sleep("The clerk greets you, but she has already "
                        "given you your ID card, so there is nothing "
                        "more to do here now.")
        else:
            print_sleep("The clerk greets you and gives you your ID "
                        "card.")
            items.append("ID card")
    elif floor == '2':
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself "
                    "in the human resources department.")
    elif floor == '3':
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself "
                    "in the engineering department.")
        print_pause("Where would you like to go next?")

    print_pause("Where would you like to go next?")



import time
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find "
                    "yourself in the lobby.")
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already "
                        "given you your ID card, so there is nothing "
                        "more to do here now.")
        else:
            print_pause("The clerk greets you and gives you your ID "
                        "card.")
            items.append("ID card")
    elif floor == '2':
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself "
                    "in the human resources department.")
        if "handbook" in items:
            print_pause("The HR folks are busy at their desks.")
            print_pause("There doesn't seem to be much to do here.")
        else:
            print_pause("The head of HR greets you.")
            if "ID card" in items:
                print_pause("He looks at your ID card and then "
                            "gives you a copy of the employee handbook.")
                items.append("handbook")
            else:
                print_pause("He has something for you, but says he can't "
                            "give it to you until you go get your ID card.")
        print_pause("You head back to the elevator.")
    elif floor == '3':
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself "
                    "in the engineering department.")

    print_pause("Where would you like to go next?")



import time
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find "
                    "yourself in the lobby.")
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already "
                        "given you your ID card, so there is nothing "
                        "more to do here now.")
        else:
            print_pause("The clerk greets you and gives you your ID "
                        "card.")
            items.append("ID card")
    elif floor == '2':
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself "
                    "in the human resources department.")
        if "handbook" in items:
            print_pause("The HR folks are busy at their desks.")
            print_pause("There doesn't seem to be much to do here.")
        else:
            print_pause("The head of HR greets you.")
            if "ID card" in items:
                print_pause("He looks at your ID card and then "
                            "gives you a copy of the employee handbook.")
                items.append("handbook")
            else:
                print_pause("He has something for you, but says he can't "
                            "give it to you until you go get your ID card.")
        print_pause("You head back to the elevator.")
    elif floor == '3':
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself "
                    "in the engineering department.")
        print_pause("This is where you work!")
        if "ID card" in items:
            print_pause("You use your ID card to open the door.")
            print_pause("Your program manager greets you and tells "
                        "you that you need to have a copy of the "
                        "employee handbook in order to start work.")
            if "handbook" in items:
                print_pause("Fortunately, you got that from HR!")
                print_pause("Congratulatons! You are ready to start your new job "
                            "as vice president of engineering!")
                break
            else:
                print_pause("They scowl when they see that you don't have it, "
                            "and send you back to the elevator.")
        else:
            print_pause("Unfortunately, the door is locked "
                        "and you can't get in.")
            print_pause("It looks like you need some kind of "
                        "key card to open the door.")
            print_pause("You head back to the elevator.")

    print_pause("Where would you like to go next?")




import time
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find "
                    "yourself in the lobby.")
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already "
                        "given you your ID card, so there is nothing "
                        "more to do here now.")
        else:
            print_pause("The clerk greets you and gives you your ID "
                        "card.")
            items.append("ID card")
    elif floor == '2':
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself "
                    "in the human resources department.")
        if "handbook" in items:
            print_pause("The HR folks are busy at their desks.")
            print_pause("There doesn't seem to be much to do here.")
        else:
            print_pause("The head of HR greets you.")
            if "ID card" in items:
                print_pause("He looks at your ID card and then "
                            "gives you a copy of the employee handbook.")
                items.append("handbook")
            else:
                print_pause("He has something for you, but says he can't "
                            "give it to you until you go get your ID card.")
        print_pause("You head back to the elevator.")
    elif floor == '3':
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself "
                    "in the engineering department.")
        print_pause("This is where you work!")
        if "ID card" in items:
            print_pause("You use your ID card to open the door.")
            print_pause("Your program manager greets you and tells "
                        "you that you need to have a copy of the "
                        "employee handbook in order to start work.")
            if "handbook" in items:
                print_pause("Fortunately, you got that from HR!")
                print_pause("Congratulatons! You are ready to start your new job "
                            "as vice president of engineering!")
                break
            else:
                print_pause("They scowl when they see that you don't have it, "
                            "and send you back to the elevator.")
        else:
            print_pause("Unfortunately, the door is locked "
                        "and you can't get in.")
            print_pause("It looks like you need some kind of "
                        "key card to open the door.")
            print_pause("You head back to the elevator.")

    print_pause("Where would you like to go next?")




    import time
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")


def first_floor():
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find "
                "yourself in the lobby.")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already "
                    "given you your ID card, so there is nothing "
                    "more to do here now.")
    else:
        print_pause("The clerk greets you and gives you your ID "
                    "card.")
        items.append("ID card")


def second_floor():
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself "
                "in the human resources department.")
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("The head of HR greets you.")
        if "ID card" in items:
            print_pause("He looks at your ID card and then "
                        "gives you a copy of the employee handbook.")
            items.append("handbook")
        else:
            print_pause("He has something for you, but says he can't "
                        "give it to you until you go get your ID card.")
    print_pause("You head back to the elevator.")


def third_floor():
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself "
                "in the engineering department.")
    print_pause("This is where you work!")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.")
        print_pause("Your program manager greets you and tells "
                    "you that you need to have a copy of the "
                    "employee handbook in order to start work.")
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulatons! You are ready to start your new job "
                        "as vice president of engineering!")
            # break
        else:
            print_pause("They scowl when they see that you don't have it, "
                        "and send you back to the elevator.")
    else:
        print_pause("Unfortunately, the door is locked "
                    "and you can't get in.")
        print_pause("It looks like you need some kind of "
                    "key card to open the door.")
        print_pause("You head back to the elevator.")


while True:
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        first_floor()
    elif floor == '2':
        second_floor()
    elif floor == '3':
        third_floor()

    print_pause("Where would you like to go next?")


import time
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")


def first_floor():
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find "
                "yourself in the lobby.")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already "
                    "given you your ID card, so there is nothing "
                    "more to do here now.")
    else:
        print_pause("The clerk greets you and gives you your ID "
                    "card.")
        items.append("ID card")
    print_pause("You head back to the elevator.")
    ride_elevator() # Added a call here.


def second_floor():
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself "
                "in the human resources department.")
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("The head of HR greets you.")
        if "ID card" in items:
            print_pause("He looks at your ID card and then "
                        "gives you a copy of the employee handbook.")
            items.append("handbook")
        else:
            print_pause("He has something for you, but says he can't "
                        "give it to you until you go get your ID card.")
    print_pause("You head back to the elevator.")
    ride_elevator() # Added a call here.


def third_floor():
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself "
                "in the engineering department.")
    print_pause("This is where you work!")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.")
        print_pause("Your program manager greets you and tells "
                    "you that you need to have a copy of the "
                    "employee handbook in order to start work.")
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulatons! You are ready to start your new job "
                        "as vice president of engineering!")
        else:
            print_pause("They scowl when they see that you don't have it, "
                        "and send you back to the elevator.")
            ride_elevator()
    else:
        print_pause("Unfortunately, the door is locked "
                    "and you can't get in.")
        print_pause("It looks like you need some kind of "
                    "key card to open the door.")
        print_pause("You head back to the elevator.")
        ride_elevator() # Added a call here.


def ride_elevator():
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        first_floor()
    elif floor == '2':
        second_floor()
    elif floor == '3':
        third_floor()


ride_elevator()




import time
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro()
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def first_floor():
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find "
                "yourself in the lobby.")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already "
                    "given you your ID card, so there is nothing "
                    "more to do here now.")
    else:
        print_pause("The clerk greets you and gives you your ID "
                    "card.")
        items.append("ID card")
    print_pause("You head back to the elevator.")
    ride_elevator()


def second_floor():
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself "
                "in the human resources department.")
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("The head of HR greets you.")
        if "ID card" in items:
            print_pause("He looks at your ID card and then "
                        "gives you a copy of the employee handbook.")
            items.append("handbook")
        else:
            print_pause("He has something for you, but says he can't "
                        "give it to you until you go get your ID card.")
    print_pause("You head back to the elevator.")
    ride_elevator()


def third_floor():
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself "
                "in the engineering department.")
    print_pause("This is where you work!")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.")
        print_pause("Your program manager greets you and tells "
                    "you that you need to have a copy of the "
                    "employee handbook in order to start work.")
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulatons! You are ready to start your new job "
                        "as vice president of engineering!")
        else:
            print_pause("They scowl when they see that you don't have it, "
                        "and send you back to the elevator.")
            ride_elevator()
    else:
        print_pause("Unfortunately, the door is locked "
                    "and you can't get in.")
        print_pause("It looks like you need some kind of "
                    "key card to open the door.")
        print_pause("You head back to the elevator.")
        ride_elevator()


def ride_elevator():
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        first_floor()
    elif floor == '2':
        second_floor()
    elif floor == '3':
        third_floor()


intro()
ride_elevator()


import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def first_floor():
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find "
                "yourself in the lobby.")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already "
                    "given you your ID card, so there is nothing "
                    "more to do here now.")
    else:
        print_pause("The clerk greets you and gives you your ID "
                    "card.")
        items.append("ID card")
    print_pause("You head back to the elevator.")
    ride_elevator()


def second_floor():
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself "
                "in the human resources department.")
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("The head of HR greets you.")
        if "ID card" in items:
            print_pause("He looks at your ID card and then "
                        "gives you a copy of the employee handbook.")
            items.append("handbook")
        else:
            print_pause("He has something for you, but says he can't "
                        "give it to you until you go get your ID card.")
    print_pause("You head back to the elevator.")
    ride_elevator()


def third_floor():
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself "
                "in the engineering department.")
    print_pause("This is where you work!")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.")
        print_pause("Your program manager greets you and tells "
                    "you that you need to have a copy of the "
                    "employee handbook in order to start work.")
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulatons! You are ready to start your new job "
                        "as vice president of engineering!")
        else:
            print_pause("They scowl when they see that you don't have it, "
                        "and send you back to the elevator.")
            ride_elevator()
    else:
        print_pause("Unfortunately, the door is locked "
                    "and you can't get in.")
        print_pause("It looks like you need some kind of "
                    "key card to open the door.")
        print_pause("You head back to the elevator.")
        ride_elevator()


def ride_elevator():
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        first_floor()
    elif floor == '2':
        second_floor()
    elif floor == '3':
        third_floor()


def play_game():
    items = []
    intro()
    ride_elevator()


play_game()





import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def first_floor(items):
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find "
                "yourself in the lobby.")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already "
                    "given you your ID card, so there is nothing "
                    "more to do here now.")
    else:
        print_pause("The clerk greets you and gives you your ID "
                    "card.")
        items.append("ID card")
    print_pause("You head back to the elevator.")
    ride_elevator(items)


def second_floor(items):
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself "
                "in the human resources department.")
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("The head of HR greets you.")
        if "ID card" in items:
            print_pause("He looks at your ID card and then "
                        "gives you a copy of the employee handbook.")
            items.append("handbook")
        else:
            print_pause("He has something for you, but says he can't "
                        "give it to you until you go get your ID card.")
    print_pause("You head back to the elevator.")
    ride_elevator(items)


def third_floor(items):
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself "
                "in the engineering department.")
    print_pause("This is where you work!")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.")
        print_pause("Your program manager greets you and tells "
                    "you that you need to have a copy of the "
                    "employee handbook in order to start work.")
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulatons! You are ready to start your new job "
                        "as vice president of engineering!")
        else:
            print_pause("They scowl when they see that you don't have it, "
                        "and send you back to the elevator.")
            ride_elevator(items)
    else:
        print_pause("Unfortunately, the door is locked "
                    "and you can't get in.")
        print_pause("It looks like you need some kind of "
                    "key card to open the door.")
        print_pause("You head back to the elevator.")
        ride_elevator(items)


def ride_elevator(items):
    print_pause("Please enter the number for the "
                "floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        first_floor(items)
    elif floor == '2':
        second_floor(items)
    elif floor == '3':
        third_floor(items)


def play_game():
    items = []
    intro()
    ride_elevator(items)


play_game()
