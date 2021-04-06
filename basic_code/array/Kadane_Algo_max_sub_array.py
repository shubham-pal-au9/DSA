# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

#Solution
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

# Solution
def maxSubArraySum(a,size):
       
        lsum = a[0]
        gsum = a[0]
        for i in range(1, size):
            lsum = max(a[i], lsum+a[i])
            gsum = max(lsum, gsum)
        print(gsum)

if __name__ == '__main__':
    arr=[1,2,3,-2,5]
    size = len(arr)

    maxSubArraySum(arr,size)
