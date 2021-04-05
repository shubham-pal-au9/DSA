# Cyclically rotate an array by one

# Solution 

def rotate(lst1):
    temp = []
    res = []
    
    for i in range(0,len(lst1)-1):
        temp.append(lst1[i])
        
    res.append(lst1[len(lst1)-1])
    
    for i in range(0,len(temp)):
        res.append(temp[i])
        
    
    print(res)
    

if __name__ == '__main__':

    lst1 = [1,2,3,4,5]
    rotate(lst1)
   
    
   
    
