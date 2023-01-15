class Solution(object):
    def is_anagrams(self, str1, str2):
        return sorted(str1) == sorted(str2)
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # keys_set = set()
        # for index, value in enumerate(strs):
        #     keys_set.add(''.join(sorted(value)))

        # hash_map = {}
        # for key in keys_set:
        #     hash_map[key] = []
        
        # for key, value in hash_map.items():
        #     for string in strs:
        #         if ''.join(sorted(string)) == key:
        #             hash_map[key].append(string)
        
        # return list(hash_map.values())
        
        lookup = {}
        for word in strs:
            word_list = list(word)
            word_list.sort()
            # print(word_list)
            
            curr_word = ''.join(word_list)
            if curr_word not in lookup:
                lookup[curr_word] = [word]
            else:
                lookup[curr_word].append(word)
        
        return [x for x in lookup.values()]


        
        
strs = ["eat","tea","tan","ate","nat","bat"]
sl = Solution()
print(sl.groupAnagrams(strs))
    

        