$ cd .. 
$ cd msaban # changing directory
$ cp -R phigaro ~ # copying phigaro to our own directory
$ sudo docker run -it --name phage_detective phagedetective
# running 
$ sudo docker start -i phage_detective
$ cd root 
$ ls
accessions.txt  main.py. miniconda3

$ Vim main.py
# the vim command is a text editing command

#To exit the text editor, please enter “:q” and the return command to return to your terminal screen

_____________________________________________
# To fetch files when Biopython is not working, please use the modified code below:
# Michael Saban modified our original code to this code to help troubleshoot issues with Biopython

import os

#Downloads assembly sequences from accession numbers in accessions.txt
def grab_datasets():
    #Change directory to home directory
    os.chdir(os.path.expanduser("~"))

    #accessions.txt must be in your home directory with your desired genome accession numbers or bioproject accession numbers
    #Assign accession numbers from accessions.txt to 'accession' variable (assemblies or bioprojects)
    with open('accessions.txt','r') as f_in:
        accession = f_in.read().strip()
    if not accession:
        print('No accession found')
        return
    #Make results directory and make it working directory
    os.system('mkdir results')
    os.chdir(os.path.expanduser("~/results"))

    #Download genome seqeuences of given accession numbers
    data_set_command = 'datasets download genome accession '+accession+' --filename ncbi_datasets_test.zip --exclude-genomic-cds --exclude-gff3 --exclude-protein --exclude-rna'
    print('Downloading genomes from NCBI')
    os.system(data_set_command)
    os.system('unzip ncbi_datasets_test.zip')
    os.chdir('ncbi_dataset/data')

    #Make directory to hold all sequences
    os.system('mkdir all_sequences')

    #Move all sequences to all_sequences
    os.system('mv GCF*/*.fna all_sequences')

    #Concatenate all sequences into one fna file
    os.chdir('all_sequences')
    os.system('cat *.fna > assemblies.fna')
        
grab_datasets()

#_____________________________________________

# Phigaro only accepts contigs greater than 20,000bp
#Code for 20,000 base pairs incase the “-d” command does not work:

seqs=[] # creating an empty lsit
data = SeqIO.parse(“path+Name_of_file.fasta” ,’fasta')
# we are reading this file in fasta format
for record in data:
    #for each record in the file
    if len(record.seq) > 20000:
        #if the len of the record is greater than 20,000 base pairs:
        seqs.append(record)
        #add the records to the list called seqs

longseqs = (“ str(len(seqs)) + " contigs > 20,000 in the assembly.")
#print the number of contigs greater than 20,000 in the assembly.
outfile.write(longseqs + " \n" + " \n")

SeqIO.write(seqs, “path+ seqs.fasta", "fasta")
#create a new file called "Long_seqs.fasta" in fasta format that will store all contigs greater than 20,000

