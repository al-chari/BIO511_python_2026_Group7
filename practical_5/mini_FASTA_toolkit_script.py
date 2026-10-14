from Bio import SeqIO, SeqRecord, Seq

# Getting the sequences, and printing the ID, length, and first 10 bases.
sequences = SeqIO.parse("dna.fasta", "fasta")
for record in sequences:
    print(record.id)
    print(len(record.seq))
    print(record.seq[0:10])

# Getting the reverse complement of the sequences, and printing the ID, length, and first 10 bases.

with open("dna_rc.fasta", "w") as output_file:
    for record in SeqIO.parse("dna.fasta", "fasta"):
        rc_seq = SeqRecord.SeqRecord(record.seq.reverse_complement(), id=f"{record.id}_rc", description=f"Reverse complement of {record.id}")
        print(rc_seq.id)
        print(len(rc_seq.seq))
        print(rc_seq.seq[0:10])
        SeqIO.write(rc_seq, output_file, "fasta")

# Getting the %GC of each sequence.
with open("dna_with_gc.fasta", "w") as output_file:
    for record in SeqIO.parse("dna.fasta", "fasta"):
            gc_percentage = 100 * float(record.seq.count("G") + record.seq.count("C")) / len(record.seq)
            gc_percentage = round(gc_percentage, 1)
            seq_w_gc = SeqRecord.SeqRecord(record.seq, id=record.id, description=f"GC={gc_percentage}%")
            SeqIO.write(seq_w_gc, output_file, "fasta")

# Translating the sequence (I dont really understand the part of reading dna_rc.fasta again to confirm the IDs and that...)

with open("dna_translated.fasta", "w") as output_file:
    for record in SeqIO.parse("dna.fasta", "fasta"):
        translated_seq = SeqRecord.SeqRecord(record.seq.translate(), id=f"{record.id}_translated", description=f"Translated sequence of {record.id}")
        print(translated_seq.id)
        print(len(translated_seq.seq))
        print(translated_seq.seq[0:10])
        SeqIO.write(translated_seq, output_file, "fasta")
