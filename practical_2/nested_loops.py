sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
stop_codons = ['TAA', 'TGA', 'TAG']
start_codon = "ATG"
print()

possible_valid_sequences = []
for sequence in sequences:
    if start_codon in sequence:
        for stop_codon in stop_codons:
            if stop_codon in sequence:
                print("The sequence " + sequence + " has the start codon ATG and also the " + stop_codon + " stop codon.")
        possible_valid_sequences.append(sequence)
    else:
        for stop_codon in stop_codons:
            if stop_codon in sequence:
                print("The sequence " + sequence + " has the stop codon " + stop_codon + ".")
            else:
                print("The sequence " + sequence + " has not a start codon, nor a stop one.")

print()
print("The sequences that have both a start and stop codon are:")
print(possible_valid_sequences)
print()

cropped_sequences = []
for sequence in possible_valid_sequences:
    i = 0
    for codon in (sequence):
        if sequence[i:i+3] == "ATG":
            sequence = sequence.replace(sequence[0:i+3], "")
            cropped_sequences.append(sequence)
        i = i + 1

final_valid_sequences = []
i = 0
for sequence in cropped_sequences:
    for stop_codon in stop_codons:
        if stop_codon in sequence:
            final_valid_sequences.append(possible_valid_sequences[i])
            break
    i = i + 1        

print("The sequences that have a valid structure (start & stop codon, with the stop one after the start codon) are:")
print(final_valid_sequences)
