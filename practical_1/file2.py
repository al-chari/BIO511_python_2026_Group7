read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}

sample = list(read_counts.keys())[1]
passed_qc = True


if sample in read_counts:
    if read_counts[sample] != None:
        if read_counts[sample] >= 1000000:
            if passed_qc == True:
                print("ready for analysis")
            else:
                print("enough reads, but did not pass QC")
        else:
            print("too few reads!")
    else:
        print("sequencing failed!")
else:
    print("unkown sample :(")
