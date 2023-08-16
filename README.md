# MyPyColorizer

A very simple way to add color to your Python CLI apps.

## Installation

pip install mypycolorizer

#

# Example uses:

## Imports
 from mypycolorizer.colorizer import Color
 -or-
 from mypycolorizer.colorizer import Color as color

## Create an instance of the Colorizer class
 color = Color()
##
##
## Example usages
 print(Color.colorize("red", "Hello, World!"))

 print(f"{Color.GREEN}This is green text.{Color.RESET}")

 color = Color() # create an object of the Color class named color

 print(f"{color.ITALIC}{color.BRIGHT_BLUE}This is italic bright blue.{color.RESET}")

##
# Caveats:

 Not all escape codes work with all terminals. Be sure to test your terminal with the styles you  would like to use.
