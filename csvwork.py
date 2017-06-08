import csv
with open('csvs/ripper.csv', 'r') as csvfile:
        our_reader = csv.reader(csvfile)
        names = [row for row in our_reader]
# with open("csvs/ripper.csv", "w") as fout:
#     csvwriter = csv.writer(fout)
#     csvwriter.appendrow([0, "ID", "filename", "journal", "date", "full_text"])
# names.append(new_row)
# names.reverse()
# print(names[0])
# full_text = [row[4] for row in names]
dates = [row[3] for row in names]
# print(dates)
earliest = dates[0]
for date in dates:
    if date < earliest:
        earliest = date
print(earliest)
# with open("csvs/ripper.csv", "w") as fout:
# #     csvwriter = csv.writer(fout)
#
