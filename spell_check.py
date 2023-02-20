# from spellchecker import SpellChecker
#
# spell = SpellChecker()
#
# # find those words that may be misspelled
# misspelled = spell.unknown(["cmputr", "watr", "study", "wrte"])
# # misspelled = spell.unknown('words.txt')
#
# for word in misspelled:
# 	# Get the one `most likely` answer
# 	print(spell.correction(word))
#
# 	# Get a list of `likely` options
# 	print(spell.candidates(word))

import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

text = "word txt"

# get the matches
matches = tool.check(text)

matches
