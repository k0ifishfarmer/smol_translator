import random
import re
from collections import defaultdict

# Create the dictionary of replacements
# Each key is paired with a list containing every translation option
replacements = defaultdict(lambda: [], {
    "the": ["le","ze"],
    "lol": ["kek"],
    "lmao": ["lmeow"],
    "small": ["smol"],
    "my": ["mi"],
    "friend": ["fren"],
    "what": ["wat","wot"],
    "when": ["wen"],
    "why": ["y"],
    "some": ["sum"],
    "they": ["dey"],
    "the": ["tha","the","da"],
    "get": ["git"],
    "good": ["gud"],
    "bro": ["broh"],
    "believe": ["blv"],
    "won't": ["wnt"],
    "yes": ["ya"],
    "you": ["u"],
    "your": ["ur"],
    "human": ["hooman"],
    "old": ["boomer"],
    "older": ["boomer"],
    "up": ["up only"],
    "computer": ["compooter"],
    "oh": ["o"],
    "throwback": ["throw bacc"],
    "be": ["b","be"],
    "market": ["mkt","markit"],
    "squat": ["sqwat"],
    "squatting": ["sqwatting"],
    "squatter": ["sqwatter"],
    "zero": ["0"],
    "zeroed": ["0'd"],
    "something": ["smthn"],
    "thing": ["ting"],
    "personally": ["pawsonally"],
    "chocolate": ["choklet","choccy"],
    "bubble": ["booble"],
    "those": ["dose"],
    "these": ["deez"],
    "there": ["dere"],
    "their": ["deir"],
    "this": ["dis"],
    "are": ["r"],
    "bull": ["bula"],
    "bullish": ["boolish"],
    "bear": ["bera"],
    "business": ["biznis","bizniz"],
    "is": ["iz"],
    "can": ["cen","can"],
    "look": ["luk","look"],
    "like": ["like","liek"],
    "make": ["mek","make","maek"],
    "okay": ["oke"],
    "ok": ["oke"],
    "said": ["sed","said"],
    "fuck": ["fukk"],
    "fucking": ["fukkin"],
    "life": ["lief","life"],
    "think": ["tink"],
    "thank": ["tank","thank"],
    "become": ["becum","become"],
    "ready": ["reddy","ready"],
    "crypto": ["brypto"],
    "see": ["c","see"],
    "shit": ["shid"],
    "excited": ["excite","excited"],
    "right": ["rite"],
    "have": ["hav","have","heff"],
    "heart": ["hart"],
    "cute": ["kewt","cute"],
    "way": ["wei","way"],
    "please": ["pls","bls"],
    "pizza": ["pidser"]
    
    
})


def translate():
    
    text = str(input('Enter the text you want to translate: \n\n'))
    
    # Split the input text into sentences and phrases
    sentences = re.split(r'(?<=[.!?])\s', text)
    phrases = [re.split(r'(?<=[,])\s', sentence) for sentence in sentences]
    
    # Initialize an empty list for the translated words
    translated = []
    
    # Translate each phrase in each sentence
    for sentence in phrases:
        for phrase in sentence:
            words = phrase.split()
            for i, word in enumerate(words):
                # Lowercase the word
                word = word.lower()
                # Remove the "g" from words ending in "ing"
                if word.endswith('ing'):
                    # With a probability of 50%, remove the "g" from the word
                    if random.random() < 0.5:
                        word = word[:-1]
                # Look up the replacement for the word and append it to the list of translated words
                if word in replacements:
                    replacement_options = replacements[word]
                    replacement = random.choice(replacement_options) 
                    # Sometimes there are multiple options for the same word
                    translated.append(replacement)
                elif word[:-1] in replacements:
                    # avoids redundancy for plural words in dictionary
                    replacement_options = replacements[word[:-1]]
                    replacement = random.choice(replacement_options) 
                    translated.append(replacement + word[-1])
                elif i == len(words) - 1 and word[-1] in ['.', ',', '!', '?']:
                    # Edge case for last word of the sentence -> has a punctuation
                    word_without_punct = word[:-1]
                    if word_without_punct in replacements:
                        replacement_options = replacements[word_without_punct]
                        replacement = random.choice(replacement_options) 
                        translated.append(replacement + word[-1])
                    elif word_without_punct[:-1] in replacements:
                        # avoids redundancy for plural words in dictionary
                        replacement_options = replacements[word_without_punct[:-1]]
                        replacement = random.choice(replacement_options) 
                        translated.append(replacement + word_without_punct[-1] + word[-1])
                    else:
                        translated.append(word)
                else:
                    translated.append(word)
    
    return "\n" + " ".join(translated)

print(translate())
