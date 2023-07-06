import YUKINA
import json
import winsound


with open('test.json') as f:
    score = json.load(fp=f)

track = []
bytestrack = b''

voice = [30000]*32 + [-30000]*32

for note in score:
    print(note)
    track = YUKINA.kernel.maid_2(voice,note)
    print('Convert Succeed')
    bytestrack += YUKINA.kernel.convert.convert(track)
YUKINA.kernel.convert.output(bytestrack,'test.wav')
winsound.PlaySound('test.wav',winsound.SND_FILENAME)
