data = {
    'pat_001': ['bacZZt98', 'bac889Ytd'], 
    'pat_002': ['bac0GFrr'], 
    'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

unique_bacteria = []

for key_patients, value_bacteria in data.items():
    for bacteria in value_bacteria:
        if bacteria not in unique_bacteria:
            unique_bacteria.append(bacteria)

print(unique_bacteria)

bacteria_to_patients = {}

for bacteria in unique_bacteria:
    bacteria_to_patients[bacteria] = []

print(bacteria_to_patients)

for patient in data.keys():
    for bacteria in bacteria_to_patients.keys():
        if patient not in bacteria_to_patients[bacteria]:
            if bacteria in data[patient]:
                bacteria_to_patients[bacteria].append(patient)

print(bacteria_to_patients)
