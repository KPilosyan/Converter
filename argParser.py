import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val", type = str.lower)
parser.add_argument("-fr", required=False, type = str.lower)
parser.add_argument("-to", required=True, type = str.lower)
args = parser.parse_args()

# TODO: make args lowercase 