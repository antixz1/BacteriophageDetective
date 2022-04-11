import os
import glob

def grab_datasets():
    #Change directory to home directory
    os.chdir(os.path.expanduser("~"))

    #accessions.txt must be in your home directory with your desired genome accession numbers or bioproject accession numbers
    #Assign accession numbers from accessions.txt to 'accession' variable (assemblies or bioprojects)
    with open('accessions.txt','r') as f_in:
        accession = f_in.read().strip()

    #Make results directory and make it working directory
    os.system('mkdir results')
    os.chdir(os.path.expanduser("~/results"))

    #Download genome seqeuences of given accession numbers
    data_set_command = 'datasets download genome accession '+accession+' --filename ncbi_datasets_test.zip --exclude-genomic-cds --exclude-gff3 --exclude-protein --exclude-rna'
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


#Run downloaded assemblies through Phigaro
def runPhigaro():
    os.chdir(os.path.expanduser("~"))
    #Run genome assemblies through Phigaro to identify prophages
    if glob.glob('results/input/*f*a'):
        print('Running Phigaro')
        os.system('phigaro -f '+glob.glob('results/input/*f*a')[0]+' -o results/phigaro_output -p -e tsv gff html -d --not-open --save-fasta')
    elif glob.glob('results/ncbi_dataset/data/all_sequences/assemblies.fna'):
         print('Running Phigaro')
         os.system('phigaro -f results/ncbi_dataset/data/all_sequences/assemblies.fna -o results/phigaro_output -p -e tsv gff html -d --not-open --save-fasta')
    else:
        print('Input files not found in results/input or in results/ncbi_dataset.')

    if glob.glob('results/phigaro_output/*.phigaro*'):
        print('Phigaro has finished running.')
    else:
        print('Phigaro run has failed.')
runPhigaro()        


