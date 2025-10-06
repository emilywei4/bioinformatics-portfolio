# FASTA/FASTQ Parsing & Basic Metrics

**Problem**  
How can we directly parse FASTA/FASTQ files to compute core sequencing metrics such as GC content, read count, and average read length?

**Approach**  
These scripts demonstrate simple file-based operations for understanding raw sequencing data formats.  
They calculate GC% for each FASTA record, count reads in gzipped FASTQ files, and estimate mean read length.

---

## Files
- `gc_content.py` — Parse multi-line FASTA and print `ID,GC_percent` for each record.  
- `fastq_count.py` — Count reads in a gzipped FASTQ by identifying `+` separator lines.  
- `mean_readlen.sh` — Estimate mean read length from gzipped FASTQ (assumes 4-line FASTQ records).  
- `sample.fa` — Example FASTA for testing.  

---

## Usage

```bash
# Compute GC% per FASTA record
python gc_content.py sample.fa
seq1,60.00
seq2,50.00

# Count reads in FASTQ
python fastq_count.py sample.fastq.gz
2

# Estimate mean read length
bash mean_readlen.sh sample.fastq.gz
151.37
