---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---


# Printing and drawing

In this lesson you will write code to print things on the screen and draw pretty pictures. This will give you the basics of Python: 

* running Python commands, called *functions*; 
* writing your own functions;
* using functions from libraries someone else wrote.

Let's get started. A computer program is made up of instructions that a computer follows. Here is a simple program:

```{code-cell}
:tags: [hide-output]

# A short program to print a few values

print(42)
print("Hello")
```

This program causes the computer to print the number 42 in the console window, and then to print the word "Hello". Click on "show code cell output" below the code to see the output. 

The lines of code are run, or *executed*, in the order they appear. 

The first line, `# A short program to print a few values`, is called a comment. Python ignores comments; they are just for us humans. Any line of code starting with the hashtag `#` is a comment.

The word `print` is a Python command, called a *function call*. All function calls look the same: the name of the function followed by parentheses, like `print()`. 

## Parameters

Sometimes there will be values inside the parentheses, like `42` or `"Hello"`. This data gives the function call additional information it needs to do its work. We call the values inside the parentheses the *parameters* to the function call. So `print(42)` has one parameter, `42`.

Each parameter has a type. The parameter `42` is an *integer*, or whole number. We can do things like multiply integers, although we won't do it yet.

The parameter `"Hello"` is a *string*, or sequence of letters and numbers. Notice that the quotes around `"Hello"` aren't printed. They just tell Python that `"Hello"` is a string. We can't multiply strings, but we might be able to do other things with them.  

## Exercise: Inigo Montoya

**Learning objective:** Run and edit Python code.

Copy the next program into your Python editor. Run the code in the editor to see the output.

```{code-cell}
:tags: [hide-output]
# A program to output a short greeting

print("Hello")
print("my")
print("name")
print("is")
print("Inigo")
print("Montoya")
```

Now use your editor to change the program to print out your name instead of Inigo Montoya's. Run it again to test it.

## Drawing with Pygame

Pygame is a library, or *module*, of Python functions that can be used to draw things on the screen.

Here is a little piece of code to draw two circles. To make it run, you'll need to download two files and put them together in the same directory: [circles.py](src/circles.py) and [simplgraphics.py](src/simplegraphics.py). Then run `circles.py`.  

```{literalinclude} src/circles.py
```

First let's look at the two function calls to the function named `circle`. The first one, `circle(Color('blue'), 125, 100, 50)` draws a blue circle centered at a location 125 pixels across from the left of the window, and 100 pixels down from the top of the window. The circle has a radius of 50 pixels.

The `circle` function call needs four parameters. How do I know? I wrote the `circle` function myself. The first parameter, `Color('blue')` is a little bit magical; we'll look at it later. The next three paramters, `125`, `100`, and `50` are integers, or whole numbers.


<!--
```{code-cell}
:tags: [remove-input]
exec(open("src/circles_mpl.py").read())
```
-->

## Using external functions: from...import

The `print` function we used earlier is built in to Python. The `circle` function is not: I wrote it myself, in the `simplegraphics.py` file. In order to use a function from a different file, you can use the `from X import Y` command, where `X` is the name of the file and `Y` is the name of the function. Like this:  

~~~{code-block}
from pygame import Color
from simplegraphics import init_graphics, circle, draw_and_wait_for_exit
~~~ 

This code imports `Color` from the `pygame` module, and imports some other functions from the `simplegraphics.py` file. We leave the `.py` extension off when we use `from X import Y` command.

The `init_graphics` function opens up a window on the screen for drawing. It takes two parameters: the width and height of the window you want to open. 

The drawing function `circle` doesn't really draw to the window; `circle` draws to something Pygame calls a screen. So the function `draw_and_wait_for_exit` copies the picture on the screen into the window, and waits for the user to click the button that closes the window.

## Exercise: bullseye

```{image} img/bullseye.png
:alt: Bullseye output
:width: 150px
:align: right
```

