
#Attempt 1 : 61ms
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = str.split(' ')
        print(x)
        return len(x[-1])

#Attempt 2 : 62 ms
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
            else:
                if length > 0: return length
        return length

'''

    public int lengthOfLastWord(String s) {
        int length = 0;
		
		// We are looking for the last word so let's go backward
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) != ' ') { // a letter is found so count
                length++;
            } else {  // it's a white space instead
				//  Did we already started to count a word ? Yes so we found the last word
                if (length > 0) return length;
            }
        }
        return length;
    }
}
'''