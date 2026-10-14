import numpy as np

# given inputs
genes = ["geneA", "geneB", "geneC", "geneD", "geneE"]
control = [120, 340, 15, 800, 60]
treated = [240, 340, 60, 200, 30]

# 1. Adding the lists
total_reads_1 = control + treated
print(total_reads_1)
# 2 Making arrays
total_reads_2 = np.array(control) + np.array(treated)
print(total_reads_2)

# 3. Calculating fold change
fold_change = np.array(treated) / np.array(control)
print(fold_change)

# 4. Calculating log2 fold change
log2_fold_change = np.log2(fold_change)
print(log2_fold_change)

# 5. Normalising the samples 
normalised_treated = np.array(treated) / np.sum(np.array(treated))
normalised_control = np.array(control) / np.sum(np.array(control))
print(normalised_treated)
print(normalised_control)

log2_fold_change_normalised = np.log2(normalised_treated / normalised_control)
print(log2_fold_change_normalised)
