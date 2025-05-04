# Returns the ANSI color code of a color passed as an argument
def color(color):
    match color:
        case "red":
            return "\033[31m"
        case "green":
            return "\033[32m"
        case "yellow":
            return "\033[33m"
        case "blue":
            return "\033[34m"
        case "purple":
            return "\033[35m"
        case "cyan":
            return "\033[36m"
        case "reset":
            return "\033[0m"

        case _:
            raise ValueError("Invalid argument.")

# Prints the logo 
def print_logo():
    logo = color("yellow") + r"""
 /$$$$$$$$                           /$$       /$$$$$$ /$$    
|__  $$__/                          | $$      |_  $$_/| $$    
   | $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  | $$ /$$$$$$  
   | $$ /$$__  $$|____  $$ /$$_____/| $$  /$$/  | $$|_  $$_/  
   | $$| $$  \__/ /$$$$$$$| $$      | $$$$$$/   | $$  | $$    
   | $$| $$      /$$__  $$| $$      | $$_  $$   | $$  | $$ /$$
   | $$| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$ /$$$$$$|  $$$$/
   |__/|__/      \_______/ \_______/|__/  \__/|______/ \___/  """ + color("reset")

    print(logo)

def print_divider():
    print("\n" + "-" * 100 + "\n\n")
