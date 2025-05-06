from matplotlib import pyplot as plt
from modules.readers import Objective, Log
from datetime import datetime, date

def get_list_of_attribute(info: list[Objective] | list[Log], attr) -> list[str] | list[int] | list[date] | list[bool]:
    return [getattr(line, attr) for line in info] # Does allow repetitions

def filter_by(info: list[Objective] | list[Log], attr: str, value: str | int | date | bool) -> list[Objective] | list[Log]:
    return [entry for entry in info if getattr(entry, attr) == value]


def get_count_per_attr(info: list[Objective] | list[Log], attr: str) -> dict[str, int] | dict[int, int] | dict[date, int] | dict[bool, int]:
    result = {}
    keys = set(get_list_of_attribute(info, attr))
    for key in keys:
        count = len(filter_by(info, attr, key))
        result[key] = count

    return result



def plt_activity(objectives: list[Objective], logs: list[Log]):
    assert False, "modules.trackit.plt_activity() is not finished."
    dates  = sorted(get_count_per_attr(logs, "creation_date").keys())
    counts = [get_count_per_attr(logs, "creation_date")[dat] for dat in dates]
    
    x_labels = [str(dat) for dat in dates]

    plt.plot(x_labels, counts, marker='o', color='skyblue', linestyle='-')
    #plt.title("General activity analysis, based on creation dates.")
    #plt.plot(list_objectives_creation_dates, label="Objectives")
    #plt.plot(list_logs_creation_dates,       label="Logs")
    #plt.legend()
    plt.show()

