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

    running   = True
    while running:
        command_code = routines.menu("assets/command_list.txt")
        match command_code:
            case  1: # Add new objective
                routines.edit_add(objectives, OBJECTIVES_PATH)
                objectives, logs = routines.read_db(OBJECTIVES_PATH, LOGS_PATH)
            case  2: # Add new log
                routines.edit_add(logs, LOGS_PATH)
                objectives, logs = routines.read_db(OBJECTIVES_PATH, LOGS_PATH)
            case  3: # Delete objective
                routines.edit_delete(OBJECTIVES_PATH)
                objectives, logs = routines.read_db(OBJECTIVES_PATH, LOGS_PATH)
            case  4: # Delete log
                routines.edit_delete(LOGS_PATH)
                objectives, logs = routines.read_db(OBJECTIVES_PATH, LOGS_PATH)
            case  5: # Plot general view
                print("Now imagine a cool function.\nYeah, so cool ik ik")
            case 99: # Quit
                running = False




if __name__ == "__main__":
    main()
