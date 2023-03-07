#! /usr/bin/env python3
# Maxval accounts value evaluator - Raymond de Groat, 2023 https://github.com/raydegroat

from pathlib import Path
import os

dir_name = 'account_history'

# Use Path to list files matching pattern
dir_list = Path(dir_name).glob('*.csv')
for file in dir_list:
    print(file)
    f = open(file, 'r')
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        line_parts = line.strip().split(',')
        print(line_parts)
        print()
