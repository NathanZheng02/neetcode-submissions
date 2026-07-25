class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Retrieve [val, time] from hashmap
        values = self.hm.get(key, []) # [String, Time]
        res = ""

        # Binary search for timestamp
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res


