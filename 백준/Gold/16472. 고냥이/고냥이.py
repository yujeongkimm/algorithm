n = int(input())
sequence = input()

alphabet_count = [0] * 26
next_index = 0
ans=0

def count_unique(alphabet_count):
    unique = 0
    for i in range(26):
        if alphabet_count[i] > 0:
            unique += 1
    return unique


for i in range(len(sequence)):
    while next_index < len(sequence):
        alphabet_count[ord(sequence[next_index]) - ord('a')] += 1
        next_index += 1

        if count_unique(alphabet_count) > n:
            next_index -= 1
            alphabet_count[ord(sequence[next_index]) - ord('a')] -= 1
            break

    ans = max(ans, next_index - i)
    alphabet_count[ord(sequence[i]) - ord('a')] -= 1

print(ans)