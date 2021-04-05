# Write a program to reverse an array or string

# Solution 
def reverse_list(lst):
    lst.sort()
    print(lst)

    for i in range(len(lst)-1,-1,-1):
        print(lst[i])


if __name__ == '__main__':
    lst = [9, 2, 3, 4, 5, 6]
    reverse_list(lst)
