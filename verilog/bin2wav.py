import sys
import numpy as np

from scipy.io.wavfile import write as wav_write

audio = np.empty([])
with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        if(i == 0):
            continue
        #print(int(line,2)-int(128))
        audio = np.vstack((audio, (int(line, 2)-int(128))))

wav_write("output.wav", data=audio, rate=int(sys.argv[2]))
