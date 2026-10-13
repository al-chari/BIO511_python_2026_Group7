# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

def count_above(seq, lim):
    """Counts the amount of numbers above a limit (lim) in a sequence (seq)"""
    count = 0
    for number in seq:
        if number > lim:
            count += 1
        else:
            continue
    return(count)

print(count)

print(count_above(nums, limit))
print(count, "\n")

def summarize_text(s):
    """"""
    summary = {"digits":0, "letters":0, "other":0}
    s = str(s)
    for character in s:
        if character.isalpha() == True:
            summary["letters"] += 1
        elif character.isdigit() == True:
            summary["digits"] += 1
        else:
            summary["other"] += 1
    return(summary)

print(summary)
print(summarize_text(text))
print(summary)
print(len(text), "\n")


def aggregate(seq, mode, threshold):
    if mode == "sum" or "count":
        result = 0
    elif mode == "max":
        result = None
    else:
        print("Invalid mode, please try again")
        return()

    for n in seq:
        if n < 0:
            continue
        elif n >= threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                if result == None or n > result:
                    result = n
    return(result)

print(result)
print(aggregate(nums, "sum", limit))
print(aggregate(nums, "count", limit))
print(aggregate(nums, "max", limit))
print(result)
print(aggregate(nums, "max", 100), "\n")

values = ['10', '5', 'hello', '8', True, 'three', '2']
for value in values:
    try:
        value = int(value)
        print(value)
    except ValueError:
        print(f"Skipping invalid value: {value}")

# It is funny, because True can be turned into 1 and False into 0.
