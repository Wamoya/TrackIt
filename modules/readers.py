import csv
from typing import NamedTuple
from datetime import datetime, date

Objective = NamedTuple("Objective", [
    ("creation_date", date),
    ("id", str),
    ("max", int),
    ("has_deadline", bool),
    ("deadline", date | None),
    ("name", str),
    ("description", str)
    ])

Log = NamedTuple("Log", [
    ("creation_date", date),
    ("id", str),
    ("value", int),
    ("comments", str)
    ])



def read_objectives(file_path: str) -> list[Objective]:
    result = []
    with open(file_path, encoding="utf-8") as f:
        myReader = csv.reader(f, delimiter=";")
        next(myReader)
        for creation_date, id, max, has_deadline, deadline, name, description in myReader:
            if bool(int(has_deadline)):
                deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
            else:
                deadline = None
            result.append(Objective(
                datetime.strptime(creation_date, "%Y-%m-%d").date(),
                id,
                int(max),
                bool(int(has_deadline)),
                deadline,
                name,
                description
                ))

    return result

def read_logs(file_path: str) -> list[Log]:
    result = []
    with open(file_path, encoding="utf-8") as f:
        myReader = csv.reader(f, delimiter=";")
        next(myReader)
        for creation_date, id, value, comments in myReader:
            result.append(Log(
                datetime.strptime(creation_date, "%Y-%m-%d").date(),
                id,
                int(value),
                comments
                ))

    return result

