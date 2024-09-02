#!/bin/bash

echo "Start spell check"
# printf "X\n" | aspell check README.md
# echo "second"
printf "X\n" ispell README.md
# ispell README.md
echo "Spell check complete!"

pip install pyspellchecker

python spell_check.py .
