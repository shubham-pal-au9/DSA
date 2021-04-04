# Maximum and minimum of an array using minimum number of comparisons
# Solution

def max_min(lst):
    lst.sort()
    

    for i in range(len(lst)-1,-1,-1):
        print "Maximum is",lst[i]
        break
    for i in range(0,len(lst)):
        print "Minimum is:",lst[i]
        break
    
    """ print(max(lst))
    print(min(lst)) """

if __name__ == '__main__':
    lst = [9, 2, 3, 4, 5, 6]
    max_min(lst)
