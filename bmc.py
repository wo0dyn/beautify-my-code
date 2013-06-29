# -*- coding: utf8 -*-

"""
Beautify My Code

Authors:
* Mathieu Agopian
* Nicolas Dubois
"""

import re
import sys

rules = (
    (r'(\S+)\s*\*\*\s*1', r'\1'),  # ^1
    (r'(\S+)\s*\*\*\s*2', r'\1²'),  # square
    (r'(\S+)\s*\*\*\s*3', r'\1³'),  # cube
    (r'(\S+)\s*>=\s*(\S+)', r'\1 ≥ \2'),  # ge
    (r'(\S+)\s*<=\s*(\S+)', r'\1 ≤ \2'),  # le
    (r'(\S+)\s*!=\s*(\S+)', r'\1 ≠ \2'),  # ne
    (r'(\S+)\s*(?<!=)=(?!=)\s*(\S+)', r'\1: \2'),  # assignment
    (r'(\S+)\s*==\s*(\S+)', r'\1 = \2'),  # eq
    (r'(\S+)\s*\/\/\s*(\S+)', r'\1 ÷ \2'),  # div
)

rules = ((re.compile(rule), replace) for rule, replace in rules)

content = open(sys.argv[1], 'r').read()
for rule, replace in rules:
    content = rule.sub(replace, content, re.MULTILINE)
print(content)
