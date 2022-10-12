class Solution:
    '''Given a string s, return the longest palindromic substring in s.
    A string is called a palindrome string if the reverse of that string is the same as the original string.
    '''

    inputs = ["babad", "bab", "baab"]
    outputs = ["aba", "aba", "baab"]

    def __init__(self):
        for s in self.inputs:
            new_s = self.longestPalindrome(s)
            print(new_s)

    def longestPalindrome(self, s: str) -> str:
        # init
        palindrome = ''
        length = 0

        # treat every char as the center of a palindrome
        for i in range(len(s)):
            # check odd length (aba)
            left = i
            right = i

            while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                # set new max length
                if (right - left + 1) > length:
                    palindrome = s[left:right+1]
                    length = right - left + 1
                
                # increment
                left -= 1
                right += 1

            # check even lenght (abba)
            if len(s) >= 2:
                left = i
                right = i + 1

                while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                    # set new max length
                    if (right - left + 1) > length:
                        palindrome = s[left:right+1]
                        length = right - left + 1

                    # increment
                    left -= 1
                    right += 1

        return palindrome
                
def main():
    Solution()

if __name__=="__main__":
    main()