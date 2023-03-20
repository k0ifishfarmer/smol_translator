# smol_translator
This is a simple text translation program that takes input text and translates it into smol.

-----------------------------------------------------------------------------------------------------------------------------------------------------
# Help Wanted
I am looking for help to improve the translation dictionary used by the script. If you are proficient in smol, please feel free to contribute by adding new translations or improving existing ones.

Additionally, I would appreciate any help in optimizing the code and finding any potential issues that could cause errors or inconsistencies in the translations. If you find any bugs or have suggestions for improving the code, please open an issue or submit a pull request.

Thank you for your contributions and help in making this project better!
-----------------------------------------------------------------------------------------------------------------------------------------------------

This code:
  1. Uses the **`input()`** function to prompt the user to enter some text to translate, and then stores that text as a string in the **`text`** variable.
  2. Uses regular expressions to split the input text into a list of sentences and then split each sentence into a list of phrases.
  3. Initializes an empty list called **`translated`**.
  4. Loops through each phrase in each sentence, and for each word in each phrase:

      a. Converts the word to lowercase if it starts with an uppercase letter.

      b. Looks up the word in a pre-defined dictionary called **`replacements`**, which maps certain words to a list of replacement options.

      c. If the word is in the **`replacements`** dictionary, randomly selects one of the replacement options and appends it to the **`translated`** list.

      d. If the word is not in the **`replacements`** dictionary, appends the original word to the **`translated`** list.

  5. Joins the **`translated`** list into a single string with spaces between the words, and returns that string with a newline character at the beginning
