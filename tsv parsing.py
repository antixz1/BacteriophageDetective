import numpy as np
import pandas as pd
from csv import writer
#importing numpy, pandas, and csv writer

df = pd.read_csv('/Users/rmansoor/Downloads/parsed_assemblies.phigaro.tsv', sep='\t', usecols = ['scaffold','vog'])
var = df.scaffold.unique()
    
mydict = {} #dictionary to count occurrences
#loop over scaffolds
for i in var:
    i = i[:9]
    #test if scaffold is already in dict, if so add to count
    if i in mydict:
        mydict[i] = mydict[i] + 1
    #otherwise add scaffold to dictionary with count 1
    else:
        mydict[i] = 1

for k, v in mydict.items():
    print(str(k) + ' ' + str(v) + '\n')









# # for i in var:
# #     letters = i[:10]
# #     print(letters)

# print(df)
# for i in df.loc(scaffold):
#     print(i)
