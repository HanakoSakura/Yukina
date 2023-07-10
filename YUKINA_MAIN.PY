import YUKINA
import json
import winsound


with open('test.json') as f:
    score = json.load(fp=f)

track = []
bytestrack = b''


track = YUKINA.Yukina_engine.synthesis(score=score)
bytestrack = YUKINA.kernel.convert.convert(track)

YUKINA.kernel.convert.output(bytestrack,'test.wav')

winsound.PlaySound('test.wav',winsound.SND_FILENAME)
