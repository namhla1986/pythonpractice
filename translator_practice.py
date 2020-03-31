def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter your word: ")))
# Remember that indentation REALLY matters! This was just a translator to test whether any vowels could be
# found in the strings that were inputted by the user. The vowels would be replaced with the letter g.I had
# to create a function called translate and use both the for loop and if statement to test the theory