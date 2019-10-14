def problem3_7(csv_pricefile, flower):
    import csv
    fin = open(csv_pricefile)
    for row in csv.reader(fin):
        if row[0] == flower:
            print(row[1])
            break
    fin.close()
