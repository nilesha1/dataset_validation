#pip install pandas
#pip install Numpy
#if file is .xls then install xlrd, xlwt packages as well

import pandas as pd
import numpy as np

df1=pd.read_excel("C:\\Users\\Nilesh\\Documents\\Source.xls")
df2=pd.read_excel("C:\\Users\\Nilesh\\Documents\\Target.xls")

#1. Count validation
count_df1= len(df1)
count_df2= len(df2)

if len(df1) == len(df2):
    status="Match"
    print("1. Test Case Pass: count is same")
else:
    status="Count does not match"
    print("1. Test Case fail: count is not same")

count_df=pd.DataFrame({
    "Source_Count":count_df1,
    "Target_Count":count_df2,
    "Status": status}, index=[0])

count_df.to_excel("C:\\Users\\Nilesh\\Documents\\Count_Validation.xls")


#2.Duplicate validation
dup_df2= df2.duplicated().sum()
dup_df2_records = df2[df2.duplicated()]
dup_df2_records.to_excel("C:\\Users\\Nilesh\\Documents\\Duplicate_Validation.xls", index=False)

if dup_df2 > 0:
   print("2. Test Case Fail: Duplicate records are found in target table")
else:
    print("2. Test Case Pass: Duplicate records are not found in target table")



#3.Data Validation
print(df1.equals(df2))
comparevalues = df1.values == df2.values
print(comparevalues)

rows, cols = np.where(comparevalues==False)

#Generate report for unmatched data
for item in zip(rows,cols):
	df1.iloc[item[0],item[1]] ='{}---->{}'.format(df1.iloc[item[0],item[1]], df2.iloc[item[0],item[1]])

df1.to_excel("C:\\Users\\Nilesh\\Documents\\Data_Validation.xls", index= False, header= True)




