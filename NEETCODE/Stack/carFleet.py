class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Array of tuples containing each car's (position, speed)
        pos_speed_pair = [(p, s) for p, s in zip(position, speed)]
        time_stack = []

        # Sorting in descending order by position
        for p, s in sorted(pos_speed_pair)[::-1]:
            # Time of each car to reach the target according to their current position and speed
            time = (target - p) / s
            time_stack.append(time)

            # If the car ahead is slower, pop off the stack
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                time_stack.pop()

        return len(time_stack)
