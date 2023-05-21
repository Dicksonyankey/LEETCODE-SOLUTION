def reverse_string(s, k):
    n = len(s)
    result = []
    for i in range(0, n, 2 * k):
        # Reverse the first k characters if there are at least k characters left
        result.append(s[i:i + k][::-1]) if i + \
            k <= n else result.append(s[i:n][::-1])

        # Add the remaining characters to the result
        result.append(s[i + k:i + 2 * k]) if i + 2 * \
            k <= n else result.append(s[i + k:n])

    return ''.join(result)
