import glob
import pandas as pd
f = glob.glob("*.xlsx")

excel_files = glob.glob('Data/*.xlsx')  # assume the path
for excel in excel_files:
    for i in range(4):
        # if only the first sheet is needed.
        df = pd.read_excel(excel, sheet_name=i)
        out = excel.split('.')[0]+'{}.csv'.format(i)
        df.to_csv(out)
