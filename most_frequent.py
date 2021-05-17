x=(input("Please enter a string "))
char={}
def most_frequent(x):
    for val in x:
        if val in char:
            char[val]+=1
        else:
            char[val]=1
    print(char)
most_frequent(x)
    
      
            
            

    
	    
	
            
