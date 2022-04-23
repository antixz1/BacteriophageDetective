import os
import glob
import csv
import pandas as pd

#Create results directory in root directory of docker container
os.chdir(os.path.expanduser("~"))
os.mkdir('results')


#Define Functions
###########################################################################################################################################################################################
#Grab genome assemblies from NCBI with user-input accessions
def grab_datasets():
    #accessions.txt must be in your home directory with your desired genome accession numbers or bioproject accession numbers
    os.chdir(os.path.expanduser("~/results"))

    #Download genome seqeuences of given accession numbers
    data_set_command = 'datasets download genome accession --inputfile /root/input/accessions.txt --filename ncbi_datasets.zip --exclude-genomic-cds --exclude-gff3 --exclude-protein --exclude-rna'
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
#Check for accessions or user-input genomes
def input_check():
    #Check for user-input accessions in accessions.txt or for user-input-fasta/fna files in accessions directory
    with open('input/accessions.txt','r') as f_in:
        accession = f_in.read().strip()
    if accession: #Grab assemblies using NCBI dataset if accessions are present in accessions.txt
        grab_datasets()
    else: #If accessions aren't present in accessions.txt, move any user-input fasta/fna files to the results directory for Phigaro to use
        if glob.glob('input/*.fasta') or glob.glob('input/*.fna'):
            os.chdir('results')
            os.mkdir('inputfile')
            os.chdir(os.path.expanduser("~"))
            os.system('cp input/*f*a results/inputfile/')
        else:
            print('Error: User input not found. Please palce desired accessions in "accessions.txt" or place a fasta/fna file in the "input" directory.')
         
###########################################################################################################################################################################################

#Run downloaded assemblies through Phigaro to identify and annotate prophages
def runPhigaro():
    mode = 'basic' #'abs' and 'without_gc' other usable modes
    
    os.chdir(os.path.expanduser("~"))
    #Run genome assemblies through Phigaro to identify prophages
    #Run with user-input files or with ncbi dataset files depending on which files are present
    if glob.glob('results/inputfile/*f*a'): 
        print('Running Phigaro')
        os.system('phigaro -f '+glob.glob('results/inputfile/*f*a')[0]+' -o results/phigaro_output -p -e tsv gff html -d --not-open --save-fasta -m '+mode)
    elif glob.glob('results/ncbi_dataset/data/all_sequences/assemblies.fna'):
        print('Running Phigaro')
        os.system('phigaro -f results/ncbi_dataset/data/all_sequences/assemblies.fna -o results/phigaro_output -p -e tsv gff html -d --not-open --save-fasta -m '+mode)
    else:
        print('Input files not found in results/input or in results/ncbi_dataset.')
    
    #Determine if Phigaro was successful in running
    if glob.glob('results/phigaro_output/*.phigaro*'):
        print('Phigaro has finished running.')
    else:
        print('Phigaro run has failed.')

###########################################################################################################################################################################################
#Count # prophages based on genome
def prophage_count():
    df = pd.read_csv(glob.glob('/root/results/phigaro_output/*.phigaro.tsv')[0], sep='\t', usecols = ['scaffold','vog'])
    outfile = open('results/Prophage_count.csv','w') # creating a new csv file
    outfile.write("WGS,#Prophages\n")
    var = df['scaffold'].tolist()

    mydict = {} #dictionary to count occurrences
    #loop over wordlist
    for i in var:
        i = i[:11]
        #test if word is already in dict, if so add to count
        if i in mydict:
            mydict[i] = mydict[i] + 1
        #otherwise add word to dictionary with count 1
        else:
            mydict[i] = 1

    for k, v in mydict.items():
        outfile.write(str(k)+',' +str(v) + "\n")
    outfile.close()

########################################################################################################################################################################
#Determine prophage similarity among different bacterial genomes
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


###########################################################################################################################################################################################
#Add VOG annotation (from database) to pVOGs found by Phigaro
def VOG_annotator(infile1, infile2):
    Final_dict = {}
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
        Final_dict_values = list()
        for vog in value:
            if vog not in VOG_dict.keys():
                Final_dict_values.append(vog + " not annotated")
            else:
                Final_dict_values.append( vog + ": " + VOG_dict[vog])
        Final_dict[key] = Final_dict_values

    with open('results/VOGAnnotations.tsv','w') as out:
        for key, value in Final_dict.items():
            out.write(key + "\t")
            for vog in value:
                out.write(vog + "\t")
            out.write("\n")

###########################################################################################################################################################################################

#Call functions for pipeline
input_check()
runPhigaro()
prophage_count()
align_prophage()
VOG_annotator('VOGTable.tsv', glob.glob('/root/results/phigaro_output/*.phigaro.tsv')[0])
