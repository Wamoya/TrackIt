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

# Returns the ANSI color code of a color passed as an argument
def set_color(color):
    print(f"\033[{colors[color]}m", end="")

def colored_text(text: str, color_initial: str, color_final: str="reset"):
    return f"\033[{colors[color_initial]}m{text}\033[{colors[color_final]}m"

def get_answer(valid_answers: list[str], color_initial: str="magenta", color_final: str="reset") -> str:

    valid_answers_str = f"[{'/'.join(answer for answer in valid_answers)}]"

    prompt_msg = f"Waiting for user input {valid_answers_str} "
    error_msg  = f"Invalid input. Accepted values are {valid_answers_str}\n"

    answer = input(colored_text(prompt_msg, color_initial, color_final)).strip().lower()

    if answer in valid_answers:
        return answer
    else:
        set_color("red")
        print(error_msg)
        return ""


# Prints the logo 
def print_logo():
    code = "yellow"
    with open(LOGO, encoding="utf-8") as f:
        set_color(code)
        print(f.read())
        set_color("reset")


def print_divider():
    print("\n" + "-" * 100 + "\n\n")
