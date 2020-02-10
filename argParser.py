import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val")
parser.add_argument("-fr", required=False)
parser.add_argument("-to", required=True)
args = parser.parse_args() 