n = int(input("Enter the number of pairs of words: "))

synonyms = {}
for i in range(n):
    pair = input(f"Enter the {i+1} pair: ").split()
    synonyms[pair[0].lower()] = pair[1].lower()
    synonyms[pair[1].lower()] = pair[0].lower()
while True:
    word = input("Enter a word: ").lower()
    if word in synonyms:
        print("Synonym:", synonyms[word])
        break
    else:
        print("There is no such word in the dictionary.")