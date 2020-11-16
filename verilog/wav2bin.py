import sys
from scipy.io import wavfile
import numpy as np

if(int(sys.argv[1]) == 1):
    sr1, data_arroz_feijao = wavfile.read('../LDC2006S16.wav')
    data_int_arroz_feijao = (data_arroz_feijao).astype(np.int16)
    for k in range(0, len(data_int_arroz_feijao)):
        # print(*np.unpackbits((data_int_arroz_feijao[k]>>8).astype(np.uint8)), sep = '')
        data_int = ((data_int_arroz_feijao[k].astype(np.double) / 32768 + 1)/2 * 255).astype(np.uint8)
        print(*np.unpackbits((data_int)), sep = '')
        # print(f'{data_int_arros_feijao[k].astype(np.int8): b}')

elif(int(sys.argv[1]) == 2):
    sr2, data_caprice = wavfile.read('../caprice24mono.wav')
    data_int_caprice = np.floor(data_caprice*255).astype(np.int8)
    for k in range(0, len(data_int_caprice)):
        print(*np.unpackbits(data_int_caprice[k].astype(np.uint8)), sep = '')
        # print(f'{data_int_caprice[k].astype(np.int8): b}')

else:
    print(error)
