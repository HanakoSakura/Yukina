
import sc

def osc()->list[int]:
    tmp = [0]
    tmp*=64
    while True:
        text = sc.scan_space(input('[OSC] '))
        if len(text)>0:
            if text[0] == 'exit':
                break
            if len(text)>1:
                s = text[1:]
                d = int(text[0])
                for i in s:
                    if int(i)>=0 and int(i)<64:
                        tmp[i]=d
                        pass
                    pass
                pass
            pass
        pass
    return tmp


                
                