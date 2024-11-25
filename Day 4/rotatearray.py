class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  
        temp = [0] * n  
        for i in range(n - d):
            temp[i] = arr[i + d]
        
        # Copy the elements
        for i in range(d):
            temp[n - d + i] = arr[i]
        
        for i in range(n):
            arr[i] = temp[i]
