# BacteriophageDetective

# Introduction
This is a Linux-based python wrapper for a pipeline that takes in a collection of bacterial genomes to identify any prophages. The prophages are then annotated and analyzed.

## What are Bacteriophages?
Bacteriophages are viruses that infect Bacteria and Archaea. Phages can survive by integrating into the genome of their bacterial host throughout the lytic or lysogenic cycles. The majority of microorganisms carry phages. In our bodies, there are more phages than human or bacterial cells combined.

# Installation/Dependencies

## Docker
Docker is a free and open platform for developing, deploying, and running software. Docker isolates your applications from your infrastructure, allowing you to deliver software quickly. On this platform, you can manage your infrastructure the same way you manage your applications. Docker lets you package and run an application within a container, which is a loosely isolated environment.


## Phigaro
Phigaro is a command-line tool that uses raw genome and metagenome assemblies as input to detect prophage areas. It also generates annotated 'prophage genome maps' and highlights potential transposon insertion sites inside prophages. It may be used to search for prophage areas in huge metagenomic datasets.

### Docker Container
Build the latest Phigaro Docker container using
```
sudo docker build --tag phigaro:latest phigaro
```
Contains all required dependencies for Phigaro (Python3, Prodigal, HMMER, Locate)
