def convertString(text):
#    replaceLinks(text)
#    replaceCite(text)
#    replaceCode(text)
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

    return text


text = "***bold***"
text = convertString(text)
print(text)


#print('**bold**'.replace('**', '[b]', 1))
