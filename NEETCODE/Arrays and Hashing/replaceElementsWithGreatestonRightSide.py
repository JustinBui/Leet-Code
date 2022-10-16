class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        current_greatest_val = 0
        current_greatest_ind = 0
        
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                
            else:
                if i >= current_greatest_ind:
                    current_greatest_val = 0
                    for j in range(i + 1, len(arr)):
                        if arr[j] >= current_greatest_val:
                            current_greatest_val = arr[j]
                            current_greatest_ind = j
                            
                arr[i] = current_greatest_val
        
        return arr

if __name__ == '__main__':
    obj = Solution()

    arr = [17,18,5,4,6,1]
    print(obj.replaceElements(arr))