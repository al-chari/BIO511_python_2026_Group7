list = ["anger", "pride", "lust", "gluttony", "greed", "envy", "sloth"]

loop_number = 0
for sin in list:
    if loop_number < 5:
        loop_number += 1
        print(str(loop_number) + " " + sin)
