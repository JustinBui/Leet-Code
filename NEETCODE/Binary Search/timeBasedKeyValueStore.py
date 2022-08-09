class TimeMap:

    def __init__(self):
        self.items = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.items.get(key) == None:
            self.items[key] = list()
        self.items[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if self.items.get(key) == None:
            return ''

        # Checking the very first timestamp (Which is the smallest)
        if self.items[key][0][0] > timestamp:
            return ''

        l = 0
        r = len(self.items[key]) - 1

        while l <= r:
            m = (l + r) // 2

            if self.items[key][m][0] == timestamp:
                # [key][location of list at this key][timestamp as 0 OR value as 1]
                return self.items[key][m][1]
            elif self.items[key][m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return self.items[key][r][1]

        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)


if __name__ == '__main__':
    timeMap = TimeMap()

    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))  # Bar
    print(timeMap.get("foo", 3))  # Bar

    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))  # Bar2
    print(timeMap.get("foo", 5))  # Bar2
