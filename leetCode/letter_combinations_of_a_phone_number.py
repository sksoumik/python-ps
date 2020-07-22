"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        res = ['']
        for i in map(int, list(digits)):
            current = []
            for j in res:
                
        

if __name__ == "__main__":
    obj = Solution()
    digits = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    res = obj.letterCombinations(digits)
