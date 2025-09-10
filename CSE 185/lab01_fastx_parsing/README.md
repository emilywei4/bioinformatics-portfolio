# Lab 1 — FASTA/FASTQ Parsing & Basic Metrics

**Goal**  
Practice direct parsing of FASTA/FASTQ files and compute simple metrics:
- GC% per FASTA record
- Count number of reads in a gzipped FASTQ
- Estimate mean read length from a gzipped FASTQ

**Why it matters**  
These basics show how sequencing data is structured on disk and build intuition for downstream analysis.

---

## Files
- `gc_content.py` — Parse multi-line FASTA and print `ID,GC_percent` for each record.
- `fastq_count.py` — Count reads in a `*.fastq.gz` by counting `+` separator lines.
- `mean_readlen.sh` — Estimate mean read length from `*.fastq.gz` (assumes 4-line FASTQ records).
- `sample.fa` — Tiny FASTA for testing.

---

## Usage

### 1) GC% per FASTA record
```bash
python gc_content.py sample.fa
seq1,60.00
seq2,50.00

python fastq_count.py sample.fastq.gz
2

bash mean_readlen.sh sample.fastq.gz
151.37
