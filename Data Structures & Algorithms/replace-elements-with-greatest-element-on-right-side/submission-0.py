class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force would be to just 
        # go through the array and then find the greatest elem
        # to its right and replace it

        n = len(arr)
        for i in range(n - 1):
            swap = float("-inf")
            for j in range(i + 1, n):
                swap = max(swap, arr[j])
            arr[i] = swap
        arr[-1] = -1
        return arr