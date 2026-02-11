def find_duplicates(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for char, count in freq.items():
        if count > 1:
            print(char, "-", count)

# Example
find_duplicates("programming")
