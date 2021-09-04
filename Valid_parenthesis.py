
def paranthesis(s):

    box = []
    dict = {"(": ")", "{": "}", "[": "]"}
    open = ["(", "{", "["]
    close = [")", "}", "]"]

    for i in s:

        if i in "({[":
            box.append(i)

        else:

            if len(box) == 0 or dict[box.pop()] != i:
                return "false"

    return len(box) == 0


print(paranthesis("({{{{}}}))"))


# Leetcode format

class Solution:
    def isValid(self, s: str) -> bool:
        box = []
        dict = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in "({[":
                box.append(i)
            else:
                if len(box) == 0 or dict[box.pop()] != i:
                    return False

        return len(box) == 0
