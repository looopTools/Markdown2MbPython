#!/usr/bin/python
#Copyright (c) 2014, Lars Nielsen / looop / looopTools / nyx
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:

#* Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.

#* Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
