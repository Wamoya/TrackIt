import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import modules.ui as ui
import modules.readers as readers

OBJECTIVES_DB = "data/objectives.csv"
LOGS_DB = "data/log.csv"

def main():
    ui.print_logo()
    objectives = readers.read_objectives(OBJECTIVES_DB)
    logs =       readers.read_logs(LOGS_DB)
    ui.print_divider()
    print(objectives)
    ui.print_divider()
    print(logs)

if __name__ == "__main__":
    main()
