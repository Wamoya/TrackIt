import modules.ui as ui
import modules.readers as readers
from modules.readers import Objective, Log
import subprocess


def read_db(objectives_path, log_path) -> tuple[list[Objective], list[Log]]: # Read both .csv files and return their values
    ui.set_color("green")
    print("\tReloading...")
    ui.set_color("reset")

    objectives = readers.read_objectives(objectives_path)
    print(f"\t- {len(objectives)} objective(s) were loaded.")

    logs = readers.read_logs(log_path)
    print(f"\t- {len(logs)} log(s) were loaded.\n")

    return objectives, logs



def menu(title: str, options: dict[str, str], color: str="cyan") -> str | None:
    answer = None
    while answer == None:
        ui.set_color(color)
        print(title)
        for key, description in options.items():
            print(f"\t{key}. {description}")

        print()

        valid_answers = list(options.keys())
        answer = get_answer(valid_answers)

    return answer

def get_answer(valid_answers: list[str], color_initial: str="magenta", color_final: str="reset") -> str | None:

    valid_answers_str = f"[{'/'.join(answer for answer in valid_answers)}]"

    prompt_msg = f"Waiting for user input {valid_answers_str} "
    error_msg  = f"Invalid input. Accepted values are {valid_answers_str}\n"

    answer = input(ui.colored_text(prompt_msg, color_initial, color_final)).strip().lower()

    if answer in valid_answers:
        return answer
    else:
        ui.set_color("red")
        print(error_msg)
        ui.set_color("reset")
        return None
