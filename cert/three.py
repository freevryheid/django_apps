import os
import pandas as pd

class Qual:
  args = '<foo bar ...>'
  help = 'our help string comes here'

  def add_qualification_agency(self, df):
    Qagy = list(df.apply(set)[2])
    for agy in Qagy:
      a = QualificationAgency(agency=agy)
      print(a)

  def add_qualification_level(self, df):
    Qagy = list(df.apply(set)[2])
    for agy in Qagy:
      Qlev = list(df['QLEV'][df['QAGY']==agy])
      for lvl in Qlev:
        a = QualificationAgency.objects.get(agency=agy)
        l = QualificationLevel(level=lvl, agency=a)
        l.save()

  def add_qualification_test(self, df):
    Qlev = list(df.apply(set)[1])
    for lev in Qlev:
      Qtst = list(df['QTST'][df['QLEV']==lev])
      for tst in Qtst:
        l = QualificationLevel.objects.get(level=lev)
        t = QualificationTest(test=tst, level=l)
        t.save()

if __name__ == "__main__":
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  certs = pd.read_csv(os.path.join(__location__, 'certs.csv'))
  q =Qual()
  q.add_qualification_agency(certs)
  # q.add_qualification_level(certs)
  # q.add_qualification_test(certs)


