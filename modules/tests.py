import modules.ui as ui
import modules.readers as readers
import routines
import modules.trackit as ti


def test_reloading_db(objectives_path="data/objectives.csv", logs_path="data/log.csv"):
    objectives, logs = routines.read_db(objectives_path, logs_path)

    print(objectives)
    ui.print_divider()

    print(logs)
    ui.print_divider()

def test_get_list_of_attribute(objectives_path="data/objectives.csv", logs_path="data/log.csv"):
    objectives, logs = routines.read_db(objectives_path, logs_path)

    objectives_attr = ["creation_date",
                       "id",
                       "max",
                       "has_deadline",
                       "deadline",
                       "name",
                       "description"
                       ]
    logs_attr       = ["creation_date",
                       "id",
                       "value",
                       "comments"
                       ]
    
    for attr in objectives_attr:
        result = ti.get_list_of_attribute(objectives, attr)
        print(result)

    for attr in logs_attr:
        result = ti.get_list_of_attribute(logs, attr)
        print(result)

def test_filter_by(objectives_path="data/objectives.csv", logs_path="data/log.csv"):
    objectives, logs = routines.read_db(objectives_path, logs_path)
    
    print(ti.filter_by(objectives, "has_deadline", False))

def test_get_count_per_attr(objectives_path="data/objectives.csv", logs_path="data/log.csv"):
    objectives, logs = routines.read_db(objectives_path, logs_path)

    print(ti.get_count_per_attr(logs, "creation_date"))

def test_plt_activity(objectives_path="data/objectives.csv", logs_path="data/log.csv"):
    objectives, logs = routines.read_db(objectives_path, logs_path)
    ti.plt_activity(objectives, logs)


