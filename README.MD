# YUKINA / ゆきな

Sound synthesis.

Sorry, the two main scripts have not been written yet.

However, Python can be used to directly call functions for sound synthesis.

Here is a sample.

``` python
import YUKINA

voice = [30000]*32 + [-30000]*32

track = []
track += YUKINA.kernel.maid(voice,{'size':64000})

bytestrack = YUKINA.kernel.convert.convert(track)

YUKINA.kernel.convert.output(bytestrack,'test.wav')
```
