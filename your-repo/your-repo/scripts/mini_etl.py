from datetime import datetime

def norm_cat(s: str):
    return s.strip().lower().replace(" ", "_")

def parse_date(s: str):
    return datetime.fromisoformat(s)
