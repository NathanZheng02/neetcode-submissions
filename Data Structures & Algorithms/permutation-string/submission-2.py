class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge Cases
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26 # O(26)
        count2 = [0] * 26 # O(26)

        # Load counts of the first window into a count array: O(m)
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # Slide window and update counts array: O(n - m)
        for right in range(len(s1), len(s2)):
            print("First Char: ", s2[right - len(s1)])
            print("Current : ", s2[right], "\n") # -1 from curr is end of window
            if count1 == count2:
                return True
            else:
                count2[ord(s2[right - len(s1)]) - ord('a')] -= 1
                count2[ord(s2[right]) - ord('a')] += 1
        # Check last window
        return count1 == count2
