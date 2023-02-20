#!/bin/bash

echo "Start spell check"
# aspell check README.md
printf "\n" ispell README.md -v
# ispell README.md
