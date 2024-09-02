import os
from spellchecker import SpellChecker

def check_spelling_in_file(file_path, spell_checker):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    words = content.split()
    misspelled = spell_checker.unknown(words)
    
    if misspelled:
        print(f"Misspelled words in {file_path}:")
        for word in misspelled:
            print(f" - {word}")
        print()

def check_spelling_in_repo(repo_path):
    spell_checker = SpellChecker()

    # Excluded from spell checking
    spell_checker.word_frequency.add("id,")
    spell_checker.word_frequency.add("github")
    
    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Check only text files
            if file_path.endswith(('.txt', '.md', '.py', '.html', '.css', '.js')):
                check_spelling_in_file(file_path, spell_checker)

if __name__ == "__main__":
    repo_path = input("Enter the path to the repository: ")
    check_spelling_in_repo(repo_path)
