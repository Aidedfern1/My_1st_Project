import argparse

parser = argparse.ArgumentParser(description="Welcome to this Argparse practice exercise")

parser.add_argument("floats", type= float, nargs="+", help= "Give a float to operate")
parser.add_argument("-s","--sum", dest= "accumulate", action= "store_const", const= sum, default= min, help="sum the numbers (default: find the min)" )
#parser.add_argument("-rd","--round",dest= "substraction", action="store_const", const=round(0), help="round a given value")

args= parser.parse_args()
print(args.accumulate(args.floats))
#print(args.substraction(args.floats))