LOGO = "assets/logo.txt"


# Returns the ANSI color code of a color passed as an argument
def set_color(color):
    match color:
        case "red":
            color = "\033[31m"
        case "green":
            color = "\033[32m"
        case "yellow":
            color = "\033[33m"
        case "blue":
            color = "\033[34m"
        case "purple":
            color = "\033[35m"
        case "cyan":
            color = "\033[36m"
        case "reset":
            color = "\033[0m"

        case _:
            raise ValueError("Invalid argument.")

    print(color, end="")

# Prints the logo 
def print_logo():
    code = "yellow"
    with open(LOGO, encoding="utf-8") as f:
        set_color(code)
        print(f.read())
        set_color("reset")


def print_divider():
    print("\n" + "-" * 100 + "\n\n")
