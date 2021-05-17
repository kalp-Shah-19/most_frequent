
  

x=(input("Please enter a string "))
char={}
for val in x:
	if val in char:
		char[val]+=1
	else:
		char[val]=1
print(char)
