Let's talk about block statements of various kinds in Python. We'll start with some simple stuff and get into more complicated things as the lesson progresses.

## Conditional Statements
The first type of block statement we'll take a look at is a `conditional` statement. You can think of this as just "if" and "else," literally. Here's a quick example:

```python
num = 8
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
print("Done")
```

In the above example, we check the remainder of `num` and `2`. If the remainder is 0, it must be an even number, so we print something that indicates that it's even. Notice that the code inside each `block` is indented appropriately. In Python, we indicate block sections by increasing the indentation by another tab (or 4 spaces). The block "ends" when we unindent, so in the above example the first block ends once we unindent and type `else`.

Notice that when you run this code, `Odd` is never printed. This is because the code that prints `Odd` is in a separate `block` from the code that prints `Even`. A conditional block looks at the boolean value that follows the conditional `if` keyword. So if, for example, we ran this code:

```python
    print(8 % 2 == 0)
```

the program prints `True`. So, in the first example we did, you can see that the code simplifies into something like this:

```python
if True:
    print("Even")
else:
    print("Odd")
print("Done")
```

Notice that what follows the `if` keyword _must_ be a boolean. It must be an expression that evaluates to either True or False. You can check all kinds of things using conditional logic like this! Based on the boolean value that we check, we determine which block of code to execute. It's worth noting that we don't _have_ to have an `else` block. We can simply write the statement as
```python
if num % 2 == 0:
    print("Even")
print("Done")
```
without the else block and it would only print out "Even" if the number is even and never "Odd".

We can also do more than just print one thing inside each block too - for example, we can add the value of `num` to an array containing only even numbers if we are in the first block, or add it to an array containing only odd numbers in the second block.

```python
evens = []
odds = []
if num % 2 == 0:
    print ("Even")
    evens.append(num)
else:
    print("Odd")
    odds.append(odd)
print(evens)
print(odds)
```

The above code will examine the number `num` and print the appropriate word as well as append it to the appropriate list. Using conditional statements like this, we can control what code executes based on any conditions we choose. This allows our code to be flexible and work generically, which brings us to the next topic!

## Functions

Functions are essentially named blocks of code. You can think of them kind of like variables - you give them a name, say how many arguments they accept, and then attach it to a big block of code that does something - hopefully something that relates to the name you gave it!

Think about the code that we were working with earlier - it examines a number and tells us whether or not it's odd or even, then it adds the number to an appropriate list. As is, the code only does this with the number `8`, but what if we wanted to do this for any number?

We can take the same code and throw it into a function and accept any number as the functions argument! Let's take a look at how that works:

```python
evens = []
odds = []


def is_even(num):
    if num % 2 == 0:
        print ("Even")
        evens.append(num)
    else:
        print("Odd")
        odds.append(num)
    print ("Done")


is_even(2)
is_even(3)
is_even(4)
print("Evens: {}".format(evens))
print("Odds: {}".format(odds))
```

Here you can see we're using a new keyword, `def`, which is shorthand for `define`. The `def` keyword tells Python that we're about to define a function. The next thing that follows is the name of the function. In this case, that's `is_even`. This function accepts exactly 1 argument, `num`, and our code block from before follows.

Functions are useful because you can _call_ them and conveniently perform the same routine over and over again. You can see in the above code snippet that we are calling the function `is_even` several times afterward. We can call the function by using its name followed by a pair of parentheses that contains all of the necessary arguments to call the function. In this case, we only need one argument: a number. So invoking the function looks like `is_even(55)`.

If the function took two arguments, we would separate all of the arguments in the parentheses with commas, like this:
```python
def my_function(x, y):
    return True

my_function(1, 2)
my_function(3, 4)
```

You get the idea.

Functions are `block statements` just like the `conditional statements` that we talked about earlier. Using indentation, we indicate what code belongs in the block that we attach to the function name. So anything that's indented more than the `def` statement is part of the function, up until we unindent or reach the end of the file. To illustrate this point super clearly:

```python
def my_silly_function(x):
    print(1+1)
    print(2+2)
    print(3+3)
    print(x+x)

print(False)
```

In the above example, all of the addition statements and the `return` statement are part of the function. That means that it will execute that code every time you call it. If you call `my_silly_function` several times, you'll always print out `2, 4, and 6` as well as `x` added to itself, but you won't print out `False` every time you call the function because it _is not part of the function_.

And that's about it! W