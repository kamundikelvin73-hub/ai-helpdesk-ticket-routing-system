import csv
from pathlib import Path

def load_tickets(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def normalize_text(text):
    return text.lower().strip()

if __name__ == "__main__":
    tickets = load_tickets("../data/sample_tickets.csv")
    for ticket in tickets:
        ticket["clean_description"] = normalize_text(ticket["description"])
    print(f"Loaded {len(tickets)} tickets")
