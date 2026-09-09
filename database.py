import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

def _load_csv(filename):
    path = DATA_DIR / filename
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def load_donors():
    donors = _load_csv("donors.csv")
    for d in donors:
        d["quantity_kg"] = float(d["quantity_kg"])
        d["latitude"] = float(d["latitude"])
        d["longitude"] = float(d["longitude"])
    return donors

def load_receivers():
    receivers = _load_csv("receivers.csv")
    for r in receivers:
        r["required_kg"] = float(r["required_kg"])
        r["priority"] = int(r["priority"])
        r["latitude"] = float(r["latitude"])
        r["longitude"] = float(r["longitude"])
    return receivers
