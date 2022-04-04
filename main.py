import os
import subprocess
#from Bio import SeqIO


# Downloads assembly sequences from accession numbers in accessions.txt
def grab_datasets():
    # Change directory to home directory
    os.chdir(os.path.expanduser("~"))

    # accessions.txt must be in your home directory with your desired genome accession numbers or bioproject accession numbers
    # Assign accession numbers from accessions.txt to 'accession' variable (assemblies or bioprojects)
    with open('accessions.txt', 'r') as f_in:
        accession = f_in.read().strip()
    if not accession:
        print('No accession found')
        return
    # Make results directory and make it working directory
    os.system('mkdir results')
    os.chdir(os.path.expanduser("~/results"))

    # Download genome seqeuences of given accession numbers
    data_set_command = 'datasets download genome accession ' + accession + ' --filename ncbi_datasets_test.zip --exclude-genomic-cds --exclude-gff3 --exclude-protein --exclude-rna'
    print('Downloading genomes from NCBI')
    os.system(data_set_command)
    os.system('unzip ncbi_datasets_test.zip')
    os.chdir('ncbi_dataset/data')

    # Make directory to hold all sequences
    os.system('mkdir all_sequences')

    # Move all sequences to all_sequences
    os.system('mv GCF*/*.fna all_sequences')

    # Concatenate all sequences into one fna file
    os.chdir('all_sequences')
    os.system('cat *.fna > assemblies.fna')

    # # Parse out all contigs < 20000 bp in length
    # print('Parsing out all contigs less than 20000 bp in length')
    # with open('assemblies.fna', 'r') as f_i:
    #     all_assemblies = list(SeqIO.parse(f_i, 'fasta'))
    #
    # usable_assemblies = []
    # for s in all_assemblies:
    #     if len(s.seq) >= 20000:
    #         usable_assemblies.append(s)
    #
    # with open('parsed_assemblies.fna', 'w') as f_o:
    #     SeqIO.write(usable_assemblies, f_o, 'fasta')


grab_datasets()


# Run downloaded assemblies through Phigaro
def runPhigaro():
    os.chdir(os.path.expanduser("~"))

    # Create docker container for phigaro image named 'phigaro_tool'
    print('Creating Docker Container for Phigaro (phigaro_usage)')
    runPhigaro_command = 'sudo docker create -it --name phigaro_usage phigaro'
    os.system(runPhigaro_command)

    # Assign the container ID to variable 'container_ID' and copy the previously downloaded assemblies to directory 'test_data' in the docker container 'phigaro_usage'
    container_ID = subprocess.check_output('sudo docker ps -aqf "name=phigaro_usage"', shell=True).strip().decode(
        'utf-8')
    print('Copying Genomes to Docker Container')
    os.system('sudo docker cp ' + os.path.expanduser(
        '~/results/ncbi_dataset/data/all_sequences/assemblies.fna') + ' ' + container_ID + ':/test_data')

    # Run genome assemblies through Phigaro to identify prophages
    print('Running Phigaro with Genome Sequences')
    os.system('sudo docker start phigaro_usage')
    os.system(
        'sudo docker exec phigaro_usage sh -c "cd root && miniconda3/bin/phigaro -f /test_data/assemblies.fna -o results -p -e tsv gff html --not-open -d --save-fasta"')

    # Copy Phigaro output to results folder on host machine, close the docker container 'phigaro_tool'
    print('Copying Identified Prophages from Docker Container to Results')
    os.system('sudo docker cp ' + container_ID + ':/root/results/. ' + os.path.expanduser('~/results'))
    os.system('sudo docker stop phigaro_usage')
    print('Finished!')


runPhigaro()