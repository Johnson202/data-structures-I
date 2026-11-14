def is_valid(s:str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        stack_brackets = []
        closing_brackets = {"}": "{", "]": "[", ")": "("}
        for bracket in s:
            if bracket in closing_brackets:
                if not stack_brackets or stack_brackets[-1] != closing_brackets[bracket]:
                    return False
                stack_brackets.pop()
            else:
                stack_brackets.append(bracket)

        return len(stack_brackets) == 0
    
print(is_valid("(()){[]}")) # True
print(is_valid("(()){[}")) # False
print(is_valid("")) # True
print(is_valid("{[({")) # False
print(is_valid("[{}")) # False
print(is_valid("[[[{]]]}")) # False