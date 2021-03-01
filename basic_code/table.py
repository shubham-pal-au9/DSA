def table(num):
    for i in range(1,11):
            print(num,"*",i,"=",num*i)

if __name__ == '__main__':
    num = int(input('Enter the number for table generation:'))

    table(num)
    
