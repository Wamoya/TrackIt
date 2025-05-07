from matplotlib import pyplot as plt
from modules.readers import Objective, Log
from datetime import timedelta, date
from collections import Counter



def get_list_of_attribute(info: list[Objective] | list[Log], attr: str) -> list[str] | list[int] | list[date] | list[bool]:
    return [getattr(line, attr) for line in info] # Does allow repetitions


def filter_by(info: list[Objective] | list[Log], attr: str, value: str | int | date | bool) -> list[Objective] | list[Log]:
    return [line for line in info if getattr(line, attr) == value]


def plt_activity(objectives: list[Objective], logs: list[Log], period: str="year"):
    assert False, "modules.trackit.plt_activity() is not finished."

    if period not in ["week", "month", "year", "always"]:
        raise ValueError(f"Invalid time period: {period}")

    match period:
        case "week":
            pass
        case "month":
            pass
        case "year":
            pass
        case "always":
            pass

    counts = Counter(log.creation_date for log in logs)
    min_date = min(counts.keys())
    max_date = max(counts.keys())
    full_range = [min_date + timedelta(days=i) for i in range((max_date-min_date).days + 1)]


    
    y_values = [counts.get(day, 0) for day in full_range]
    x_labels = [date.strftime("%Y-%m-%d") for date in full_range]
    
    #plt.figure(figsize=(10, 5))
    plt.plot(x_labels, y_values, marker="o", color="skyblue", linestyle="-")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Log count")
    plt.title("Log activity over time")
    plt.tight_layout()
    plt.grid(True)
    ##plt.plot(x_labels, y_values, marker='', color='skyblue', linestyle='-')
    #plt.title("General activity analysis, based on creation dates.")
    #plt.plot(list_objectives_creation_dates, label="Objectives")
    #plt.plot(list_logs_creation_dates,       label="Logs")
    #plt.legend()
    plt.show()

