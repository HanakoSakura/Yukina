import traceback

try:

    import YUKINA
    import json
    import winsound
    import sys

    voice = {}
    with open('voice.json') as f:
        voice = json.load(f)

    YUKINA.voice.VOICE = { **YUKINA.voice.VOICE , **voice }

    if len(sys.argv)>=3 and sys.argv[1]=='--input' :
        file = sys.argv[2]
    else:
        file = input('>')

    with open(file+'.json') as f:
        score = json.load(fp=f)

    track = []
    bytestrack = b''


    track = YUKINA.Yukina_engine.synthesis(score=score)
    bytestrack = YUKINA.kernel.convert.convert(track)

    YUKINA.kernel.convert.output(bytestrack,file+'.wav')

    if not '--noplay' in sys.argv:
        winsound.PlaySound(file+'.wav',winsound.SND_FILENAME)

except Exception:
    tb = traceback.format_exc()
    print('Something error.\n',tb)
