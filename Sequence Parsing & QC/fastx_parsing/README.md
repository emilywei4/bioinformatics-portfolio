# FASTA/FASTQ Parsing & Basic Metrics

**Problem**  
How can we directly parse FASTA/FASTQ files to compute core sequencing metrics such as GC content, read count, and average read length?

**Approach**  
These scripts demonstrate simple file-based operations for understanding raw sequencing data formats.  
They calculate GC% for each FASTA record, count reads in gzipped FASTQ files, and estimate mean read length.

---

## Files
- **Pipeline drivers (documented commands below)**  
  - GC content per FASTA record (`gc_content.py`)  
  - FASTQ read counting via Python (`fastq_count.py`)  
  - FASTQ read counting via `zcat` (`fastq_count_zcat.sh`)  
  - Mean read length estimation (`mean_readlen.sh`)  

---

## Usage

```bash
Here, we use an example FASTA file called `sample.fa`:

>seq1
ATGCATGCATGC
>seq2
ATGCGCGTAA
EOF

# Compute GC% per FASTA record
python gc_content.py sample.fa
seq1,50.00
seq2,60.00

# Count reads in gzipped FASTQ (Python version)
python fastq_count.py sample.fastq.gz
2

# Count reads in gzipped FASTQ (zcat + grep version)
bash fastq_count_zcat.sh sample.fastq.gz
2

# Estimate mean read length
bash mean_readlen.sh sample.fastq.gz
151.37
