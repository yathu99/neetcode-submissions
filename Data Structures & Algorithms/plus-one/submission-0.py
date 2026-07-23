class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        digits[len(digits)-1]+=1
        for z in range(len(digits)-1,-1,-1):
            digits[z]+=carry
            if(digits[z]==10):
                digits[z]=0
                carry=1
            else:
                carry=0
        if(carry==1):
            digits.insert(0,1)
        return digits