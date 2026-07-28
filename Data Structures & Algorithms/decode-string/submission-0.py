class Solution:
    def decodeString(self, s: str) -> str:
        # [] indicates a call to recurse
        # Key is that s = 1[s], so we can start with call

        # If we hit [], we need to recurse
        # Recursion returns unraveled string - Ex: 2[a3[b]] would
        # give us 2[abbb] -> abbbabbb. This works because we
        # return from the top of the recursion call stack first
        
        # If string has char, just add to output string
        # If contains number, read number until "[" and store number
        # Call recurse with string what is in between "[]" - determine
        # whenever a "]" is seen. Return output string when "]"

        # Parameters:
            # String to parse: Ex: a3[b]
            # Index to store position
        # Returns:
            # Output string


        def recurse(string, i):
            out = ""
            val = 0
            while i < len(string):
                c = string[i]
                if c.isdigit():
                    val = val * 10 + int(c)
                    i += 1
                elif c == "[":
                    res, idx = recurse(string, i + 1)
                    out += res * val
                    i = idx
                    val = 0
                elif c == "]":
                    return out, i + 1
                else:
                    out += c
                    i += 1
            return out, i
            
        return recurse(s, 0)[0]