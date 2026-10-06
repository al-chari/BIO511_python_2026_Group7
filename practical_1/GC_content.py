sequence = "TTAGGCATGCCGATATCGGCTTA"

# checking for the first base in sequence
if sequence[0] == "G" or sequence[0] == "C":
    print("First base is a G/C!")
else:
    print("First base is not a G/C!")


# counting number of G/C bases in sequence
gc_count = 0
for base in sequence:
    if base == "G" or base == "C":
        gc_count = gc_count + 1
print(gc_count)

# calculating the G/C %
gc_percentage = (gc_count / len(sequence)) * 100
print(f"The %GC is {gc_percentage}")
