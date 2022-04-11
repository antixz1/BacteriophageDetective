Code to BLAST FASTA Phigaro output against BLAST database made from FASTA Phigaro output

```python
def align_prophage
    os.chdir(os.path.expanduser("~"))
    os.system('makeblastdb -in results/phigaro_output/*.phigaro.fasta -dbtype nucl -out results/phigaroblastdb/phigarodb')
    os.system('blastn -query results/phigaro_output/*.phigaro.fasta -db results/phigaroblastdb/phigarodb -out results/bpalign.csv -outfmt "10 qseqid sseqid pident qcovhsp" -max_hsps 1')
```

Code to parse matches with query coverages <75 (this can easily be altered) and parse matches where query ID is the same as the subject ID

```python
    with open('results/bpalign.csv','r') as b_in:
        reader = csv.reader(b_in)
        alignments = []
    
        for row in reader: 
            alignments.append(row)
    
        qcov_threshold = 75 #can be altered.
        parsed_alignments = []
    
        for a in alignments:
            if a[0] != a[1] and int(a[3]) > qcovthreshold:
                parsed_alignments.append(a)
    
    header = ['qseqid','sseqid','pident','qcovhsp']
        with open('reseults/bpalign.csv','w') as b_out:
            writer = csv.writer(b_out)
            writer.writerow(header)
            writer.writerows(parsed_alignments)

    
```
