#-*-coding:utf-8 -*-

def scan_space(s:str)->list[str]:
    tmp = []
    m = ''
    flag = 'space'
    s+=' '
    for i in s:
        if i == '\'' and flag == 'space':
            m+=i
            flag = 'string'
        elif i == '\'' and flag == 'string':
            m+=i
            tmp.append(m)
            m = ''
            flag = 'space'
        elif i == ' ' and flag == 'word' :
            tmp.append(m)
            m = ''
            flag = 'space'
        elif i == '\t' and flag == 'word' :
            tmp.append(m)
            m = ''
            flag = 'space'
        elif i != ' ' :
            if flag != 'string' :
                flag = 'word'
            m+=i
    return tmp
