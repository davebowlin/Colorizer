"""
    A simple example of importing and using Colorizer
"""
from mypycolorizer.colorizer import Color as color  # import the class as an object named color

# different examples of using the colors
print(f"This is {color.RED}red{color.RESET} text.")
print(f"And this is {color.ITALIC}{color.GREEN}italicized green{color.RESET} text.")
print(f"{color.BLUE_BG}{color.YELLOW} Yellow on blue {color.REVERSE} and blue on yellow {color.RESET_REVERSE} and back to yellow on blue.{color.RESET} And now everything reset to default.")
print(f"If supported in your terminal, this will {color.BLINK}blink{color.RESET}.")
