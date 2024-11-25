class Solution:
    def reverseArray(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        
        while left < right:
            # Swap the elements at `left` and `right`
            arr[left], arr[right] = arr[right], arr[left]
            # Move the pointers
            left += 1
            right -= 1
        
        return arr