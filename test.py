"""
    A simple example of importing and using Colorizer
"""
from colorizer import Colorizer  # import the class

color = Colorizer()  # create a Colorizer object named color

# different examples of using the colors
print(f"This is {color.red}red{color.reset} text.")
print(f"And this is {color.italic}{color.green}italicized green{color.reset} text.")
print(f"{color.blue_bg}{color.yellow} Yellow on blue {color.reverse}and blue on yellow {color.reset_reverse} and back to yellow on blue.{color.reset} And now everything reset to default.")
print(f"If supported in your terminal, this will {color.blink}blink{color.reset}.")