**Learning objective.** Use `circle()` function calls to make a drawing.

Copy the complete code for drawing two circles above into a new Python file. Edit the code to draw an archery bullseye like the one on the right.

*Hint:* My solution drew four circles centered at the center of the 400x400 pixel screen: one yellow, one red, one blue, and one black. Each circle had a different radius. The order that the circles is drawn matters, since circles drawn later cover up circles drawn first. 

## Writing your own functions

We can write our own commands in Python. A *function* in Python is like a little named program within your program. Here's an example that defines two different functions: `say_hello` and `why_goodbye`.

```{code-cell}
def say_hello():
    print("I say")
    print("hello.")

def why_goodbye():
    print("I don't know why you say goodbye.")
```

Check the output of the program above. You will see that there isn't any. The code defined two functions, but it didn't actually run the functions. 

Function definitions have two parts: a header, and a body. The header gives the name of the function you want to define (as well as some other things we’ll see later). The body is a set of lines of code that tell what the function does. Each line of the body must be indented by pressing the tab key. The indentations tell Python where the function body begins and ends.

The header uses the keyword def (short for define), the name of the function you’d like to define, parentheses after the name of the function, and a colon. So the header for the first function is:

```{code-block}
def say_hello():
```

The body of the first function is
```{code-block}
  print("I say")
  print("hello.")
```


## Exercise: I don't know why you say goodbye

**Learning objective**: Call functions that have been defined.

Copy the code for the function definitions for `say_hello` and `why_goodbye` into a new Python file in your editor. Add function calls to those function after the definitions so that program prints the following when run. (The answer is hidden under "show code cell source"; no peeking until you've tried it yourself.)


```{code-cell}
:tags: [hide-input]
def say_hello():
    print("I say")
    print("hello.")

def why_goodbye():
    print("I don't know why you say goodbye.")

say_hello()
why_goodbye()
say_hello()
```

## Exercise: reading code

**Learning objective.** Read through some code to figure out how to use functions from that code.

```{image} img/simple_shapes.png
:alt: Simple shapes
:width: 150px
:align: right
```

The picture on the right shows some example shapes that `simplegraphics.py` can draw. Here is the code that drew the shapes:

```{literalinclude} src/simplegraphics_examples.py
```

Open up `simplegraphics.py` and read the body of the `test_draw` function and look at the function headers for the functions `rectangle`, `ellipse`, `triangle` and `line`. Try to figure out what you might need to type to use these functions. Since this is a reading exercise, you don't have to type anything.

## Project: book cover

**Learning objective.** Use a variety of drawing commands to draw an interesting picture.

Childrens board books often have colorful, simple covers. See the covers for
[Goodnight Moon](https://upload.wikimedia.org/wikipedia/en/5/51/Goodnightmoon.jpg) and [The Very Hungry Caterpillar](https://upload.wikimedia.org/wikipedia/en/b/b5/HungryCaterpillar.JPG).

Create a new file with the name `bookcover.py` in the same directory as `simplegraphics.py`. Your job is to write complete code in `bookcover.py` to draw a picture, using function calls to `circle`, `rectangle`, `triangle`, and `ellipse`. You can create your own artwork from scratch, or use one of the book covers for inspiration.

Some other ideas are: light rays passing through a prism; a snowman in a cozy scene with evergreen trees; a child holding a bunch of balloons.

**Hints:** Simplify the problem. Set a simple objective, like drawing a single circle on the screen.

1) Start with the imports. You'll need functions like `init_graphics` and `draw_and_wait_for_exit`, as well as at least one of the shapes, like `circle`, so import those things. 

2) Then use `init_graphics`, a call to `circle`, and `draw_and_wait_for_exit()`. Run the code. If it works, add more drawing commands, importing the different types of shapes at the top of the code as needed.

3) Run the code frequently. If at any point, the code doesn't run, compare it carefully to the `circles.py` code we looked at earlier.
 