class Solution:
    def reverse(self, x):
        s=str(x)
        ans=""
        if x<0:
            a=s[:1]
            b=s[1:][::-1]
            ans=a+b
        else:
            ans=s[::-1]
        ans=int(ans)
        if (-(2**31)>ans or ans>(2**31)-1):
            return 0
        return ans