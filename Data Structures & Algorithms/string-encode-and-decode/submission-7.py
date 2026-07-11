class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            string_length = len(string)
            prefix = f"{string_length: 4}"
            encoded.append(prefix + string)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        length = len(s)
        while index < length:
            str_len = int(s[index: index + 4])
            index += 4
            decoded_str = s[index: index + str_len]
            decoded.append(decoded_str)
            index += str_len
        return decoded
