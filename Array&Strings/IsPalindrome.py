class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        # strList = list(s)
        # for i in range(len(strList)):
        #     if not strList[i].isalpha() or not strList[i].isdigit():
        #         print(i)
        #         strList.pop(i)
        # we shouldn't pop in the loop itself, we should keep track of the index of smthn
        # can make it better -> below
        # we can shorten all that by just making a new list from str checking if satisfies our conition
        strList = [char for char in s if char.isalpha() or char.isdigit()]
        return True if strList == strList[::-1] else False

