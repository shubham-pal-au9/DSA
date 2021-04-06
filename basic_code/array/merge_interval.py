""" Merge Intervals

Input: intervals = [[1,3],[2,6],[8,10],[9,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]. """

# Solution

if __name__ == '__main__':
    arr = [[1,3],[2,6],[8,10],[15,18]]
    res = []
    temp = []
    final = []
    final_one = []
    for i in range(0,len(arr)-1):
        if arr[i][0] == arr[i+1][0]-1:
            
            temp.append(arr[i][0])
            temp.append(arr[i+1][1])
            for j in range(i+2,len(arr)):
                
                res.append(arr[j])
    
    res.append(temp)
    
    final_one.append(res[len(res)-1])
    
    for i in range(0,len(res)-1):
        final_one.append(res[i])
    
    print(final_one)

    

                
            

    
  
