class Solution:
    dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
    
    sub_combo_dict = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    
    skip_flag = False
    
    def romanToInt(self, s: str) -> int:
        # init
        int = 0
        
        # loop
        for i, char in enumerate(s):
            # check if prev iteration was a sub combo
            if self.skip_flag:
                self.skip_flag = False
                continue
    
            # check if subtraction if before end of string
            if i <= (len(s)-2):
                if s[i] == 'I' and s[i+1] == 'V':
                    int += self.sub_combo_dict['IV']
                    self.skip_flag = True
                elif s[i] == 'I' and s[i+1] == 'X':
                    int += self.sub_combo_dict['IX']
                    self.skip_flag = True
                elif s[i] == 'X' and s[i+1] == 'L':
                    int += self.sub_combo_dict['XL']
                    self.skip_flag = True
                elif s[i] == 'X' and s[i+1] == 'C':
                    int += self.sub_combo_dict['XC']
                    self.skip_flag = True
                elif s[i] == 'C' and s[i+1] == 'D':
                    int += self.sub_combo_dict['CD']
                    self.skip_flag = True
                elif s[i] == 'C' and s[i+1] == 'M':
                    int += self.sub_combo_dict['CM']
                    self.skip_flag = True
                else:
                    int += self.dict[char]
            else:
                # add last character
                int += self.dict[char]
            
        return int
        