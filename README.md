# ProphageDetective

# Introduction
This is a Linux-based python wrapper for a pipeline that takes in a collection of bacterial genomes to identify any prophages. The prophages are then annotated and analyzed.

## What are Phages?
Phages are viruses that infect Bacteria and Archaea. Phages can survive by integrating into the genome of their bacterial host throughout the lytic or lysogenic cycles. The majority of microorganisms carry phages. In our bodies, there are more phages than human or bacterial cells combined. Prophages follow the lysogenic path, integrating their DNA within bacterial DNA in a dormant state.

# Installation/Dependencies

## Docker
Docker is a free and open platform for developing, deploying, and running software. Docker isolates your applications from your infrastructure, allowing you to deliver software quickly. On this platform, you can manage your infrastructure the same way you manage your applications. Docker lets you package and run an application within a container, which is a loosely isolated environment.

This Docker container contains all required dependencies for this pipeline, as well as the pipeline script (main.py). 

To build the docker image, first clone the repository using
```
git clone https://github.com/antixz1/ProphageDetective
```

Next, build the image using
```
sudo docker build ProphageDetective --tag prophagedetective:latest
```

Finally, create a Docker container with the prophagedetective image using
```
sudo docker create -it --name [container name] prophagedetective
sudo docker start -i [container name]
```
or start the interactive session automatically using
```
sudo docker run -it --name [container name] prophagedetective
```
where 'container name' is any user-given name.


## NCBI Datasets
The National Center for Biotechnology Information is a division of the National Institutes of Health's National Library of Medicine. The United States government has approved and sponsored it. The National Center for Biotechnology Information (NCBI) holds a number of databases pertinent to biotechnology and biomedicine, as well as bioinformatics tools and services. It includes the GenBank nucleic acid sequence database and the PubMed database of citations and abstracts for published life science journals, among other online resources for biological knowledge and data.

NCBI Datasets is a new resource that makes it simple to obtain information from many NCBI databases. Gene, transcript, protein, and genome sequences, as well as annotation and metadata, may be found and downloaded.

## Phigaro
Phigaro is a command-line tool that uses raw genome and metagenome assemblies as input to detect prophage areas. It also generates annotated 'prophage genome maps' and highlights potential transposon insertion sites inside prophages. It may be used to search for prophage areas in huge metagenomic datasets.

## VOG Table
VOGTable.tsv is a tab delimited value file detailing the functional attributes for each pVOG along with additional information. This file is included within the installation package and will be placed into one's home/working directory. This file allows the pipeline to identify the functional attributes present to each accession as identified by Phigaro. 

# Pipeline Usage
## Input
### Using NCBI Assemblies
The pipeline can download and run assemblies automatically with user-provided accession IDs. The accessions.txt file in the 'accessions' folder should be edited to contain any number of accessions, separated by spaces, in order to run successfully. Bioproject accessions can also be used to download entire bioproject assemblies.
### Using fasta/fna Files
The pipeline also accepts fasta/fna files as opposed to NCBI assembly accessions. **The accessions.txt file must be empty for the pipeline to run with user-input fasta/fna files.** 
Files can be copied to the Docker container using
```
sudo docker cp [file path] [container name]:/root/accessions
```

## Output
All output can be found in the results directory:

***phigaro.fasta:*** Contains sequences for all identified prophages in fasta format

***phigaro.tsv:*** Contains prophage coordinates within their respective scaffolds, transposability, taxonomy, and all detected VOGs

***phigaro.gff3:*** Contains prophage coordinates within their respective scaffolds, as well as gene information for each prophage

***phigaro.html:*** Interactive webpage to visualize prophages and their gene content

***bpalign.csv:*** Contains BLASTn results determining prophage similarity among different scaffolds

***VOGAnnotations.tsv:*** Contains annotated VOGs by scaffold

***Prophage_count.csv:*** Contains the number of prophages identified in each bacterial genome

## Running the Pipeline

## Limitations
- Phigaro tosses out contigs that are less than 20,000 bp long
- The VOG annotation database is a work in progress and may not provide annotations for all pVOGs found by Phigaro
