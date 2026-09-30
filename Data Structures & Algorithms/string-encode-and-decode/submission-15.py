class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            str_len = len(s)
            pfx = f"{str_len:4}"
            encoded.append(pfx + s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        idx = 0
        while idx < len(s):
            str_len = int(s[idx:idx + 4])
            idx += 4
            decoded_word = s[idx:idx + str_len]
            decoded.append(decoded_word)
            idx += str_len
        return decoded
