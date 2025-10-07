def encode(strs):
    result = ""
    for s in strs:
        result += str(len(strs)) + "#" + s
    return result
def decode(s):
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        word = s[j+1:j+1+length]
        result.append(word)
        i = j + 1 + length
    return result
s=encode(["neet","code","love","you"])
print(encode(["neet","code","love","you"]))
print(decode(s))