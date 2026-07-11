class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            word_len = len(word)
            prefix = f"{word_len:4}"
            encoded.append(prefix + word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        word_len = len(s)
        while index < word_len:
            str_len = int(s[index:index + 4])
            index += 4
            decoded_str = s[index: index + str_len]
            decoded.append(decoded_str)
            index += str_len
        return decoded

