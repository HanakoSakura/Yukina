# encoding="utf-8"

from math import sin,pi,floor

def sinc(x:float)->float:
    if x == 0.0 :
        return 1.0
    return sin(x*pi)/(x*pi)

def resampling(w:list[int], step:float)->int:
    s = 0.0
    i = 0.0
    for sample in w:
        s += float(sample)*sinc(step-i)
        i+=1.0
        pass
    return int(s)

def vol(w:list[int], power:float):
    tmp = []
    for sample in w:
        tmp.append(int(sample*power))
    return tmp

def freq(w:list[int], step:float)->list[int]:
    if step<=0.0 or step == 1.0 or len(w)==0 :
        return w
    tmp = []
    offset = 0.0
    while offset<float(len(w)):
        tmp.append(resampling(w,offset))
        offset+=step
        pass
    return tmp

def freq_line(w1:list[int], step:float)->list[int]:
    if step<=0.0 or step == 1.0 or len(w1)==0 :
        return w1
    w = w1
    w += [0]
    tmp = []
    offset = 0.0
    k=b=x=0
    while offset+1 < len(w):
        b = w[floor(offset)]
        k = w[floor(offset)+1] - b
        x = offset - floor(offset)
        tmp.append(int(k*x+b))
        offset+=step
    
    return tmp

def repeat(w:list[int],new_size:int)->list[int]:
    ret = w
    while len(ret)<new_size:
        ret+=w
    return ret[:new_size]

def OLA(w:list[int],power:float,cut_size:int)->list[int]:
    if power<=0.0 or power==1.0 :
        return w
    window = []
    ret = []
    offset = 0
    i = 0
    while offset+cut_size<len(w) :
        window = w[offset:offset+cut_size]
        ret+=window
        offset+=int(power*cut_size)
        pass
    if offset<len(w):
        ret+=w[offset:len(w)]
    return ret
