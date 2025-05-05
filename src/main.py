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
        print(ui.color("red") + "Running on mode: Test" + ui.color("reset"))

        run_tests()

        print(ui.color("green") + "All thest have been executed." + ui.color("reset"))
        exit(0)
    else:
        print(ui.color("red") + "Running on mode: Normal" + ui.color("reset"))

def run_tests():
    tests.test_reloading_db()



def main():
    test_mode(False) # Temporary function call for debugging purposes
    
    ui.print_logo()
    objectives, logs = routines.read_db(OBJECTIVES_DB, LOGS_DB)

    

if __name__ == "__main__":
    main()
