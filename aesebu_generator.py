# import scipy.io.wavfile as waves
import wave
import array
import io

Stream_out = open("aesebu_output.aes", "w")

""" Preambles preformados"""
PR_X0 = int('11100010', 2)
PR_X1 = int('00011101', 2)
PR_Y0 = int('11100100', 2)
PR_Y1 = int('00011011', 2)
PR_Z0 = int('11101000', 2)
PR_Z1 = int('00010111', 2)

""" Predefinir el apartado Channel (Opciones)"""
def chanel_buffer()
    chanel = []
    chanel.apend(1,0,0,0,0,1)
    if audio == 48
        chanel.apend(0,1)
    elsif audio == 44.1
        chanel.apend(1,0)
    elseif audio = 32
        chanel.apend(1,1)
    end if
    
    chanel.apend(0,0,0,1,0,0,0,1)
    
return chanel
"""" Colas preformadas"""
def cola (frame)
    Validation = int('0',2)
    User = int('0',2)
    Chanel = chanel[frame]
    Validation
    cola.push(Validation)
    cola.push(User)
    cola.push(Chanel)
    cola.push(Parity)
    
return cola




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

