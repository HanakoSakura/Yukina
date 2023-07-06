from . import convert,CurseLib

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