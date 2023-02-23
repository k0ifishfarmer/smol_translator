import random
import re
from collections import defaultdict

# Create the dictionary of replacements
# Each key is paired with a list containing every translation option
replacements = defaultdict(lambda: [], {
    "lol": ["kek"],
    "lmao": ["lmeow"],
    "small": ["smol"],
    "my": ["mi"],
    "friend": ["fren"],
    "what": ["wat"],
    "when": ["wen"],
    "some": ["sum"],
    "they": ["dey"],
    "get": ["git"],
    "good": ["gud"],
    "bros": ["brohs"],
    "believe": ["blv"],
    "won't": ["wnt"],
    "yes": ["ya"],
    "you": ["u"],
    "human": ["hooman"],
    "old": ["boomer"],
    "older": ["boomer"],
    "the": ["le","ze"],
    "up": ["up only"],
    "computer": ["compooter"],
    "oh": ["o"],
    "throwback": ["throw bacc"],
    "be": ["b"],
    "market": ["mkt"],
    "squat": ["sqwat"],
    "squatting": ["sqwatting"],
    "squatter": ["sqwatter"],
    "zero": ["0"],
    "zeroed": ["0'd"],
    "something": ["smthn"],
    "personally": ["pawsonally"],
    "chocolate": ["choklet"],
    
})


def translate():
    
    text = str(input('Enter the text you want to translate: \n\n'))
    
    # Split the input text into sentences and phrases
    sentences = re.split(r'(?<=[.!?])\s', text)
    phrases = [re.split(r'(?<=[,])\s', sentence) for sentence in sentences]
    
    # Initialize an empty list for the translated words
    translated = []
    #print(phrases)
    # Translate each phrase in each sentence
    for sentence in phrases:
        #print (sentence[-1])
        for phrase in sentence:
            words = phrase.split()
            for word in words:
                # Lowercase the word if it starts with an uppercase letter
                #if word[0].isupper():
                word = word.lower()
                # Look up the replacement for the word and append it to the list of translated words
                if word in replacements :
                    replacement_options = replacements[word]
                    replacement = random.choice(replacement_options) 
                    # Sometimes there are multiple options for the same word
                    translated.append(replacement)
                elif word[:-1] in replacements :
                    # avoids redundancy for plural words in dictionary
                    replacement_options = replacements[word[:-1]]
                    replacement = random.choice(replacement_options) 
                    translated.append(replacement+word[-1])
                # Edge case for last word of the sentence -> has a punctuation and can be plural   
                elif word == words[-1] and word[:-2] in replacements :
                    replacement_options = replacements[word[:-2]]
                    replacement = random.choice(replacement_options) 
                    translated.append(replacement+word[-2]+word[-1])
                # If not, just append the original word to the list of translated words
                else:
                    translated.append(word)
    
    return "\n" + " ".join(translated)

print(translate())

