import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import modules.ui as ui
import routines
import modules.tests as tests

OBJECTIVES_PATH = "data/objectives.csv"
LOGS_PATH       = "data/log.csv"


def test_mode(yes: bool):
    if yes:
        ui.set_color("red")
        print("Running on mode: Test")
        ui.set_color("reset")

        run_tests()

        ui.set_color("green")
        print("All tests have been executed.")
        ui.set_color("reset")
        exit(0)

    else:
        ui.set_color("red")
        print("Running on mode: Normal")
        ui.set_color("reset")

def run_tests():
    tests.test_reloading_db()
    tests.test_get_list_of_attribute()
    tests.test_filter_by()
    tests.test_plt_activity()



def main():
    test_mode(False) # Temporary function call for debugging purposes
    
    ui.print_logo()
    objectives, logs = routines.read_db(OBJECTIVES_PATH, LOGS_PATH)

    next_menu = "main"
    running   = True
    while running:
        match next_menu:
            case "main":
                title   = "What do you want to do?"
                options = {"i": "Edit the database.",
                           "o": "Read the database.",
                           "q": "Quit"}
            case "edit":
                title   = "How do you want to edit the database?"
                options = {"1": "Add a new entry to the log.",
                           "2": "Create a new objective.",
                           "3": "Delete a log entry.",
                           "4": "Delete an objective.",
                           "0": "Go back."}
            case "read":
                title   = "How do you want to read the database?"
                options = {"1": "...",
                           "2": "...",
                           "0": "Go back."}

        answer = routines.menu(title, options)

        match next_menu:
            case "main":
                match answer:
                    case "i":
                        next_menu = "edit"
                    case "o":
                        next_menu = "read"
                    case "q":
                        running = False
            case "edit":
                match answer:
                    case "1":
                        routines.edit_add(logs, LOGS_PATH)
                    case "2":
                        routines.edit_add(objectives, OBJECTIVES_PATH)
                    case "3":
                        print("Deleting log entry stuff...")
                    case "4":
                        print("Deleting objective stuff...")
                    case "0":
                        next_menu = "main"
            case "read":
                match answer:
                    case "1":
                        print("...")
                    case "2":
                        print("...")
                    case "0":
                        next_menu = "main"







if __name__ == "__main__":
    main()
