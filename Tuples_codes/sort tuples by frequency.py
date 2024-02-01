tup =[ (11, 3), (9, 1), (6, 11), (2, 10), (5, 7)]
diff_list = [abs(x - y) for x, y in tup]
 
ans = sorted(tup, key = lambda sub: diff_list.count(abs(sub[0] - sub[1])))
 
print("Sorted Tuples : " + str(ans))