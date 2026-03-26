#!/bin/bash

echo "enter the pattern to search in a file"
read pat

grep -l -r "$pat" * > outpat
if [ $? -eq 0 ]
then
echo "$pat Pattern found in below files"
cat outpat
else
echo "$pat is not found in any of the files"
fi
