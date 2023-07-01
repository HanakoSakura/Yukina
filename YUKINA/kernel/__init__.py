from . import convert,CurseLib

def maid(w:list[int],ctrl:dict)->list[int]:
    tmp = w
    if ctrl.get('freq') != None:
        tmp = CurseLib.freq(tmp,ctrl['freq'])
    if ctrl.get('vol') != None:
        tmp = CurseLib.vol(tmp,ctrl['vol'])
    if ctrl.get('size') != None:
        tmp = CurseLib.repeat(tmp,ctrl['size'])
    return tmp