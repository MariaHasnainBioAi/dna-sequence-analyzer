# DNA Sequence Analyzer 🧬

## Project Overview

The DNA Sequence Analyzer is a beginner bioinformatics project developed using Python and Biopython. It analyzes a DNA sequence and calculates its length, nucleotide composition, GC content, reverse complement, and translated protein sequence.

## Project Objectives

- Calculate DNA sequence length.
- Count A, T, G, and C nucleotides.
- Calculate GC content as a percentage.
- Generate the reverse-complement sequence.
- Translate DNA into amino acids using Biopython.

## Technologies Used

- Python 3.14
- Biopython 1.88
- Visual Studio Code

## Installation

Install Biopython using:

```bash
python -m pip install biopython
```

## Features

### 1. DNA Sequence Analysis

The program analyzes an illustrative DNA sequence containing 120 nucleotides.

### 2. Nucleotide Composition

It counts the four DNA bases:

- Adenine (A): 31
- Thymine (T): 29
- Guanine (G): 32
- Cytosine (C): 28

### 3. GC Content

The program calculates GC content using:

GC content = ((G + C) / Total DNA length) × 100

For this sequence, GC content is 50.0%.

### 4. Reverse Complement

The program generates the reverse complement of the input DNA sequence using Biopython.

### 5. Protein Translation

The DNA sequence is translated into amino acids using Biopython's standard genetic code. The symbol `*` represents a stop codon.

## Sample Results

- Sequence length: 120 bases
- GC content: 50.0%
- A count: 31
- T count: 29
- G count: 32
- C count: 28

## Learning Outcomes

This project provides introductory experience in Python programming, DNA sequence analysis, nucleotide composition, GC content calculation, reverse-complement generation, and DNA translation.

## Future Improvements

- Read DNA sequences from FASTA files.
- Validate DNA input.
- Generate nucleotide composition charts.
- Analyze multiple DNA sequences.
- Perform sequence alignment.

## Author

**Dr. Maria Hasnain**  
Bioinformatics | Biotechnology | Computational Biology and AI in Life Sciences

## Note

The DNA sequence used in this project is an illustrative practice sequence, not a verified biological gene. Protein translation results should not be interpreted as a validated functional protein.

## License

For educational and research purposes.
