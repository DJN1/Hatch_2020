import csv

for num in range(1, 21):

    txt_file = r"data/F{}.txt".format(num)
    csv_file = r"data/F{}.csv".format(num)
    with open(txt_file, "r") as in_text:
        in_reader = csv.reader(in_text, delimiter='\t')
        with open(csv_file, "w", newline='') as out_csv:
            out_writer = csv.writer(out_csv)
            for row in in_reader:
                out_writer.writerow(row)
