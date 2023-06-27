# YUKINA / ゆきな

Sound synthesis.

Sorry, the two main scripts have not been written yet.

However, Python can be used to directly call functions for sound synthesis.

Here is a sample.

``` python

import kernel.convert
import kernel.maid

voice = [32760]*32
voice += [0]*32

note = kernel.maid.maid(voice,{'size':64000})

bytestrack = kernel.convert.convert(note)

outfile='test.wav'

kernel.convert.output(bytestrack,outfile)

```

