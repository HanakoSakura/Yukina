from . import convert,CurseLib,pitch

def maid(w:list[int],ctrl:dict)->list[int]:
    tmp = w
    print('|####',end='')
    if ctrl.get('freq') != None:
        tmp = CurseLib.freq(tmp,ctrl['freq'])
    print('####',end='')
    if ctrl.get('vol') != None:
        tmp = CurseLib.vol(tmp,ctrl['vol'])
    print('####',end='')
    if ctrl.get('size') != None:
        tmp = CurseLib.repeat(tmp,ctrl['size'])
    print('####',end='|\n')
    return tmp


def maid_2(w:list[int],ctrl:dict)->list[int]:
    tmp = w
    print('|####',end='')
    if ctrl.get('pitch') != None:
        freq = 440*(2**(pitch.PITCH[ctrl['pitch']]/12))
        tmp = CurseLib.freq(tmp,freq/1000)
    print('####',end='')
    if ctrl.get('vol') != None:
        tmp = CurseLib.vol(tmp,ctrl['vol'])
    print('####',end='')
    if ctrl.get('beat') != None:
        tmp = CurseLib.repeat(tmp,ctrl['beat']*640)
    else:
        tmp = CurseLib.repeat(tmp,640)
    print('####',end='|\n')
    return tmp

