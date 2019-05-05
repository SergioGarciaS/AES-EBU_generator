import wave
import array
import io
import random
import sys


# AQUI SE INCLUYE EL APARTADO DE OPCIONES.

if len(sys.argv) != 3:
    sys.exit("Usage : $ python3 prueba.py Frequency bits")



"""Stream_out = open("aesebu_output.aes", "w")"""

audio_r = []
for i in range(0,4880):
    audio_r.append(random.randint(0,1))


def parity (i):
    len = 0
    for j in i:
        if j == 1:
            len +=1
    if  len %2 == 0:
        parity = 0
    else:
        parity = 1

    return int(parity)

def arrayChannel(wav, b_wav):
    print("WAV ES: ", wav)
    print("b_wav es: ",b_wav)
    chanel = [1,0,0,0,0,0]
    " Definimos por frecuencias del wav"

    if wav == "48":
        chanel = chanel + [0,1]
    if wav == "44,1":
        chanel = chanel + [1,0]
    if wav == "32":
        chanel = chanel + [1,1]
    chanel  = chanel + [0,0,0,1,0,0,0,1]
    "Definimos por bits"
    if b_wav == "20":
        chanel = chanel + [0,0,0]
    else:
        chanel == chanel + [0,0,1]
    "Rellenamos el resto con ceros"
    for i in range(len(chanel),192):
        chanel.append(0)

    return chanel



""" preambulos """
PR_X0 = [1,1,1,0,0,0,1,0]
PR_X1 = [0,0,0,1,1,1,0,1]
PR_Y0 = [1,1,1,0,0,1,0,0]
PR_Y1 = [0,0,0,1,1,0,1,1]
PR_Z0 = [1,1,1,0,1,0,0,0]
PR_Z1 = [0,0,0,1,0,1,1,1]

""" Leemos el audio """
audio = wave.open('muestra2448.wav')
""" Calculamos el numero de muestras """
nframes = audio.getnframes()
""" Almacenamos las muestras en bytes """
muestras_audio = audio.readframes(nframes)

""" Creamos un array vacio de 192 posiciones donde incluiremos Posision """
Frames = []
for i in range(0,192):
    Frames.append(0)
print(len(Frames))
""" EN ESTE PUNTO DECIDIMOS CUAL SERÁ EL PREAMBULO"""

aes = []
for Posision in range(0, len(Frames)):
    trama = []
    print("Número de trama :")
    print(Posision)
    if int(Posision) == 0:
        trama = PR_Z0
    else:
        if int(Posision) % 2 == 0:
            trama = PR_X0
        else:
            trama = PR_Y0


    """ Ahora rellenamos con el wav """
    trama = trama + audio_r[(Posision*20):(((Posision+1)*20))]
    """Terminamos con la inclusión de la cola"""
    chanel = arrayChannel(sys.argv[1],sys.argv[2])
    cola  = [0,0] + [chanel[Posision]]
    trama = trama + cola
    print("Trama sin paridad + tamaño")
    print(trama)
    print(len(trama))
    trama.append(parity(trama))

    aes.append(trama)
    print("TRAMAFINAL y tamaño de trama:")
    print(trama)
    print(len(trama))

print("ARCHIVO AES:")
print(aes)
