LOGO = "assets/logo.txt"


colors = {
        "black":   "30",
        "red":     "31",
        "green":   "32",
        "yellow":  "33",
        "blue":    "34",
        "magenta": "35",
        "cyan":    "36",
        "white":   "37",
        "reset":   "0"
        }

# Prints the ANSI color code of a color passed as an argument
def set_color(color: str):
    print(f"\033[{colors[color.lower()]}m", end="")

def colored_text(text: str, color_initial: str, color_final: str="reset"):
    return f"\033[{colors[color_initial.lower()]}m{text}\033[{colors[color_final.lower()]}m"

# Prints the logo 
def print_logo():
    color = "yellow"
    with open(LOGO, encoding="utf-8") as f:
        set_color(color)
        print(f.read())
        set_color("reset")

def print_divider():
    print("\n" + "-" * 100 + "\n\n")
