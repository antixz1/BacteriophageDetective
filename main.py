import os

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

grab_datasets()

#assuming Phigaro and docker are installed
def runPhigaro():
    os.chdir(os.path.expanduser("~"))
    runPhigaro_command = 'sudo docker run -it --name phigaro_tool phigaro'
    os.system(runPhigaro_command)

runPhigaro()

