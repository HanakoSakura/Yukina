# encoding="utf-8"

import ctypes
import wave

def convert(w:list[int])->bytes:
    return bytes((ctypes.c_int16 * len(w))(*w))

def output(s:bytes,file_name:str)->None:
    f =wave.open(file_name,'wb')
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(64000)
    f.writeframes(s)
    f.close()
