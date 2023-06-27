
# YUKINA MAIN

import tools.sc as sc
import tools.osc as osc
import kernel.maid

using_voice = [0]
using_voice*=64

work_note = []

print('--YUKINA 0.1 ALPHA--')

while True:
    text = sc.scan_space(input('YUKINA '))
    if len(text) > 0:
        if text[0] == 'exit':
            break
        if text[0] == 'osc':
            using_voice = osc.osc()
        
    
    
