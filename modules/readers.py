import csv
from typing import NamedTuple
from datetime import datetime, date

Objective = NamedTuple("Objective", [
    ("creation_datetime", datetime),
    ("id", str),
    ("max", int),
    ("has_deadline", bool),
    ("deadline", date | None),
    ("name", str),
    ("description", str)
    ])

Log = NamedTuple("Log", [
    ("creation_datetime", datetime),
    ("id", str),
    ("value", int),
    ("comments", str)
    ])



def read_objectives(file_path: str) -> list[Objective]:

    result = []
    with open(file_path, encoding="utf-8") as f:

        myReader = csv.reader(f, delimiter=";")
        next(myReader) # Ignore first line since it just contains the name of the columns

        for line in myReader:
            objective = parse_objective(*line)
            result.append(objective)


    return result

def read_logs(file_path: str) -> list[Log]:

    result = []
    with open(file_path, encoding="utf-8") as f:

        myReader = csv.reader(f, delimiter=";")
        next(myReader) # Ignore first line since it just contains the name of the columns

        for line in myReader:
            log = parse_log(*line)
            result.append(log)


    return result

def parse_objective(creation_datetime, id, max, has_deadline, deadline, name, description) -> Objective:

    if has_deadline != "1" and has_deadline != "0": # Ensure has_deadline has always a valid value to avoid possible problems in the future
        raise ValueError("Invalid value in column `has_deadline`.")

    has_deadline = bool(int(has_deadline))

    if has_deadline:
        deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
    else:
        deadline = None

    return Objective(
        datetime.strptime(creation_datetime, "%Y-%m-%d-%H:%M"),
        id,
        int(max),
        has_deadline,
        deadline,
        name,
        description
        )


def parse_log(creation_datetime, id, value, comments) -> Log:
    return Log(
        datetime.strptime(creation_datetime, "%Y-%m-%d-%H:%M"),
        id,
        int(value),
        comments
        )
