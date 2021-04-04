# Move all negative numbers to beginning and positive to end with constant extra space

# Solution
    
if __name__ == '__main__':
    
    lst = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    neg_lst = []
    pos_lst = []

    
    for i in range(0,len(lst)):
        if lst[i] < 0:
            neg_lst.append(lst[i])
        
        else:
            pos_lst.append(lst[i])
    
    for i in range(0,len(pos_lst)):
        neg_lst.append(pos_lst[i])
            
    print(neg_lst)
    
   
    
