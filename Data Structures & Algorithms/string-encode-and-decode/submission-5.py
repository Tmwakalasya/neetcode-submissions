class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            length = len(string)
            prefix = f"{length: 4}"
            encoded.append(prefix + string)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded_res = []
        length = len(s)
        i = 0
        while i < length:
            str_length = int(s[i: i + 4])
            i += 4

            decoded_str = s[i:i + str_length]
            decoded_res.append(decoded_str)
            i += str_length
        return decoded_res

