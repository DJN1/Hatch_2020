import csv

for num in range(1, 21):

    txt_file = r"data/F{}.txt".format(num)
    csv_file = r"data/F{}.csv".format(num)
    with open(txt_file, "r") as in_text:
        in_reader = csv.reader(in_text, delimiter='\t')
        with open(csv_file, "w", newline='') as out_csv:
            out_writer = csv.writer(out_csv)
            for i, row in enumerate(in_reader):
                if i == 0:
                    row[2] = row[2].split()[1]
                    row[3] = row[3].rstrip()
                    row[4] = row[4].split()[2]
                    row[5] = row[5].split()[0]
                out_writer.writerow(row)
