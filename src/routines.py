import modules.ui as ui
import modules.readers as readers
from modules.readers import Objective, Log
import subprocess


def read_db(objectives_path, log_path) -> tuple[list[Objective], list[Log]]: # Read both .csv files and return their values
    ui.set_color("green")
    print("\n\tReloading...")
    ui.set_color("reset")

    objectives = readers.read_objectives(objectives_path)
    print(f"\t- {len(objectives)} objective(s) were loaded.")

    logs = readers.read_logs(log_path)
    print(f"\t- {len(logs)} log(s) were loaded.\n")

    return objectives, logs

def menu(command_list_path: str) -> int:
    with open(command_list_path, "r") as f:
        all_lines = f.readlines()

    result = subprocess.run(
        ["fzf", "--height=40%", "--header=Select a command to use", "--border", "--layout=reverse-list"],
        input = "".join(all_lines),
        text = True,
        capture_output = True
    )
    
    selected_command = result.stdout.strip() if result.stdout else "-1"

    # Format of each command:
    # 00. Description
    # (command code). (command description)

    command_code_length = 2
    command_code        = int(f"{selected_command[:command_code_length]}")

    return command_code

def edit_add(info: list[Objective] | list[Log], path: str):

    if isinstance(info[0], Objective):
        constructor = Objective
        parser      = readers.parse_objective
    else:
        constructor = Log
        parser      = readers.parse_log

    parameters = []
    for parameter in constructor._fields:
        parameters.append(input(ui.colored_text(f"\t{parameter}: ", "cyan")))

    error = False
    try:
        _ = parser(*parameters)
    except:
        error = True
        ui.set_color("red")
        print("An error occured when trying to convert user input to new entry...\nReturning to previous menu...")

    if not error:
        new_entry_str = f"{";".join(parameters)}\n"
        with open(path, "a") as f:
            f.write(new_entry_str)

def edit_delete(path: str):

    with open(path, "r") as f:
        all_lines = f.readlines()

    result = subprocess.run(
        ["fzf", "--multi", "--height=40%", "--header=Select entries to delete", "--border"],
        input = "".join(all_lines[::-1]), # Reverse line order to start the cursor on the last entry
        text = True,
        capture_output=True
    )

    selected_lines = result.stdout.strip().split("\n") if result.stdout else []

    remaining_lines = [line for line in all_lines if line.strip("\n") not in selected_lines]

    with open(path, "w") as f:
        f.writelines(remaining_lines)

    print(f"Deleted entries: {len(selected_lines)}")


