dict = {"Gfg" : 5, "is" : 8, "Best" : 10, "for" : 8, "Geeks" : 9}
print("Original: " + str(dict))

updict = {"Gfg" : 10, "Best" : 17}
print("Value to be changed : " + str(updict))

for sub in dict:
		if sub in updict:
		  dict[sub] = updict[sub]

print("updated: " + str(dict)) 
