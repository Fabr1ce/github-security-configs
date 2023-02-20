from spellchecker import SpellChecker

spell = SpellChecker()

# # Mention the language keyword
# tool = language_check.LanguageTool('en-US')
# i = 0

# Path of file which needs to be checked
with open(r'README.md', 'r') as f:
   for line in f:
        # matches = tool.check(line)
        # i = i + len(matches)
        # pass
        # find those words that may be misspelled
        misspelled = spell.known(line)
        print(misspelled)

for word in misspelled:
	# Get the one `most likely` answer
	print(spell.correction(word))

	# Get a list of `likely` options
	print(spell.candidates(word))
