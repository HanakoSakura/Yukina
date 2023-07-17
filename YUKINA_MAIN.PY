import YUKINA
import json
import winsound

voice = {}
with open('voice.json') as f:
    voice = json.load(f)

YUKINA.voice.VOICE = { **YUKINA.voice.VOICE , **voice }

file = input('>')

with open(file+'.json') as f:
    score = json.load(fp=f)

track = []
bytestrack = b''


track = YUKINA.Yukina_engine.synthesis(score=score)
bytestrack = YUKINA.kernel.convert.convert(track)

YUKINA.kernel.convert.output(bytestrack,file+'.wav')

winsound.PlaySound(file+'.wav',winsound.SND_FILENAME)
