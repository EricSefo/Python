import smtplib
import zipfile
import os
import logging
from pathlib import Path

arxius_processats_correctament = []
arxius_amb_errors = []
logging.basicConfig(filename='log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
quantitat_total = {}
config = open("config.txt","r").read().split()
os.chdir(config[0])
arxius = os.listdir()
arxius.sort()

def comprovacio(directori_arxius_generats, arxiu_generat):
    try:
        comprovar_arxiu = '../' + directori_arxius_generats + '/' + arxiu_generat
        p = Path(comprovar_arxiu)
        if p.is_file():
            print("El fitxer", arxiu_generat, "ja existeix.")
            return open("../" + directori_arxius_generats + "/" + arxiu_generat, 'a')
        else:
            print("Creant l'ariux", arxiu_generat, "...")
            return open("../" + directori_arxius_generats + "/" + arxiu_generat, 'a')
    except Exception as e:
        logging.error('Ocurrió un error: %s', str(e))

fitxer_cru = comprovacio(config[2], "cru.txt")
fitxer_articleColor = comprovacio(config[2], "articleColor.txt")

for valor in arxius:
    try:
        info = open(valor,"r")
        dades = info.readlines()
        calcul_quantitat_total = dades
        cru = dades
        primera_linea = True
        for dades in calcul_quantitat_total:
            if primera_linea:
                primera_linea = False
                continue  # Saltar a la següent iteració sense processar la primera línia
            dades = dades.split(";")[:-1]
            if dades[1] not in quantitat_total.keys():
                quantitat_total[dades[1]]=int(dades[-1])
            elif dades[1] in quantitat_total.keys():
                quantitat_total[dades[1]]+=int(dades[-1])
        primera_linea = True
        seccio = valor.split("_")[0]
        terminal = valor.split("_")[1].split(".")[0]
        for dades_cru in cru:
            if primera_linea:
                primera_linea = False
                continue  # Saltar a la següent iteració sense processar la primera línia
            dades_cru = dades_cru.split(";")[:-1]
            fitxer_cru.write(seccio+";"+dades_cru[1]+";"+str(quantitat_total[dades_cru[1]])+"\n")
            fitxer_articleColor.write(seccio+";"+dades_cru[1]+";"+dades_cru[2]+";"+dades_cru[-1]+"\n")
        quantitat_total = {}
    except Exception as e:
        arxius_amb_errors.append(valor)
        logging.error('Hi ha un error: %s', str(e))
    arxius_processats_correctament.append(valor)
fitxer_cru.close()
fitxer_articleColor.close()

#EXTRACCIÓ
try:
    #Creació i adició de fitxers
    os.chdir("../"+config[2])
    print("Generant arxiu comprimit dels fitxers d'inventari...")
    newZip = zipfile.ZipFile('../'+config[1]+'/Arxius_generats.zip', 'w')
    newZip.write('cru.txt', compress_type=zipfile.ZIP_DEFLATED)
    newZip.write('articleColor.txt', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()
except Exception as e:
    print("Error al generar l'arxiu comprimit dels fitxers d'inventari...")
    logging.error('Hi ha un error: %s', str(e))

CLAU = config[6]
smtpObj = smtplib.SMTP(config[3],int(config[4]))
smtpObj.starttls()
smtpObj.login(config[5],CLAU)

missatge = "Arxius processats correctament:"
for arxiu in arxius_processats_correctament:
    missatge += "\n\t\t"+arxiu+"\n"

subject = "Inventari de cursors"
body = "Arxius processats correctament:\n\t" + "\n\t".join(arxius_processats_correctament)

# Construir el cuerpo del mensaje
message = f"Subject: {subject}\n\n{body}"

# Enviar el mensaje utilizando sendmail
smtpObj.sendmail(config[5], config[7], message)

#smtpObj.sendmail(config[5], config[7], "Subject: Inventari de cursors\n" + missatge)
smtpObj.quit()