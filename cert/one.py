import csv
Qsec, Qlev, Qagy, Qtst = set(), set(), set(), set()
with open('tst1.csv') as f:
  reader = csv.reader(f, delimiter=',')
  next(reader, None)
  for i, row in enumerate(reader):
    if i == 0: print(row)
    Qsec.add(row[0])
    Qlev.add(row[1])
    Qagy.add(row[2])
    Qtst.add(row[3])
  print(Qsec)

