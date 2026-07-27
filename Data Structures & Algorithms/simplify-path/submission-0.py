class Solution:
    def simplifyPath(self, path: str) -> str:
        # "/" acts like a stop processing symbol
        # From one slash to another, there are 2 commands
        # ".." essentially pops from the stack
        # Everything else that is not "." or "" adds to the stack

        # Other considerations: 
            # Path must start with "/", so we
            # just manually add that at the end before we return
            # Directories separated by slash, so we keep track
            # of file names in the stack and .join them with "/"

        stack = []
        curr = ""

        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        
        return "/" + "/".join(stack)
