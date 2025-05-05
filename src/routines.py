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

def main_menu():
    while True:
        ui.set_color("cyan")
        print("What do you want to do?")
        print("\ti. Edit the database.")
        print("\to. Read the database.")
        print("\tq. Quit.")

        response = input(ui.colored_text("Waiting for user input [i/o/q]: ", "cyan")).strip().lower()

        match response:
            case "i":
                edit_menu()
                break
            case "o":
                read_menu()
                break
            case "q":
                exit(0)
            case _:
                ui.set_color("red")
                print("Invalid input. Accepted values are: i, o, q\n")
                ui.set_color("reset")

def edit_menu():
    assert False, "UNIMPLEMENTED"

def read_menu():
    assert False, "UNIMPLEMENTED"
