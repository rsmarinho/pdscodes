import sys
import numpy as np

from scipy.io.wavfile import write as wav_write

audio = np.empty((0,1), dtype = np.uint8)
with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        if i == 0 or i == 1:
            print(i)
            continue
        l = list(line)
        l.remove('\n')
        ll = np.packbits(np.array(l, dtype=np.uint8))
        audio = np.vstack((audio, ll.astype(np.uint8)))

audio = np.stack(audio, axis=1)[0]
wav_write("output.wav", data=audio, rate=int(sys.argv[2]))
