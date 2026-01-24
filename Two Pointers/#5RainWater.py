class Solution:
    def trap(self, height: List[int]) -> int:

        bar = 0

        lefty = []
        num1 = height[0]
        for i in height:
            if i > num1:
                num1 = i
            lefty.append(num1)

        righty = []
        num2 = height[-1]
        for j in range(len(height)-1,-1,-1):
            if height[j] > num2:
                num2 = height[j]
            righty.append(num2)

        righty.reverse()

        l = 0
        r = len(height)-1

        while l < r :
            bar += min(lefty[l],righty[l]) - height[l]
            l+=1

        return bar
            

