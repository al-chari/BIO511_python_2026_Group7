data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}
#making the empty dictionary
unique_bacteria = []
for pat, bacterium in data.items():
    for bacteria in bacterium:
        #originally I only wrote up to here then realised I am not interating through them individually
        #I was also going through bacterium meaning all of them in the dictionary instead of through each of them
        #individually, make sure you don´t make my mistakes
        if bacteria not in unique_bacteria:
            unique_bacteria.append(bacteria)
print(unique_bacteria)

#I screw up the brackets too often I need to fix that
bacteria_to_patients={}
for bacteria in unique_bacteria:
    if bacteria not in bacteria_to_patients:
        bacteria_to_patients[bacteria]= []

#this is from the first run I just left it here to show the work flow print(bacteria_to_patients)

for pat, bacterium in data.items():
    for bacteria in bacterium:
        #honestly no clue why this worked as I did it, I broke my head over it will have to read
        #I mean I know that I am appending them as strings in a list so that is why append works
        #I just feel like I am missing a step at this point.
        bacteria_to_patients[bacteria].append(pat)
print(bacteria_to_patients)
