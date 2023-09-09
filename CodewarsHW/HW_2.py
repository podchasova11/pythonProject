#  20
#  Your classmates asked you to copy some paperwork for them.
#  You know that there are 'n' classmates and the paperwork has 'm' pages.
#
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
#
# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0

def paperwork(n, m):
    if m > 0 and n >0:
        return m*n
    else:
        return 0

    #  21 Create a function that takes an integer

    #  as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#   22 If you've completed this kata already and want a bigger challenge, here's the 3D version
#
# Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. The box is special because it has the ability to change gravity.
#
# There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity, it begins to pull all the cubes to a certain side of the box, d, which can be either 'L' or 'R' (left or right). Below is an example of what a box of cubes might look like before and after switching gravity.
#
# +---+                                       +---+
# |   |                                       |   |
# +---+                                       +---+
# +---++---+     +---+              +---++---++---+
# |   ||   |     |   |   -->        |   ||   ||   |
# +---++---+     +---+              +---++---++---+
# +---++---++---++---+         +---++---++---++---+
# |   ||   ||   ||   |         |   ||   ||   ||   |
# +---++---++---++---+         +---++---++---++---+
# Given the initial configuration of the cubes in the box, find out how many cubes are in each of the n columns after Bob switches the gravity.
#
# Examples (input -> output:
# * 'R', [3, 2, 1, 2]      ->  [1, 2, 2, 3]
# * 'L', [1, 4, 5, 3, 5 ]  ->  [5, 5, 4, 3, 1]


def flip(d, a):
    return sorted(a, reverse=d == 'L')


flip('R', [3, 2, 1, 2])


#  23 For this problem you must create a program that says who ate the last cookie.
#  If the input is a string then "Zach" ate the cookie. If the input is a float or
#  an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie.
#  The way to return the statement is: "Who ate the last cookie? It was (name)!"
#
# Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach!
# (The reason you return Zach is because the input is a string)
#
# Note: Make sure you return the correct message with correct spaces and punctuation.

def cookie(x):
  return f'Who ate the last cookie? It was {"Zach" if type(x) is str else "Monica" if type(x) in [int, float] else "the dog"}!'


def cookies11(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")


def cookie1(x):
    if type(x) is str:
        return "Who ate the last cookie? It was Zach!"
    if type(x) is int or type(x) is float:
        return "Who ate the last cookie? It was Monica!"
        return "Who ate the last cookie? It was the dog!"


#  24 Grasshopper - Function syntax debugging
# A student was working on a function and made some syntax mistakes while coding.
# Help them find their mistakes and fix them.


def main(verb, noun):
    return str(verb, noun)

#  25