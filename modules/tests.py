import modules.ui as ui
import modules.readers as readers
import routines


def test_reloading_db(objectives_db="data/objectives.csv", logs_db="data/log.csv"):
    objectives, logs = routines.read_db(objectives_db, logs_db)

    print(objectives)
    ui.print_divider()

    print(logs)
    ui.print_divider()

