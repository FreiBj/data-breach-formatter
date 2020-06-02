
# Data Breach Formatter
A simple tool initially created to format username and password lists for use with [Shard](https://github.com/philwantsfish/shard).

**Only use in coherence with Shard when using your own information.**

## How it formats 📝 Input & Output

This script takes the format
```
username:password\n
```

It will create a output file where the first variable and the second variable will be surrounded by quotation marks, separated by a colon and a newline wrap on the end of every line.

```
"username":"password"\n
```

## Running the script

The script takes two arguments, the file you want to format, and the name of the output file you want your formatted data to be written to.

```
$ python3 formatter.py --help
usage: formatter.py [-h] --file FILE --outputFile OUTPUTFILE

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE
  --outputFile OUTPUTFILE, -o OUTPUTFILE
```

You could either run the script with Python version 2.7 or later.  Run with Python3 for the best compatibility.
```
$ python3 formatter.py -f filename.txt -o output.txt
```

The formatted data will be in your specified file, and will be ready to directly test with Shard.

```
$ java -jar shard-1.5.jar -f output.txt
```