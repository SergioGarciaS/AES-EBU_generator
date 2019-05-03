import wave
import array
import io


Stream_out = open("aesebu_output.aes", "w")
def array_Channel()
    chanel []
    chanel = [1,0,0,0,0,0]
    " Definimos por frecuencias del wav"

    if wav == "48":
        chanel = chanel + [0,1]
    else if wav == "44,1":
        chanel = chanel + [1,0]
    else if wav == "32":
        chanel = chanel + [1,1]
    chanel  = chanel + [0,0,0,1,0,0,0,1]
    "Definimos por bits"
    if b_wav = "20":
        chanel = chanel + [0,0,0]
    else:
        chanel = chanel + [0,0,1]
    "Rellenamos el resto con ceros"
    for i in range(lenght(chanel),192):
        chanel.append(0)

    return chanel

"" preambulos ""
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

""" Creamos un array vacio de 192 posiciones donde incluiremos Subframes """
Frames = [None] * 192

""" EN ESTE PUNTO DECIDIMOS CUAL SERÁ EL PREAMBULO"""

for subframes in Frames
    if Subframes = 0:
        trama[i] = PR_X0;
    else:
        if Subframe % 2 == 0:
            trama[i] = PR_X0
        else:
            trama[i] = PR_Y0

""" Ahora rellenamos con el wav """
    trama [i] = trama [i] + wave

"Terminamos con la inclusión de la cola"
    cola  = [0,0] + chanel[i] + parity

    trama[i] = trama[i] + cola
