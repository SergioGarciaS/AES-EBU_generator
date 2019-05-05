


bytes = b'\x18\x00\x03w\xff\xff\x0099\x05\xff\xff\xff\xff'
# bytes = b'k\xfa\xff\x12\xdf\xff\x16\xe1\xff\xd8\xba\xff\xc5\xe4\xff\xff\xe7\xffx\xf1\xff \xd0\xff\xfd\xcb\xffU\xb7\xffl\x93\xff\xc5\x89\xffzx\xff\xd8\x83\xff]\x89\xff\x9e\x96\xff,\xb5\xffV\xc4\xff\xbd\xac\xff\x10\x9f\xffM\xc5\xff0\xd7\xff\xad\xce\xff\xd9\xc1\xff\xf2\x9e\xff\xfe\xa4\xff\x00\xa3\xff\xf9\x9e\xff"\x94\xff:\xa7\xffg\xa7\xff\xd4\xaf\xff\xa1\xb2'

cadena = str(bytes)
cadena  = cadena.splitlines()
print(cadena)
salida = [];
movidita = cadena[0].split("'")[1].split('\\')
print(movidita)
movidita.pop(0)
for lines in movidita:
    print(lines)
    binary = bin(int(lines[1:3],16))[2:] #Cogemos toda la trama sin x y sin otro valor
    print(binary)
    print(len(binary))
    i = 0
    sum = "0"
    if len(binary) != 8: # PARA EL FORMATO DE 8 BITS
        for i in range(int(len(binary)), 7):
            sum += "0"
        binary = sum + binary
        print(binary)
    else:
        print(binary)
    salida.append(binary)

salida = "".join(salida)
print(salida)
audio = []
for i in salida:
    audio.append(int(i))


print(audio)
