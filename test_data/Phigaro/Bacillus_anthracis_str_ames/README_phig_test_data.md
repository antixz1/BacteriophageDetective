Running Phigaro with test_data from installation 

Copying directory with phigaro successfully installed via docker

This command will take the user back one directory and then into the msaban directory containing phigaro already successfully installed.

```
$ cd ..
$ cd msaban
```

This command will copy the phigaro directory stored in the msaban directory:

```
$ cp -R phigaro ~
```

This command will list all of the files in the current working directory (should see phigaro if done correctly):

```
$ ls

accessions.txt  phigaro         Software
datasets.py     README.md       test_data
miniconda3      results         test_PHANOTATE
PHANOTATE       sequence.fasta  Test.py
```

```
$ cd
$ pwd

/home/atruckenbrod

$ sudo docker build --tag phigaro:latest phigaro

successfully built 669daa6
successfully tagged phigaro:latest

$ ls 

phigaro
```

Now, the phigaro docker container is within your user directory within the remote machine. Next, we need to initialize the docker container with phigaro (note: this only needs to be done once): 

- [phigaro_container] is the [container name] and can be anything you choose. Here, the docker container name is 'phigaro_container'

```
$ sudo docker run -it --name phigaro_container phigaro
```

Now, in order to finish the initialization of the docker container, we need to access or open the newly created docker container, which can be done by using this command:

- [-i] in the code below is for initialization purposes and only needs to be done the first time

- In future sessions, leave out the [-i] flag, and this will open the docker container you created. For this demonstration, the docker container is named [phigaro_container]. Line 2 in the code block below shows what this would look like

```
$ sudo docker start -i phigaro_container

$ sudo docker start phigaro_container
```

Now, the phigaro docker container [phigaro_container] is open and ready to be used. Here, we will run phigaro on the test_data that comes with the installation to ensure that it is installed correctly and working properly (note: phigaro must be run within the *root *directory)

```
$ phigaro -f /test_data/Bacillus_anthracis_str_ames.fna -o test_data/Bacillus_anthracis_str_ames -p --not-open --save-fasta -e tsv
```

After running phigaro on this test data, we can see 2 newly created files within the /Bacillus_anthracis_str_ames directory: 

- These 2 newly created files are the output of phigaro, which can be modified/changed to suit your needs (see phigaro documentation for more information on possible output files from phigaro)

```
$ cd /test_data/Bacillus_anthracis_str_ames/

$ ls

Bacillus_anthracis_str_ames.fasta  Bacillus_anthracis_str_ames.phigaro.tsv

$ exit
```

Copying and pasting the two output files of phigaro to personal directory on virtual machine:

```
$ sudo docker ps
```

The command shown above will show all of the currently running docker containers with their respective ID numbers and Image Names.

If your container does not show up, you likely need to re-open it or 'start it' again with:

```
$ sudo docker start phigaro_container

phigaro_container

$ sudo docker ps
```

Copying the two output files of phigaro to my personal directory on remote machine:

(note: '/home/atruckenbrod' is the destination of where the output files are being copied to. This needs to be changed to where *you* want the output to go on *your*  machine.)

```
$ sudo docker cp 19aa9638653e:/root/test_data/ /home/atruckenbrod

$ ls

phigaro  test_data
```


