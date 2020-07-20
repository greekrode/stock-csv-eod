import os.path
import csv

data_file_name = input("Enter the file name: ")

reader = csv.DictReader(open(os.path.expanduser("~/Downloads/" + data_file_name + ".csv"),"rt"), delimiter = ',')
for i, line in enumerate(reader):
    ticker = line['Ticker']
    path_name = os.path.expanduser("~/Downloads/EOD Data/" + ticker + ".csv")
    if os.path.exists(path_name):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
    file = open(path_name, append_write, newline = '')
    writer = csv.writer(file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    writer.writerow([ ticker, line['Date/Time'], line['Open'], line['High'], line['Low'], line['Close'], line['Volume(Unit)'] ])
