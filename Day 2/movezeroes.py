class Solution:
    def pushZerosToEnd(self,arr):
        n=len(arr)
        count=0
        for i in range(n):
            if arr[i]!=0:
                arr[count]=arr[i]
                count=count+1
        while count<n :
           arr[count]=0
           count=count+1
        return arr
