
from Bio.Seq import Seq

dna = Seq("ATGCGTACGTAGCTAGGCTAACGT""GATCGATCGGCTAGCTAGCATGCA""ATGCCGTAGCTAGCATCGATCGTA""GCTAGCTAACGTAGCATCGATGCT""AGCTAGCATGCGTACGTAGCTTAA")

print("DNA Sequence:", dna)

print("Sequence Length:", len(dna), "bases")

print("A count:", dna.count("A"))
print("T count:", dna.count("T"))
print("G count:", dna.count("G"))
print("C count:", dna.count("C"))

gc_count = dna.count("G") + dna.count("C")
gc_percent = (gc_count / len(dna)) * 100

print("GC Percentage:", round(gc_percent, 2), "%")

print("Reverse Complement:", dna.reverse_complement())

complete_length = (len(dna) // 3) * 3
coding_dna = dna[:complete_length]
protein = coding_dna.translate()

print("Protein Sequence:", protein)

print("DNA analysis completed successfully!")