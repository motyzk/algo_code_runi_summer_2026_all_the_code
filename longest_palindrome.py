def solve(s):
    start_longest = end_longest = 0
    for i in range(len(s)):
        for k in range(2):
            curr_start_longest, curr_end_longest = i, i + k
            while (curr_start_longest >= 0 and
                   curr_end_longest < len(s) and
                s[curr_start_longest] == s[curr_end_longest]):
                    curr_start_longest -= 1
                    curr_end_longest += 1
            curr_start_longest += 1
            if curr_end_longest - curr_start_longest > end_longest - start_longest:
                end_longest, start_longest = curr_end_longest, curr_start_longest
    return s[start_longest: end_longest]

assert solve("cabad") == "aba"
assert solve("caad") == "aa"
# example input 2 - “aacd”      output “aa”
# example input 3 - “aac”        output “aa”
# example input 4 - “babad”    output “aba” or “bab”
