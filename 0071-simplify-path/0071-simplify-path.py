class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # Current file or path
        cur = ""
        
        for ch in path + "/":
            if ch == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += ch

        
        return "/" + "/".join(stack)
