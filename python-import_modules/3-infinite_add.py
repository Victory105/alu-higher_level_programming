#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name itself
    total = sum(map(int, args))
    print(total)
