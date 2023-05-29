import argparse

parser = argparse.ArgumentParser(description="Welcome to this Argparse practice exercise")

parser.add_argument("floats", type= float, nargs="+", help= "Give a float to operate")
parser.add_argument("-s","--sum", dest= "accumulate", action= "store_const", const= sum, default= min, help="sum the numbers (default: find the min)" )

args= parser.parse_args()
print(args.accumulate(args.floats))