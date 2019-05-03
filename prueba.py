import wave
import array
import io
import random

"""Stream_out = open("aesebu_output.aes", "w")"""

stream_out = []
for i in range(0,4880):
    stream_out.append(random.randint(0,1))


def parity (i):
    len = 0
    for j in i:
        if j == 1:
            len +=1
    if  len %2 == 0:
        parity = 1
    else:
        parity = 0

    return int(parity)

def arrayChannel(wav, b_wav):
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
trama = []
for i in range(1,10):
    stream_out.append(0)
aes = []
for Posision in range(0, len(Frames)-1):
    trama = []
    print("posision:")
    print(Posision)
    if int(Posision) == 0:
        trama = PR_Z0
    else:
        if int(Posision) % 2 == 0:
            trama = PR_X0
        else:
            trama = PR_Y0


    """ Ahora rellenamos con el wav """
    trama = trama + stream_out[(Posision*20):(((Posision+1)*20))]
    """Terminamos con la inclusión de la cola"""
    chanel = arrayChannel("48","20")
    cola  = [0,0] + [chanel[Posision]]
    trama = trama + cola
    print(trama)
    print(len(trama))
    # parity = parity(lol)
    # print(parity)
    trama.append(parity(trama))

    aes.append(trama)
    # print("TRAMAFINAL:")
    # print(trama)
    # print(len(trama))
print(aes)
