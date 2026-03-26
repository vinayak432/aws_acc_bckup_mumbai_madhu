#!/bin/bash

files=`ls -lrt | awk -F " " 'NR>2 {print $NF}'`
echo " list of filenames 
$files"

delete
