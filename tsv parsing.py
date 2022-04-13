import numpy as np
import pandas as pd
from csv import writer
#importing numpy, pandas, and csv writer

df = pd.read_csv('/Users/rmansoor/Downloads/parsed_assemblies.phigaro.tsv', sep='\t', usecols = ['scaffold','vog'])
outfile = open('Parsed_tsv.csv','w') # creating a new csv file
outfile.write("Scaffold," + "Number of Scaffolds," + "\n")
var = df.scaffold.unique()
    
mydict = {} #dictionary to count occurrences
#loop over wordlist
for i in var:
    i = i[:9]
    #test if word is already in dict, if so add to count
    if i in mydict:
        mydict[i] = mydict[i] + 1
    #otherwise add word to dictionary with count 1
    else:
        mydict[i] = 1

for k, v in mydict.items():
    #print(str(k) + ' ' + str(v) + '\n')
    
    outfile.write(str(k)+ ',' +str(v)+ ',' +"\n")
outfile.close()

