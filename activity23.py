bts_svt = ["Jin", "Jhope", "Suga", "Namjoon", "Jimin", "Jungkook", "Taehyung","Woozi", "S.coups"]
#           0       1        2       3            4         5           6          7        8

print("FIRST LIST:\n","\n",bts_svt[1],"\n",bts_svt[3:8],"\n")
#       All      2nd      3rd to 8th 

bts_svt.append("The8") # Adding an item
print("The8 ADDED:\n",bts_svt,"\n")

bts_svt.insert(2, 'Wonwoo') # Inserting an item in between the other items
print('INSERT Wonwoo IN BETWEEN:\n',bts_svt,'\n')

bts_svt.pop() # Removing the last
print('REMOVE LAST ITEM\n',bts_svt,'\n')

print('COUNTING ITEMS:\n',len(bts_svt)) # Counting the number of items 