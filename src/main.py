import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import modules.ui as ui
import routines
import modules.tests as tests

OBJECTIVES_DB = "data/objectives.csv"
LOGS_DB       = "data/log.csv"


def test_mode(yes: bool):
    if yes:
        ui.set_color("red")
        print("Running on mode: Test")
        ui.set_color("reset")

        run_tests()

        ui.set_color("green")
        print("All thest have been executed.")
        ui.set_color("reset")
        exit(0)

    else:
        ui.set_color("red")
        print("Running on mode: Normal")
        ui.set_color("reset")

def run_tests():
    tests.test_reloading_db()



def main():
    test_mode(False) # Temporary function call for debugging purposes
    
    ui.print_logo()
    objectives, logs = routines.read_db(OBJECTIVES_DB, LOGS_DB)

    answer = routines.main_menu()

    match answer:
        case "i":
            answer = routines.edit_menu()
        case "o":
            answer = routines.read_menu()
        case "q":
            exit(0)




if __name__ == "__main__":
    main()
