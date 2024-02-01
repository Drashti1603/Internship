x = input("Enter String:")
freq = {}
 
for i in x:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
 
print(str(freq))