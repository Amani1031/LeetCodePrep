
import collections

class Solution:
    def canConstruct(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

'''
Couldn't do this one at all on my own.

TIPS:
- There is a Counter() mechanism in Collections which can be added and subtracted to find differences
'''