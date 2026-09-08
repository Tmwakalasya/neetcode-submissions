class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            word_len = len(word)
            pfx = f"{word_len:4}"
            encoded.append(pfx + word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        idx = 0
        word_len = len(s)
        decoded = []
        while idx < word_len:
            str_len = int(s[idx: idx + 4])
            idx += 4
            decoded_word = s[idx : idx + str_len]
            decoded.append(decoded_word)
            idx += str_len
        return decoded
