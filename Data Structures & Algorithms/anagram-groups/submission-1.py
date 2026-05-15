class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = dict()
        output = list()
        for words in strs:
            key = tuple(sorted(words))
            if key not in anag_dict:
                anag_dict[key] = [words]
            else:
                anag_dict[key].append(words)
        for key, values in anag_dict.items():
            output.append(values)
        return output
