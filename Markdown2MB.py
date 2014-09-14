#!/usr/bin/python

import re

def convertString(text):
    text = replaceLinks(text)
    text = replaceFootnotes(text)
    text = replaceCite(text)
    text = replaceCode(text)
    text = replaceBold(text)
    text = replaceItalic(text)

    return text

def replaceBold(text):

    lines = text.splitlines()
    j = 0

    for x in range(0, len(lines)):
        if '***' in lines[x] and j == 0:
            lines[x] = lines[x].replace("***", "[b]*", 1)
            j = 1
        if '***' in lines[x] and j == 1:
            lines[x] = lines[x].replace("***", "*[/b]", 1)
            j = 0
        if '**' in lines[x] and j == 0:
            lines[x] = lines[x].replace("**", "[b]", 1)
            j = 1
        if '**' in lines[x] and j == 1:
            lines[x] = lines[x].replace("**", "[/b]", 1)
            j = 0
    return '\n'.join(lines)

def replaceItalic(text):

    lines = text.splitlines()
    j = 0

    for x in range(0, len(lines)):
        if '*' in lines[x] and j == 0:
            lines[x] = lines[x].replace('*', '[i]', 1)
            j = 1
        if '*' in lines[x] and j == 1:
            lines[x] = lines[x].replace('*', '[/i]', 1)
            j = 0
    return '\n'.join(lines)

def replaceLinks(text):

    lines = text.splitlines()
    lines = text.splitlines()

    for x in range(0, len(lines)):
       lines[x] = re.sub(r'\[([^]]*)\]\((.*?)\/?\)', r'[link=\2]\1[/link]', lines[x])

    return '\n'.join(lines)

def replaceCode(text):

    codeStarted = False
    lines = text.splitlines()

    for x in range(0, len(lines)):
        if lines[x].startswith('   '):
            if not codeStarted:
                lines[x] = lines[x].replace(lines[x], '[code]\n' + lines[x])
                codeStarted = True
        elif not lines[x].startswith('   ') and codeStarted:
            lines[x] = lines[x].replace(lines[x], '[/code]\n' + lines[x])
            codeStarted = False

    if codeStarted:
        return '\n'.join(lines) + '\n[/code]'
    else:
        return '\n'.join(lines)

def replaceCite(text):
    lines = text.splitlines()
    for x in range(0, len(lines)):
        if lines[x].startswith('>'):
            lines[x] = lines[x][:0] + '[citat]' + lines[x][1:] + '[/citat]\n'

    return '\n'.join(lines)

def replaceFootnotes(text):
    lines = text.splitlines()

    footnoteNumber = 1
    for x in range(0, len(lines)):
        lines[x] = re.sub(r'\[([^]]*)\] \[(.*?)\/?\]', r'[^X]', lines[x])
        if re.match('\[[0-9]*\]', lines[x]):
            lines[x] = lines[x].replace("[{}]".format(footnoteNumber), "[^{}]".format(footnoteNumber), 1)
            footnoteNumber = footnoteNumber + 1

    footnoteNumber = 1
    for x in range(0, len(lines)):
        while '[^X]' in lines[x]:
            lines[x] = lines[x].replace("[^X]", "[^{}]".format(footnoteNumber), 1)
            footnoteNumber = footnoteNumber + 1
    return '\n'.join(lines)
