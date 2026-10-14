import csv
import sys
with open("trial.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Gender"])
    writer.writerow(["Alice", 30, "Female"])
    writer.writerow(["Bob", 25, "Male"])
    writer.writerow(["Charlie", 35, "Male"])
    writer.writerow(["Diana", 18, "Female"])

with open("trial.csv", 'a') as f:
    writer = csv.writer(f)
    if len(sys.argv) != 4:
        print("Please provide exactly three arguments: NAME, AGE, GENDER\nUsage: python filename.py NAME AGE GENDER")
        sys.exit(1)
    elif len(sys.argv) == 4:
        writer.writerow([sys.argv[1], sys.argv[2], sys.argv[3]])
