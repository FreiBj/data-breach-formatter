# Data Breach Formatter
A simple tool initially created to format username and password lists for Shard


#### To get started, clone this repository and cd into it

Run this to format the file you want

Default format is

'''
username:password
'''

It will generate a output file where the two seperated variables will be converted into a string.

'''
"username":"password"\n
'''


'''
$ python3 formatter.py -f filename.txt -oP output.txt
'''
