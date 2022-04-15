import os
import glob
import csv
import pandas


os.chdir(os.path.expanduser("~"))
os.mkdir('results')
###########################################################################################################################################################################################
def grab_datasets():
    #accessions.txt must be in your home directory with your desired genome accession numbers or bioproject accession numbers
    os.chdir(os.path.expanduser("~/results"))

    #Download genome seqeuences of given accession numbers
    data_set_command = 'datasets download genome accession --inputfile /root/accessions/accessions.txt --filename ncbi_datasets.zip --exclude-genomic-cds --exclude-gff3 --exclude-protein --exclude-rna'
    os.system(data_set_command)
    os.system('unzip ncbi_datasets.zip')
    os.chdir('ncbi_dataset/data')

    #Make directory to hold all sequences
    os.system('mkdir all_sequences')

    #Move all sequences to all_sequences
    os.system('mv GCF*/*.fna all_sequences')

    #Concatenate all sequences into one fna file
    os.chdir('all_sequences')
    os.system('cat *.fna > assemblies.fna')
###########################################################################################################################################################################################

#Check for user-input accessions in accessions.txt or for user-input-fasta/fna files in accessions directory
with open('accessions/accessions.txt','r') as f_in:
    accession = f_in.read().strip()
if accession:
    grab_datasets()
else:
    if glob.glob('accessions/*.fasta') or glob.glob('accessions/*.fna'):
        os.chdir('results')
        os.mkdir('input')
        os.chdir(os.path.expanduser("~"))
        os.system('cp accessions/*f*a results/input/')
    else:
        print('Error: User input not found. Please palce desired accessions in "accessions.txt" or place a fasta/fna file in the "accessions" directory.')
###########################################################################################################################################################################################

#Run downloaded assemblies through Phigaro
def runPhigaro():
    mode = 'basic' #'abs' and 'without_gc' other usable modes
    os.chdir(os.path.expanduser("~"))
    #Run genome assemblies through Phigaro to identify prophages
    if glob.glob('results/input/*f*a'):
        print('Running Phigaro')
        os.system('phigaro -f '+glob.glob('results/input/*f*a')[0]+' -o results/phigaro_output -p -e tsv gff html -d --not-open --save-fasta -m '+mode)
    elif glob.glob('results/ncbi_dataset/data/all_sequences/assemblies.fna'):
        print('Running Phigaro')
        os.system('phigaro -f results/ncbi_dataset/data/all_sequences/assemblies.fna -o results/phigaro_output -p -e tsv gff html -d --not-open --save-fasta -m '+mode)
    else:
        print('Input files not found in results/input or in results/ncbi_dataset.')

    if glob.glob('results/phigaro_output/*.phigaro*'):
        print('Phigaro has finished running.')
    else:
        print('Phigaro run has failed.')
        
runPhigaro()
###########################################################################################################################################################################################

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
########################################################################################################################################################################
def align_prophage():
    os.chdir(os.path.expanduser("~"))
    os.system('makeblastdb -in results/phigaro_output/*.phigaro.fasta -dbtype nucl -out results/phigaroblastdb/phigarodb')
    os.system('blastn -query results/phigaro_output/*.phigaro.fasta -db results/phigaroblastdb/phigarodb -out results/bpalign.csv -outfmt "10 qseqid sseqid pident qcovhsp" -max_hsps 1')

    with open('results/bpalign.csv','r') as b_in:
        reader = csv.reader(b_in)
        alignments = []
        for row in reader: 
            alignments.append(row)
    
    qcov_threshold = 75 #can be altered.
    parsed_alignments = []
    
    for a in alignments:
        if a[0] != a[1] and int(a[3]) > qcov_threshold:
            parsed_alignments.append(a)
    
    header = ['qseqid','sseqid','pident','qcovhsp']
    with open('results/bpalign.csv','w') as b_out:
        writer = csv.writer(b_out)
        writer.writerow(header)
        writer.writerows(parsed_alignments)

align_prophage()
###########################################################################################################################################################################################

VOG_dict = {}
Phigaro_dict = {}
Final_dict = {}
Final_dict_values = list()

def VOG_identifier(infile1, infile2):
    with open(infile1, mode ='r') as inp:
        reader = csv.reader(inp, delimiter = "\t")
        VOG_dict = {rows[0]:rows[6] for rows in reader}

    with open(infile2, mode = 'r') as inp:
        reader = csv.reader(inp, delimiter = "\t")
        Phigaro_dict = {rows[0]:rows[5] for rows in reader}
        for key, value in Phigaro_dict.items():
            value = list(value.split(", "))
            Phigaro_dict[key] = value

    del Phigaro_dict["scaffold"]

    for key, value in Phigaro_dict.items():
        for vog in value:
            if vog not in VOG_dict.keys():
                Final_dict_values.append(vog + " not annotated")
            else:
                Final_dict_values.append( vog + ": " + VOG_dict[vog])
        Final_dict[key] = Final_dict_values

    for key, value in Final_dict.items():
        print(key)
        print(value)

VOG_identifier('VOGTable.tsv', os.path.expanduser('~/results/phigaro_output/*.phigaro.tsv'))
###########################################################################################################################################################################################
