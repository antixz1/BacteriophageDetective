Phigaro can be run in one of three modes:

1. *basic* (default)

2. *abs*

3. *without_gc*

 For this project, only the basic mode was used (basic mode is set by default). The commands to run the other two modes will be shown below. For more information on Phigaro modes, refer to https://github.com/bobeobibo/phigaro/

---

Running Phigaro in *abs* mode using previous command example from `/test_data/Bacillus_anthracis_str_ames/README_phig_test_data.md`: 

```
$ phigaro -f /test_data/Bacillus_anthracis_str_ames.fna -o test_data/Bacillus_anthracis_str_ames -p --not-open --save-fasta -e tsv -m abs
```

Running Phigaro in *without_gc* mode using previous command example from `/test_data/Bacillus_anthracis_str_ames/README_phig_test_data.md`:

```
$ phigaro -f /test_data/Bacillus_anthracis_str_ames.fna -o test_data/Bacillus_anthracis_str_ames -p --not-open --save-fasta -e tsv -m without_gc

```

---

Phigaro can also output different file types after conducting its analyses. Its output can be in the form of an html, tsv, gff, bed, or stdout file type. The default file type is html. 

In order to specify Phigaro produce multiple file types as its output, use a space as a separator with the [-e EXTENSION] flag. Ex: `-e tsv html gff bed stdout`

Using the same command example as above (`/test_data/Bacillus_anthracis_str_ames/README_phig_test_data.md`), and assuming the use of the *basic* mode, one could specify phigaro produce all of the file types it is capable of with this block of code: 

```
$ phigaro -f /test_data/Bacillus_anthracis_str_ames.fna -o test_data/Bacillus_anthracis_str_ames -p --not-open --save-fasta -e tsv html gff bed stdout
```

 











