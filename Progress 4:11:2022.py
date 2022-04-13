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
__________________________________________________
            

