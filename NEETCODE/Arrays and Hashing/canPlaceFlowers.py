class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Add dummy 0's to each side of our input array
        flowerbed.insert(0, 0)
        flowerbed.insert(len(flowerbed), 0)

        consecutive_0s = 0
        total_flowers_allowed = 0

        for i, f in enumerate(flowerbed):
            if f == 0:
                consecutive_0s += 1
            if f == 1 or i == len(flowerbed) - 1:
                if consecutive_0s >= 3:
                    total_flowers_allowed += (consecutive_0s - 1) / 2
                consecutive_0s = 0
        
        return total_flowers_allowed >= n

if __name__ == '__main__':
    flowerbed = [0,0]
    n = 3

    entity = Solution()
    print(entity.canPlaceFlowers(flowerbed, n))