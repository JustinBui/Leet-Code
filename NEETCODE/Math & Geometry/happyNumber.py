class Solution:
    def isHappy(self, n: int) -> bool:
        str_n = str(n) # Convert to string
        existing_nums = set()

        while True:
            total = 0
            for num in str_n:
                total += int(num) ** 2 # Convert character to integer and square it. Then add to total
            
            if total == 1:
                return True
            elif total in existing_nums:
                return False
            
            existing_nums.add(total)
            str_n = str(total)

