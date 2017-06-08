import csv
with open('csvs/ripper.csv', 'r') as csvfile:
         our_reader = csv.reader(csvfile)
         names = [row for row in our_reader]

with open("csvs/ripper.csv", "w") as fout:
    column_headers = ["text id", "filename", "jounal", "pub date", "full text"]
    names.append(column_headers)
print(names[0])
