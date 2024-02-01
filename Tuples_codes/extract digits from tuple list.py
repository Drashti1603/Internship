# lst = [(1, 45), (3, 67), (99, 10), (52, 43), 'hi']
 
# print(str(lst))
# x=""
# for i in lst:
#     if type(i)!=str:
#         for j in i:
#             x+=str(j)
# ans=[]
# for i in x:
#     if i not in ans:
#         ans.append(i)
# print("Digits=",*ans)
list=[(45),(5),(6),(568),'hi']
result=[]
for i in list:
    if type(i)!=str:
       for j in str(i):
          if j not in result:
            result.append(j)
print(result)