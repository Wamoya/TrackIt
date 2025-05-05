import modules.ui as ui
import modules.readers as readers
from modules.readers import Objective, Log


def read_db(objectives_path, log_path) -> tuple[list[Objective], list[Log]]: # Read both .csv files and return their values
    ui.set_color("green")
    print("\tReloading...")
    ui.set_color("reset")

    objectives = readers.read_objectives(objectives_path)
    print(f"\t- {len(objectives)} objective(s) were loaded.")

    logs = readers.read_logs(log_path)
    print(f"\t- {len(logs)} log(s) were loaded.\n")

    return objectives, logs

def main_menu() -> str:
    while True:
        ui.set_color("cyan")
        print("What do you want to do?")
        print("\ti. Edit the database.")
        print("\to. Read the database.")
        print("\tq. Quit.")

        valid_answers = ["i", "o", "q"]
        answer = ui.get_answer(valid_answers)

        if answer == "":
            pass
        else:
            return answer

def edit_menu():
    while True:
        ui.set_color("cyan")
        print("How do you want to edit the database?")
        print("\t1. Add a new entry to the log.")
        print("\t2. Create a new objective.")
        print("\t3. Delete a log entry.")
        print("\t4. Delete an objective.")
        print("\t0. Go back.")

        valid_answers = ["1", "2", "3", "4", "0"]
        answer = ui.get_answer(valid_answers)

        if answer == "":
            pass
        else:
            return answer


def read_menu():
    while True:
        ui.set_color("cyan")
        print("How do you want to read the database?")
        print("\t1. Use fzf.")
        print("\t2. ...")

        valid_answers = ["1", "2"]
        answer = ui.get_answer(valid_answers)

        if answer == "":
            pass
        else:
            return answer
