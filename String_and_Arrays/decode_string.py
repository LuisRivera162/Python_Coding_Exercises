# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s,0)[0]

    def helper(self, s, index):
        integer = ''
        result = '' 
        
        while index < len(s):
            char = s[index]

            if char.isalpha():
                result += char
            elif char.isdigit():
                integer += char
            elif char == ']':
                return result, index
            elif char == '[':
                str_to_add, index = self.helper(s,index+1)
                for _ in range(int(integer)):
                    result += str_to_add
                integer = ''
            index += 1

        return result, index