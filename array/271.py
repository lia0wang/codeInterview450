class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        encode = ''
        for s in strs:
                encode += s + '#'
        return encode
            
    def decode(self, strs):
        return [s for s in strs.split('#')][0:-1]
        



input = ["lint", "code", "love", "you"]
sl = Solution()
print(sl.encode(input))
print(sl.decode(sl.encode(input)))