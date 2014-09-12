#!/usr/bin/python
def convertString(text):
#    replaceLinks(text)
    text = replaceCite(text)
    text = replaceCode(text)
    text = replaceBold(text)
    text = replaceItalic(text)

    return text

def replaceBold(text):

    index = 0
    j = 0

    while index < len(text) - 1:

        if index < len(text) - 2:
            if (text[index] == '*' and text[index + 1] == '*' and text[index + 2] == '*') or (text[index] == '_' and text[index + 1] == '_' and text[index + 2] == '_'):
                regEx = ''
                if(text[index] == '*'):
                    regEx = '*'
                if j == 0:
                    text = text[:index] + '[b]' + text[index+2:]
                    j = 1
                else:
                    text = text[:index+1] + '[/b]' + text[index+3:]
                    j = 0
        elif (text[index] == '*' and text[index + 1] == '*') or (text[index] == '_' and text[index + 1] == '_'):
               regEx = ''
               if text[index] == '*':
                   regEx = '**'
               else:
                   regEx = '__'
               if j == 0:
                   text = text.replace(regEx, '[b]', 1)
                   j = 1
               else:
                   text = text.replace(regEx, '[/b]', 1)
                   j = 0
        index = index + 1
    return text

def replaceItalic(text):

    index = 0
    j = 0

    while index < len(text) - 1:
        if ( text[index] == '*' and text[index + 1] != '*' ) or (text[index] == '_' and text[index + 1] != '_'):
            regEx = ''
            if text[index] == '*':
                regEx = '*'
            else:
                regEx = '_'

            if j == 0:
                text = text.replace(regEx, '[i]', 1)
                j = 1
            else:
                text = text.replace(regEx, '[/i]', 1)
                j = 0
        index = index + 1
    if (text[index] == '*' or text[index] == '_') and j == 1:
        text = text.replace(regEx, '[/i]', 1)
    return text

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

text = "**lol**\n***bold***\n   laskdlkdalk\n   john\n>lol"
text = convertString(text)
print(text)


#print('**bold**'.replace('**', '[b]', 1))
