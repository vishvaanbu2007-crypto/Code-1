string=input("enter string: ")
chars=list(string)
result=""
while(len(chars)>0):
    smallest=chars[0]   
    for chr in chars:
    
        
    
        if(chr.lower()<smallest.lower()):
    
            smallest=chr


    
    result+=smallest
    
    chars.remove(smallest)

print(result)