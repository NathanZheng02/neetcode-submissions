# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Edge Cases
        if len(pairs) == 0:
            return []
        
        ret_arr = [pairs[:]]

        # Keep track of valid indicies (sorted ones already)
        valid = 1
        while valid < len(pairs):
            # Pop next searching index
            curr = pairs.pop(valid)

            count = valid - 1
            while count >= 0 and pairs[count].key > curr.key:
                count -= 1
            pairs.insert(count + 1, curr)

            # Copy and increment
            ret_arr.append(pairs[:])
            valid += 1

        return ret_arr
