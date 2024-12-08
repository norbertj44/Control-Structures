# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU" #vowel to samogloska
vowel_count = 0

# Count vowels in the text using while loop
i = 0
while i < len(text): #dopoki 'i' bedize mniejsze od ilosci znakow 'text', to:
    char = text[i] #znaki = tekst od 1 do konca tekstu
    if char in vowels:
        vowel_count += 1
    i += 1

print(f"The number of vowels in the text is: {vowel_count}")
