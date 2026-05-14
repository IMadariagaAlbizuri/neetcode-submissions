class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "_" + word
        return string

    def decode(self, s: str) -> List[str]:
        list_words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            counter = int(s[i:j])
            list_words.append(s[j+1:j+1+counter])
            i = j + 1 + counter
        return list_words
