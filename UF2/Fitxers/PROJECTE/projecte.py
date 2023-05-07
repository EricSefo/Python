# Importem les biblioteques necessàries
import os
from pathlib import Path
import zipfile
import shutil
from datetime import datetime, timedelta
from math import sqrt
from tqdm import tqdm
from time import sleep

# Creem una llista buida per a guardar els fitxers de còpia de seguretat
backup = []

# Definim la data i hora actuals en el format "AAAA-MM-DD HH:MM:SS"
avui = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Definim la data d'ahir en el format "AAAAMMDD"
ahir = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')

# Obrim el fitxer "config.txt" en mode lectura i el dividim en una llista
config = open("config.txt","r").read().split()

# Canviem el directori de treball al directori especificat en el fitxer "config.txt"
os.chdir(config[0])

# Obtenim una llista de fitxers en el directori actual i els ordenem alfabèticament
arxius = os.listdir()
arxius.sort()


def calcul(llista, document):
    # Inicialitzem les variables necessàries
    inc = 0
    pesades = 0
    errors = 0
    num_animals = 0
    fora_rang = 0
    diferencia = 0
    pesos = []
    
    # Iterem a través de la llista de pesades
    for valor in llista:
        # Augmentem el comptador de pesades
        pesades += 1
        
        try:
            # Comprovem si el pes està dins del rang permès
            if float(config[3]) <= float(valor) <= float(config[4]):
                # Si el pes és correcte, augmentem el comptador de animals i la suma total de pesos
                num_animals += 1
                inc += float(valor)
                # Afegim el pes a la llista de pesos
                pesos.append(float(valor))
            else:
                # Si el pes no està dins del rang permès, enregistrem un missatge de registre
                log.write(avui + " - " + document + " - Error de pesada!!! - Pes: " + valor)
                fora_rang += 1
        except:
            # Si hi ha un error al llegir el pes, enregistrem un missatge de registre
            log.write(avui + " - " + document + " - Error de lectura!!!\n")
            errors += 1
    
    # Calculem la mitjana dels pesos
    mitjana = inc / num_animals
    
    # Ordenem la llista de pesos
    pesos.sort()
    
    # Calculem la mediana dels pesos
    meitat = len(pesos) // 2
    if len(pesos) % 2 == 0:
        mediana = (pesos[meitat - 1] + pesos[meitat]) / 2
    else:
        mediana = float(pesos[meitat])
    
    # Calculem la desviació estàndard dels pesos
    for valor in pesos:
        diferencia += (float(valor) - mitjana) ** 2
    desviacio = round(sqrt(diferencia / (len(pesos) - 1)), 2)
    
    # Retornem les dades calculades
    return pesades, errors, fora_rang, num_animals, round(mitjana, 2), mediana, desviacio

def main(data):
    # Escriu la capçalera de l'arxiu XML
    xml.write('<?xml version="1.0" encoding="utf-8"?>\n')
    xml.write("<pesades>\n")
    
    # Itera a través de tots els arxius de pesades per a la data especificada
    for percentatge, arxiu in tqdm(enumerate(arxius), desc="Procesant arxius", total=len(arxius)):
        if arxiu.split("_")[0] == data:
            # Afegeix l'arxiu a la llista de backups
            backup.append(arxiu)
            # Obre l'arxiu de pesades i llegeix totes les línies
            var = open(arxiu,"r")
            rows = var.readlines()
            # Obte el número de lot del fitxer
            lote = int((arxiu.split("_")[1]).split(".")[0])
            # Calcula les estadístiques de les pesades
            valors = calcul(rows,arxiu)
            # Escriu les dades de la pesada a l'arxiu XML
            xml.write("\t<pesada>\n")
            xml.write("\t\t<lot>"+str(lote)+"</lot>\n")
            xml.write("\t\t<num_pesades>"+str(valors[0])+"</num_pesades>\n")
            xml.write("\t\t<errors_pesades>"+str(valors[1])+"</errors_pesades>\n")
            xml.write("\t\t<fora_rang>"+str(valors[2])+"</fora_rang>\n")
            xml.write("\t\t<dades_animals>\n")
            xml.write("\t\t\t<num_animals>"+str(valors[3])+"</num_animals>\n")
            xml.write("\t\t\t<mitjana>"+str(valors[4])+"</mitjana>\n")
            xml.write("\t\t\t<mediana>"+str(round(valors[5],2))+"</mediana>\n")
            xml.write("\t\t\t<desv_tipica>"+str(valors[6])+"</desv_tipica>\n")
            xml.write("\t\t</dades_animals>\n")
            xml.write("\t</pesada>\n")
            # Pausa per evitar sobrecarregar el sistema
            sleep(1)
    
    # Tanca l'arxiu XML i el fitxer de log
    xml.write("</pesades>\n")
    xml.close()
    log.close()

# recorrem la llista d'arxius
for arxiu in arxius:
    # si la data del fitxer config.txt coincideix amb la data d'algun fitxer, processa les dades i crea l'XML
    if config[5] in arxiu.split("_")[0]:
        xml = open("../"+config[2]+"/"+config[5]+'.xml', 'w')
        log = open('../log.txt', 'a')
        file_zip = 'copia_seguretat_'+config[5]+'.zip'
        main(config[5])
        pivot = True
        break
    # si la data d'ahir està en el nom de l'arxiu, processa les dades i crea l'XML
    elif ahir in arxiu.split("_")[0]:
        xml = open("../"+config[2]+"/"+ahir+'.xml', 'w')
        log = open('../log.txt', 'a')
        file_zip = 'copia_seguretat_'+ahir+'.zip'
        main(ahir)
        pivot = True
        break
    # si no hi ha arxius que coincideixen amb la data actual ni amb la de d'ahir, estableix la variable pivot a False
    pivot = False

# Comprovem si s'ha processat algun arxiu
if pivot == False:
    print("No hi ha cap arxiu a processar.")
else:
    # Creem un arxiu zip per a la còpia de seguretat
    with zipfile.ZipFile(file_zip, 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
        for arxiu in backup:
            archivo_zip.write(arxiu)
        archivo_zip.close()
    
    # Movem l'arxiu zip a la ruta especificada a la configuració
    shutil.move(file_zip, Path("../"+config[1]) / file_zip)