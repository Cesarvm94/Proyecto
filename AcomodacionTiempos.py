import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

import os
ruta='C:/Users/cesar/Desktop/Tiempos/AnalisisPythonNube/BDSISD'
contenido = os.listdir(ruta)
contenido.remove(contenido[-1])
contenido=sorted_alphanumeric(contenido)
ruta1='C:/Users/cesar/Desktop/Tiempos/AnalisisPythonNube/BDSISD/SoloTiempos'
contenido1 = os.listdir(ruta1)

lines11 =[1,2,3]
lines12 =[6,7,8]
lines13 =[11,12,13]
lines21 =[16,17,18,19]
lines22 =[22,23,24,25]
lines23 =[28,29,30,31]
lines31 =[34,35,36]
lines32 =[38,39,40]
lines33 =[43,44,45]
lines34 =[48,49,50]
lines41 =[53,54]
lines42 =[57,58]
lines43 =[61,62]
lines51 =[65,66,67]
lines52 =[70,71,72]
lines53 =[75,76,77]
lines61 =[80,81]
lines62 =[84,85]
lines63 =[88,89]
lines71 =[92,93,94,95,96]
lines72 =[99,100,101,102,103]
lines73 =[106,107,108,109,110]
lines81 =[113,114]
lines82 =[117,118]
lines83 =[121,122]
lines91 =[125,126]
lines92 =[129,130]
lines93 =[133,134]
lines101=[137,138]
lines102=[141,142]
lines103=[145,146]
lines111=[149,150]
lines112=[153,154]
lines121=[157,158]
lines122=[161,162]
lines123=[165,166]
data = []
i = 0
for m in lines123:
    with open(ruta1+"/"+'12-3.txt', "a") as f1:
        for j in contenido:
            i=0
            with open(ruta+"/"+j, "r+") as f:
                for line in f:
                    if i ==m and j=='R_T_BDSISD_20.txt':
                        f1.write(line[20:26]+"\n")
                    elif i ==m and j!='R_T_BDSISD_20.txt':
                        f1.write(line[20:26]+",")
                    i=i+1

            f.close()
