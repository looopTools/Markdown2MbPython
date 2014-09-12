#!/usr/bin/python
def convertString(text):
#    replaceLinks(text)
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

    return text

def replaceCite(text):

    return text

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

text = "**lol**\n***bold***\n   laskdlkdalk\n   john\n>lol \n*kklsd*"
text = convertString(text)
print(text)


#print('**bold**'.replace('**', '[b]', 1))
