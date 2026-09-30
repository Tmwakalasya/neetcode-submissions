class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            word_len = len(word)
            pfx = f"{word_len:4}"
            encoded.append(pfx + word)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = []
        idx = 0
        while idx < len(s):
            str_len = int(s[idx:idx + 4])
            idx += 4
            d_word = s[idx:str_len + idx]
            decoded.append(d_word)
            idx += str_len
        return decoded
