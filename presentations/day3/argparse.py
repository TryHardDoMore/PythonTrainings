import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--int1", dest="int1", type=int)
parser.add_argument("--int2", dest="int2", type=int)
parser.add_argument('sum', type=bool, default=False, required=False)
parser.add_argument('cont', type=bool, default=False, required=False)

args = parser.parse_args()

if args.sum:
    print args.int1 + args.int2
elif args.cont:
    print args.int1 * args.int2
