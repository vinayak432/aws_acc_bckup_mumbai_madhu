#!/bin/bash

echo $0
echo $0 | awk -F "/" '{print $NF-1}'
echo $1 $2 $# $* $@ $? $! $0 $$
