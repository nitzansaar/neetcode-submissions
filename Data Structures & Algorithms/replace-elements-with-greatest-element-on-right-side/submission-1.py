class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force would be to just 
        # go through the array and then find the greatest elem
        # to its right and replace it

        # better approach, start from the end and keep a curr max
        # and just use that curr max to update the array
        n = len(arr)
        curr_max = arr[-1]
        for i in range(n-1, -1, -1): # start from the back
            tmp = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, tmp)
        arr[-1] = -1
        return arr

