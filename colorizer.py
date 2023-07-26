class LowercaseAttributesMeta(type):
    """A metaclass that automatically creates lowercase variants of class attributes."""
    def __new__(mcls, name, bases, attrs):
        # Create the class as normal.
        cls = super().__new__(mcls, name, bases, attrs)
        
        # Add lowercase attributes.
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, str) and attr_name.isupper():
                setattr(cls, attr_name.lower(), attr_value)
        
        return cls

class Color(metaclass=LowercaseAttributesMeta):
    
    BOLD_BRIGHT = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    RAPID_BLINK = "\033[6m"
    REVERSE = "\033[7m"
    HIDE = "\033[8m"
    STRIKETHROUGH = "\033[9m"
    
    RESET = "\033[0m"  # resets all colors and styles
    RESET_BACKGROUND = "\033[49m"
    RESET_FOREGROUND = "\033[7m"
    RESET_REVERSE = "\033[27m"
    RESET_BOLD_BRIGHT = "\033[21m"
    RESET_DIM = "\033[22m"
    RESET_ITALIC = "\033[23m"
    RESET_UNDERLINE = "\033[24m"
    RESET_BLINK = "\033[25m"
    RESET_HIDE = "\033[28m"
    RESET_STRIKETHROUGH = "\033[29m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    ORANGE = "\033[38;5;208m"

    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    BLACK_BG = "\033[40m"
    RED_BG = "\033[41m"
    GREEN_BG = "\033[42m"
    YELLOW_BG = "\033[43m"
    BLUE_BG = "\033[44m"
    MAGENTA_BG = "\033[45m"
    CYAN_BG = "\033[46m"
    WHITE_BG = "\033[47m"

    @classmethod
    def colorize(cls, color, text):
        return f'{getattr(cls, color.upper(), "")}{text}{cls.RESET}'
    @classmethod
    def get_color(cls, name):
        """Gets the color constant for the given name."""
        if name.lower() in cls.__dict__:
            return getattr(cls, name.lower())
        elif name.upper() in cls.__dict__:
            return getattr(cls, name.upper())
        else:
            raise ValueError(f"Invalid color name: {name}")
        
# example use:
# print(Color.colorize("red", "Hello, World!"))

# print(f"{Color.GREEN}This is green text.{Color.RESET}")

# color = Color()
# print(f"{color.ITALIC}{color.BRIGHT_BLUE}This is italic bright red.{color.RESET}")
