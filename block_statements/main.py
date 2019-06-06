'''
Let's do some simple tasks for your homework. This week, we'll do some practice using what we learned about functions
and conditional blocks to make some useful, reusable code! First, let's start by writing a function called plus_five
which takes a number and prints out that number plus five.
'''

def plus_five(x):
    return x + 5

'''
Once you've done that, call your function a few times and check your work. Calling plus_five with an argument of 5,
for example, should print the number 10.
'''

'''
Now let's try something a little more complicated. Using what you learned about conditional statements, write a function
that takes two numbers and prints the larger number. We'll call this function "max". This should be a little bit harder.
Try using a conditional statement to decide which number to pick. You can compare the two numbers using ordinary mathematical
operators such as < (less than), > (greater than), == (equal) , >= (greater than or equal), <= (less than or equal), etc.
'''

def max(x, y):
    if x < y:
        return y
    else:
        return x

p = plus_five(3)
print(p)
v = max(3, 11)
print(v)
