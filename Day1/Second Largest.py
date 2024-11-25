class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        arr.sort()
        for i in range(n - 2, -1, -1):
            if arr[i] != arr[n - 1]:
                return arr[i]
        return -1
"""
Another methos without using sort()
class Solution:
    def getSecondLargest(self, arr):
        first = second = float('-inf')
        for num in arr:
            if num > first:
                second = first  
                first = num     
            elif num > second and num != first:
                second = num  
        return second if second != float('-inf') else -1

"""
