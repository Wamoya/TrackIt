import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import modules.ui as ui
import modules.readers as readers

OBJECTIVES_DB = "data/objectives.csv"
LOGS_DB = "data/log.csv"


def test_mode(yes: bool):
    if yes:
        print(ui.color("red") + "Running on mode: Test" + ui.color("reset"))
        run_tests()
        exit(0)
    else:
        print(ui.color("red") + "Running on mode: Normal" + ui.color("reset"))

def run_tests():
    ui.print_logo()
    ui.print_divider()

    objectives = readers.read_objectives(OBJECTIVES_DB)
    logs       = readers.read_logs(LOGS_DB)

    print(objectives)
    ui.print_divider()

    print(logs)
    ui.print_divider()



def main():
    test_mode(True) # Temporary function call for debugging purposes
    
    ui.print_logo()

if __name__ == "__main__":
    main()
