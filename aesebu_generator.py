# import scipy.io.wavfile as waves
import wave
import array
import io

Stream_out = open("aesebu_output.aes", "w")

""" Preambles """
PR_X0 = int('11100010', 2)
PR_X1 = int('00011101', 2)
PR_Y0 = int('11100100', 2)
PR_Y1 = int('00011011', 2)
PR_Z0 = int('11101000', 2)
PR_Z1 = int('00010111', 2)

""" Leemos el audio """
audio = wave.open('muestra2448.wav')
""" Calculamos el numero de muestras """
nframes = audio.getnframes()
""" Almacenamos las muestras en bytes """
muestras_audio = audio.readframes(nframes)

""" Creamos un array vacio de 192 posiciones donde incluiremos Subframes """
Frames = [None] * 192

""" Iteramos sobre el bucle para introducir los campos en cada subframe """
for Subframes in Frames:
    if Subframes = 0:
        DATA.push(PR_Z0)
    else:
        if Subframe % 2 == 0:
            DATA.push(PR_X0)
        else:
            DATA.push(PR_Y0)

    DATA.push(muestras_audio)
""Prueba de rama"
    DATA.push(valid = 0)
    DATA.push(user = 0)
    DATA.push(channel = 'R o L')
    DATA.push(parity = 0)

""" Pasamos todo a nivel de byte """
Stream_out.write(bytes(DATA))

Stream_out.close()

