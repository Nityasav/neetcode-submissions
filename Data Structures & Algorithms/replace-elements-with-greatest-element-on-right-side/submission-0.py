class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l, r = 0, len(arr)-2
        count = 1

        while l != len(arr)-1:
            tmp = r
            maxOnRight = arr[len(arr)-1]
            while tmp > l:
                maxOnRight = max(maxOnRight, arr[tmp])
                tmp -= 1
            
            arr[l] = maxOnRight
            l += 1
            count += 1
        
        arr[len(arr)-1] = -1

        return arr

                
