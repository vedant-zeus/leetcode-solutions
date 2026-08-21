class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtracking(current ,open , close):
            if len(current) == 2 * n :
                result.append(current)
                return
            
            if open < n :
                backtracking(current + '(' , open + 1, close)
            
            if close < open:
                backtracking(current + ')' , open , close+1)
            
        backtracking("",0,0)
        return result