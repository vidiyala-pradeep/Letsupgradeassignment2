Word=input("Enter the Word:")
vowels=["a","e","i","o","u","A","E","I","O","U"]
result=""
for vowel_letter in range(len(Word)):
    if Word[vowel_letter] not in vowels:
        result = result+ Word[vowel_letter]
else:
    result = result
print(result)
