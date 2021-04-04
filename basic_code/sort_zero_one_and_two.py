# Sort an array of 0s, 1s and 2s
# Solution 
def sorting(lst):
    
    res = []
    
    
    for i in range(0,len(lst)):
        if lst[i] == 0:
            res.append(lst[i])
    
    for i in range(0,len(lst)):
        if lst[i] == 1:
            res.append(lst[i])
            
    for i in range(0,len(lst)):
        if lst[i] == 2:
            res.append(lst[i])
            

    print(res)
    
if __name__ == '__main__':
    lst = [0,2,1,2,0]
   
    sorting(lst)
