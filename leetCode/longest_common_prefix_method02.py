def longest_common_prefix(strs):
    longest_prefix = ""
    if not strs: return longest_prefix
    shortest_strs = min(strs, key=len)
    for i in range(len(shortest_strs)):
        if all([x.startswith(shortest_strs[:i + 1]) for x in strs]):
            longest_prefix = shortest_strs[:i + 1]
        else:
            break
    return longest_prefix


if __name__ == "__main__":
    inp = ['flower', 'flow', 'flight']
    res = longest_common_prefix(inp)
    print(res)
