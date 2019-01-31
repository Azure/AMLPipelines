import argparse
import os

print("In dataprep.py: as a data scientist, this is where you should fill in your dataprep code.")

parser = argparse.ArgumentParser("dataprep")

parser.add_argument("--input_data", type=str, help="input data")
parser.add_argument("--processed_data", type=str, help="processed_data directory")

args = parser.parse_args()

print(f"Argument 1: {args.input_data}")
print(f"Argument 2: {args.processed_data}")

if not (args.processed_data is None):
	os.makedirs(args.processed_data, exist_ok=True)
	print(f"{args.processed_data} created")
