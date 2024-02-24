# Coverletter-Yap
Remixes premade text while replacing flagged words with designated values

# Uses
- Make a generic cover letter and replace flagged words with chosen names/words
- Give variety in paragraphs

# How to use
After Install Python and this repository:
1. Edit Flag string and Key dictionary in main.py file to desired values
2. Edit the text inside of each of the paragraph folders inside of user_name
3. Run code, and enjoy the output on output.txt

# Simplest Way to Sub-Values (Avoids Remixes)
- Set paragraphs variable to 0
- Choose your key and flag it appropriately
- Inside the introduction folder, keep only 1.txt and paste everything inside
- Keep the Conclusion folder, but make the Txt files empty

# How to Set Up Folders
- Inside the user_name folder, there is the introduction and conclusion folder, and there are the paragraph folders.
  - It is crucial that the name introduction, and conclusion stay the same
  - It is crucial that the name of the paragraph folders is always paragraph_n; n ranging from 1 to the number of paragraphs
- Inside each of the paragraph folders, there is a selection of txt files numbered from 1 - n
  - The text within each of the txt files can be edited as pleased
  - It is crucial that the files are named consecutively starting from 1
  - The amount of options in each paragraph can be customized based on preference, files can be deleted on will, but they need to be numbered appropriately

# How to set up flags/keys
- The flag variable tells my code when to check for a key
- The key variable is substituted by its corresponding value in the dictionary, also the whole word is replaced with a string
- The flag and key variables can be edited based on preference
- The current example uses the return based on chat gpt's output which gives me stuff in [Company Name]
- Make sure there are no spaces inside a key
