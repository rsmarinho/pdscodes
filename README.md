# pdscodes

Code snippets and notebooks used in PDS classes.

All (almost) codes are in Python3 language.

If you want to run the examples locally, I recomend you to use an python environment as follows:

### On linux
1. Create and enter virtual environment
  * `virtualenv --clear env`
  * `source env/bin/activate`
2. Install adam requirements to the virtual env
  * `pip install -r requirements.txt
3. Install plugin requirements to the virtual env
  * ufpbots example: `pip install -r ufpbots/requirements.txt`

---

## Sampling and quantization
- [quantization](https://github.com/rsmarinho/pdscodes/blob/master/quantization.py): 1d signal quantization examples
- [quantization2](https://github.com/rsmarinho/pdscodes/blob/master/quantization2.py): 2d signal quantization examples
- [nyquist](https://github.com/rsmarinho/pdscodes/blob/master/nyquist.py): Shannon-Nyquist Sampling Theorem examples

## Signals and operations
- [impulse](https://github.com/rsmarinho/pdscodes/blob/master/impulse.py): Impulse signal examples
- [step](https://github.com/rsmarinho/pdscodes/blob/master/step.py): Step signal examples
- [operations](https://github.com/rsmarinho/pdscodes/blob/master/operations.py): Signal operations examples
- [convolution](https://github.com/rsmarinho/pdscodes/blob/master/convolution.py): Convolution function example

## Discrete Fourier
- [dft](https://github.com/rsmarinho/pdscodes/blob/master/dft.ipynb) (jupyter notebook): Discrete Fourier Transform notebook
- [fft](https://github.com/rsmarinho/pdscodes/blob/master/fft.ipynb) (jupyter notebook): Fast Fourier Transform notebook

## Homework (Trabalhos Práticos)
All home works are jupyter notebooks. These files can be opened using google-colab.

- [TP01](https://github.com/rsmarinho/pdscodes/blob/master/TP01.ipynb) - Convolução linear de duas dimensões.
- [TP02](https://github.com/rsmarinho/pdscodes/blob/master/TP02.ipynb) - Efeitos de operações lineares em sinais de audio
- [TP03](https://github.com/rsmarinho/pdscodes/blob/master/TP03.ipynb) - Quantização Lei-A e Lei-u
- [TP04](https://github.com/rsmarinho/pdscodes/blob/master/TP04.ipynb) - Fuções de Janelamento
- [TP05](https://github.com/rsmarinho/pdscodes/blob/master/TP05.ipynb) - Espectrograma
- [TP07](https://github.com/rsmarinho/pdscodes/blob/master/TP07.ipynb) - Aplicações de modulação digital em sistemas de comunicação
- [TP08](https://github.com/rsmarinho/pdscodes/blob/master/TP08.ipynb) - Processamento e Compactação de imagem
---

## Auxiliary files
- [arroz e feijao](https://github.com/rsmarinho/pdscodes/blob/master/LDC2006S16.wav): Audio wave file used in some examples (SPOLTECH audio file)
- [barbara](https://github.com/rsmarinho/pdscodes/blob/master/barbara.png): Image (png) file used in some examples
- [paganini](https://github.com/rsmarinho/pdscodes/blob/master/caprice24mono.wav): Audio wave file used in some examples (from wikimedia)
- [table notes](https://github.com/rsmarinho/pdscodes/blob/master/notas_musicais.jpg): Image containing the frequencies of musical tones. Don't know the author.
- [transmission](https://github.com/rsmarinho/pdscodes/blob/master/transmission.wav): Recorded example used in TP07
- [lena](https://github.com/rsmarinho/pdscodes/blob/master/lena512.png): Image (png) file used in TP08

## TODO
- Melhorar exemplo operations.py. Exemplo não está tão claro como deveria estar (pouco eficiente na apresentacao).
- TP02.ipynb: Adicionar/melhorar os comentários e comandos de questões.

