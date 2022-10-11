class Solution:
    '''
    Given a string s, return the longest palindromic substring in s.
    A string is called a palindrome string if the reverse of that string is the same as the original string.
    '''
    inputs = ["babad", "bab"]

    def __init__(self):
        for s in self.inputs:
            print(self.longestPalindrome(s))

    def longestPalindrome(self, s: str) -> str:
        pass

def main():
    Solution()

if __name__=="__main__":
    main()