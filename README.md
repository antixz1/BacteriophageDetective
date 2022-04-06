# BacteriophageDetective

# Introduction
This is a Linux-based python wrapper for a pipeline that takes in a collection of bacterial genomes to identify any prophages. The prophages are then annotated and analyzed.

## What are Bacteriophages?
Bacteriophages are viruses that infect Bacteria and Archaea. Phages can survive by integrating into the genome of their bacterial host throughout the lytic or lysogenic cycles. The majority of microorganisms carry phages. In our bodies, there are more phages than human or bacterial cells combined.

# Installation/Dependencies

## Docker
Docker is a free and open platform for developing, deploying, and running software. Docker isolates your applications from your infrastructure, allowing you to deliver software quickly. On this platform, you can manage your infrastructure the same way you manage your applications. Docker lets you package and run an application within a container, which is a loosely isolated environment.

This Docker container contains all required dependencies for this pipeline, as well as the pipeline script (main.py). 

To build the docker image, first clone the repository using
```
git clone https://github.com/antixz1/BacteriophageDetective
```

Next, build the image using
```
sudo docker build BacteriophageDetective --tag phagedetective:latest
```


## NCBI Datasets
The National Center for Biotechnology Information is a division of the National Institutes of Health's National Library of Medicine. The United States government has approved and sponsored it. The National Center for Biotechnology Information (NCBI) holds a number of databases pertinent to biotechnology and biomedicine, as well as bioinformatics tools and services. It includes the GenBank nucleic acid sequence database and the PubMed database of citations and abstracts for published life science journals, among other online resources for biological knowledge and data.

NCBI Datasets is a new resource that makes it simple to obtain information from many NCBI databases. Gene, transcript, protein, and genome sequences, as well as annotation and metadata, may be found and downloaded.

## Phigaro
Phigaro is a command-line tool that uses raw genome and metagenome assemblies as input to detect prophage areas. It also generates annotated 'prophage genome maps' and highlights potential transposon insertion sites inside prophages. It may be used to search for prophage areas in huge metagenomic datasets.

# Running the Pipeline

