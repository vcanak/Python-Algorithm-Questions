def longest_palindrome(string:str)->int:
        """
        :type s: str
        :rtype: int
        """
        store_dic = dict()
        for single_str in string:
            if single_str in store_dic:
                del store_dic[single_str]
            else:
                store_dic[single_str] = 1
       
        if len(store_dic) == 0:
            return len(string) 
        else:
            return len(string) - len(store_dic) + 1

print(longest_palindrome("abccccdd"))