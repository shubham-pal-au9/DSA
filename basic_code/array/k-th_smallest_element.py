# Kth smallest element

# Solution 


def k_smallest(lst,k):
    lst.sort()
    
    print "Kth smallest element is:",lst[k-1]
    
if __name__ == '__main__':
    lst = [7,10,4,3,20,15]
    k =3 
    k_smallest(lst,k)
