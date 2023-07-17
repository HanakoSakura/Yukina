# encoding="utf-8"

from . import kernel,pitch,voice
import matplotlib.pyplot as plt

def synthesis(score:dict)->list[int]:
    '''YUKINA Synthesis Main Curse'''
    
    # Get Global Voice
    useVoice = score.get('use voice',voice.VOICE['default'])
    if useVoice == 'default':
        print('Cannot find Use VOice')
    # Get Score (list)
    useScore = score.get('score')
    # Get Global Beat Unit
    useBeat = score.get('beat',640)
    
    track = []
    
    i = 0
    
    i+=1
    p = int(i/len(useScore)*100)
    print('\rSynthesis',end=' |')
    print('#'*p,end='')
    print(' '*(100-p)+'|',len(useScore)-i,end='   ')
    
    for note in useScore:
        # Get note parameters
        
        Voice = note.get('voice')
        if voice.VOICE.get(Voice)==None :
            Voice = voice.VOICE.get(useVoice)
        else :
            Voice = voice.VOICE.get(Voice)
        
        
        freq = note.get('pitch')
        if freq==None :
            freq = 1000.0
        if type(freq)==str :
            freq = 440*(2**(pitch.PITCH[freq]/12))
        
        vol = note.get('vol')
        if vol==None:
            vol = 1.0
        
        delay = note.get('beat')
        if delay==None:
            delay = 1
        
        # Start synthesis
        tmp = Voice
        if vol != 1.0:
            tmp = kernel.CurseLib.vol(tmp,vol)
        tmp = kernel.CurseLib.freq(tmp,freq/100.0)
        tmp = kernel.CurseLib.repeat(tmp,delay*useBeat)
        track += tmp
        
        
        i+=1
        p = int(i/len(useScore)*100)
        print('\rSynthesis',end=' |')
        print('#'*p,end='')
        print('_'*(100-p)+'|',len(useScore)-i,end='   ')
        
    print('')
    return track
        
        

