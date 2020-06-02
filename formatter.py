# with open("test.txt", "r") as myfile:
#     text=myfile.read()

# output_text = text.split(" ")

# with open("Output.txt", "w",) as outfile:
#     for line in output_text:
#         outfile.write('"'+ line + '"')

# s = "username:password"
# s2 ="wolfdo65gtornado:salmontiger223"
# result = "".join(itertools.takewhile(lambda x : x!=':' , s))
# result2 = "".join(itertools.takewhile(lambda y : y=="!", s2))

# text ="username:password"
# left_text = text.partition(":")[0]

# left_text = None

# print(left_text)

import itertools
import sys
import os


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument("--outputFile", "-oF", type=str, required=True)
args = parser.parse_args()

# Opens a output file
outF = open(args.outputFile, "w")


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
        outF.write(format + "\n")
        print(format)
        
        # f.write(format + "\n")
        line = f.readline().splitlines()
        
        # print(format, end='')
        # f.write(format)
     
    f.close()
    # while line != '':  # The EOF char is an empty string
    #     # line.split(':')
    #     # print(line.split(':'), end='"')
    #     # line = reader.readline()
        
        
    #     # format = '"' + username + '"' + semicolon + '"' + password + '"'
    #     print(x)
    #     print(format, end="")
    #     line = f.readline()
    
# function