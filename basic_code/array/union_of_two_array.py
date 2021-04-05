# Union of two arrays
#Solution

def union(lst1,lst2):
    count = 0
    
    for i in range(0,len(lst2)):
        lst1.append(lst2[i])
        
    mylist = sorted(set(lst1))
    
    
    for i in range(0,len(mylist)):
        count = count + 1 
    
    print(count)

def intersection(lst1,lst2):
    res = []
    count = 0
    for i in range(0,len(lst2)):
        for j in range(0,len(lst1)):
            if lst2[i] == lst1[j]:
                res.append(lst2[i])

    mylist = sorted(set(res))
    
    for i in range(0,len(mylist)):
        count = count + 1 
    print(count)

if __name__ == '__main__':
    
    lst1 = [1,2,3,4,5]
    lst2 = [1,2,3]
    
    union(lst1,lst2)
    intersection(lst1,lst2)
   
