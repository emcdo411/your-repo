import argparse, csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def norm_cat(s):
    return s.strip().lower().replace(" ", "_")

def parse_date(s):
    return datetime.fromisoformat(s)

def read_rows(p):
    with p.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if not row.get("date") or not row.get("amount") or not row.get("category"):
                continue
            try:
                dt = parse_date(row["date"])
                amt = float(row["amount"])
            except Exception:
                continue
            yield {"date": dt, "amount": amt, "category": norm_cat(row["category"])}

def write_csv(path, fieldnames, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

def main():
    ap = argparse.ArgumentParser(description="Mini ETL")
    ap.add_argument("--in", dest="inp", required=True, help="input CSV")
    ap.add_argument("--out", dest="outdir", required=True, help="output directory")
    args = ap.parse_args()

    inp = Path(args.inp)
    outdir = Path(args.outdir)

    rows = list(read_rows(inp))
    assert rows, "No valid rows found."

    by_cat = defaultdict(float)
    by_month = defaultdict(float)
    for r in rows:
        by_cat[r["category"]] += r["amount"]
        key = r["date"].strftime("%%Y-%%m")
        by_month[key] += r["amount"]

    write_csv(outdir / "totals_by_category.csv", ["category","total_amount"],
              [{"category": k, "total_amount": f"{v:.2f}"} for k, v in sorted(by_cat.items())])

    write_csv(outdir / "totals_by_month.csv", ["month","total_amount"],
              [{"month": k, "total_amount": f"{v:.2f}"} for k, v in sorted(by_month.items())])

    print(f"Rows in: {len(rows)}")
    print("By category:", dict(by_cat))
    print("By month:", dict(by_month))

if __name__ == "__main__":
    main()
