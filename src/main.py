import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import modules.tests

def main():
    print(modules.tests.test())

if __name__ == "__main__":
    main()
