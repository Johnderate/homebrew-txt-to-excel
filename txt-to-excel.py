#!/usr/bin/env python3
import sys
import argparse
import glob
from openpyxl import Workbook
import re
import time

version = "1.0.0"

args = None
workbook = Workbook()
worksheet = workbook.active

def main():
    setup_arguments()

    setup_worksheet()
    
    if (sys.stdin.isatty()):
        # No input from stdin, read whole directory
        process_directory()
    else:
        process_stdin()

# Process files
def process_directory():
    files = glob.glob("**/*.txt", recursive=True) if args.use_recursion else glob.glob("./*.txt")
    process_files(files)

def process_stdin():
    raw_input = sys.stdin.readlines()
    input = []
    for line in raw_input:
        input.append(line.strip())

    process_files(input)

def process_files(files):
    print("Found {} files, getting to work.".format(len(files)))

    for index, file in enumerate(files, start=1):
        progress = round(index / len(files) * 100)

        if not args.verbose: print ("Progress: [{:<20}] {}%".format("–"*(round(progress/5)), progress), end="\r")
        process_file(index, file)

    workbook.save(args.filename)

    print("✅ Successfully imported {} files into {}".format(len(files), args.filename))

def process_file(index, file):
    if args.verbose: print("📝 Reading file Nr. {}, {:<40} ".format(index, file), end="", flush=True)
    
    with open(file, "r") as stream:
        data = stream.read()
    
    #global worksheet
    data_to = re.search("TO: (.+?)\n", data).group(1)
    data_from = re.search("FROM: (.+?)\n", data).group(1)
    data_subject = re.search("SUBJECT: (.+?)\n", data).group(1)
    data_message = re.search("\n\n.*$", data, re.DOTALL).group(0)
    worksheet.append([data_to, data_from, data_subject, data_message])

    if args.verbose: print("✅")

# Setup
def setup_arguments():
    usage_examples = '''Example usages:
    Make all files in this directory into an Excel file called "abc.xlsx":
        txt-to-excel.py --filename abc.xlsx

    Make all files in the current directory that include #Seenotrettung into an Excel file using grep:
        grep -rl "#Seenotrettung" . | txt-to-excel.py -f seenotrettung.xlsx
    '''

    parser = argparse.ArgumentParser(description="Process txt into an excel worksheet. If no input is specified, the current directory is searched for txt files.", epilog=usage_examples, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-r', dest="use_recursion", action="store_true", help="Search recursively, i.e. consider subdirectories. By default, the script only looks in the current directory.")
    parser.add_argument('-f', "--filename", nargs="?", dest="filename", default="output.xlsx", help="The filename for the output excel file. Default is 'output.xlsx'")
    parser.add_argument('-v', "--verbose", dest="verbose", action="store_true", help="Print the progress and other useful info.")
    parser.add_argument('--version', action='version', version="Program version: {}".format(version))

    global args
    args = parser.parse_args()

def setup_worksheet():
    # Set titles for our Columns
    worksheet["A1"] = "To"
    worksheet["B1"] = "From"
    worksheet["C1"] = "Subject"
    worksheet["D1"] = "Text"
    

if __name__ == "__main__":
    main()