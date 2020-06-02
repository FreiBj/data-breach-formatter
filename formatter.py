import itertools
import sys
import os


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument("--outputFile", "-o", type=str, required=True)
args = parser.parse_args()

# Opens a output file
outputFile = open(args.outputFile, "w")


with open(args.file, 'r+') as f:
    # Read and print the entire file line by line
    line = f.readline().splitlines()
    
    for line in f:
        # Remove the \n on the end of every line
        line = line.strip()
        
        username = line.partition(":")[0]
        semicolon = line.partition(":")[1]
        password = line.partition(":")[2]
        
        format = '"' + username + '"' + semicolon + '"' + password + '"'
        outputFile.write(format + "\n")
        
        line = f.readline().splitlines()
     
    f.close()
