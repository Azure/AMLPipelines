import argparse
import os

print("In train.py: as a data scientist, this is where you should fill in your training code.")

parser = argparse.ArgumentParser("train")

parser.add_argument("--input_data", type=str, help="input data")
parser.add_argument("--output_train", type=str, help="output_train directory")

args = parser.parse_args()

print(f"Argument 1: {args.input_data}")
print(f"Argument 2: {args.output_train}")

if not (args.output_train is None):
	os.makedirs(args.output_train, exist_ok=True)
	print(f"{args.output_train} created")
