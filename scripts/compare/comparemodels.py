import argparse
import os

print("In comparemodels.py: as a data scientist, this is where you should fill in code to compare two models.")

parser = argparse.ArgumentParser("comparemodels")
parser.add_argument("--new_model_location", type=str, help="new_model_location directory")
parser.add_argument("--prod_model_location", type=str, help="prod_model_location directory")
parser.add_argument("--model_version", type=str, help="model_version")
parser.add_argument("--compare_result", type=str, help="compare_result directory")

args = parser.parse_args()

print(f"Argument 1: {args.new_model_location}")
print(f"Argument 2: {args.prod_model_location}")
print(f"Argument 3: {args.model_version}")
print(f"Argument 4: {args.compare_result}")

if not (args.compare_result is None):
	os.makedirs(args.compare_result, exist_ok=True)
	print(f"{args.compare_result} created")
