import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import modules.ui as ui

def main():
    ui.print_logo()
    ui.print_divider()

if __name__ == "__main__":
    main()
