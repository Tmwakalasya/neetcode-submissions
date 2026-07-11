class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            length = len(word)
            prefix = f"{length:4}"
            encoded.append(prefix + word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        length = len(s)
        while index < length:
            prefix = int(s[index:index + 4])
            index += 4
            decoded_word = s[index:index + prefix]
            decoded.append(decoded_word)
            index += prefix
        return decoded
