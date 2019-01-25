import argparse

print("In publish.py")
print("As a data scientist, this is where I use my training code.")

parser = argparse.ArgumentParser("train")


parser.add_argument("--pipeline_param", type=int, help="pipeline_parama")

args = parser.parse_args()

print(f"Argument 1: {args.pipeline_param}")