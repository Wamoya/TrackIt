import modules.ui as ui
import modules.readers as readers
from modules.readers import Objective, Log


def read_db(objectives_path, log_path) -> tuple[list[Objective], list[Log]]: # Read both .csv files and return their values
    ui.color("green")
    print("\tReloading...")
    ui.color("reset")

    objectives = readers.read_objectives(objectives_path)
    print(f"\t- {len(objectives)} objective(s) were loaded.")

    logs = readers.read_logs(log_path)
    print(f"\t- {len(logs)} log(s) were loaded.\n")

    return objectives, logs
