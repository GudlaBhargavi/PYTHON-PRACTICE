text = input("Enter string: ")
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)