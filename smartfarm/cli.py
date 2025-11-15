import argparse
from . import sensors, data_manager

def main():
    parser = argparse.ArgumentParser(
        prog="smartfarm",
        description="Smart Farm Terminal — beginner → intermediate learning project."
    )

    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("read", help="Read one simulated sensor sample")
    sub.add_parser("save", help="Save one sample to CSV")
    sub.add_parser("stats", help="Show basic stats from CSV")

    args = parser.parse_args()

    if args.cmd == "read":
        sample = sensors.sample()
        for k, v in sample.items():
            print(f"{k:15} {v}")
    
    elif args.cmd == "save":
        sample = sensors.sample()
        data_manager.append_sample(sample)
        print("Sample saved to data/readings.csv")

    elif args.cmd == "stats":
        df = data_manager.load_data()
        if df is None or df.empty:
            print("No data available.")
            return
        print(df.describe())

    else:
        parser.print_help()
