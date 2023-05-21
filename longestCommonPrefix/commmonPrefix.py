def longestCommonPrefix(strs: list[str]) -> str:
    count = 0
    prefix = ""

    while count < len(strs[0]):
        for s in strs:
            if count == len(s) or s[count] != strs[0][count]:
                return prefix
        prefix += strs[0][count]
        count += 1

    return prefix
