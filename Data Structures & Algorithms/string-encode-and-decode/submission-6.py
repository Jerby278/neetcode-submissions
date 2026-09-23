class Solution:

    def encode(self, strs: List[str]) -> str:
        lst = []
        for word in strs:
            lst.append(str(len(word)))
            lst.append("#")
            lst.append(word)
        return "".join(lst)

    def decode(self, encoded_str: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(encoded_str):
            j = i
            while encoded_str[i] != "#":
                i += 1

            decoded_str.append(encoded_str[i+1:(int(encoded_str[j:i]) + i+1)])
            i += int(encoded_str[j:i])+1

        return decoded_str
