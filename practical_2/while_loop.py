#The data it is a string so do not worry gabron
sequence = 'GATTACAGAACTGATAC'
#this is the maximum number you can set it for both loops here
count_a = 3

#the position of the sequence defined externally as 0 and the number of As starting with 0
pos= 0
a_count= 0

#we set the while based on the variables
while a_count < count_a:
    if sequence[pos] == "A":
        a_count+=1
    pos+=1
#seen as how we want it to move once at the end because the loops moves even after we are done I added a -1
#could have probably done something else by altering the loop but seen as how everything is very small I do not find
#much need for it.
pos=pos-1
print("third A at position while:", pos)

#it is practically identical, made new variables other than count_a 
b_count = 0
posi= 0
for nucleo in sequence:
    if nucleo== "A":
        b_count +=1
    if b_count == count_a:
        break
    posi+=1
print("Third A at position for:", posi)
