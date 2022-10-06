dni=(input("Quin és el teu número del DNI sense la lletra? "))
dni_numero=int(dni[0:8])
valor = dni_numero % 23
llista = ("TRWAGMYFPDXBNJZSQVHLCKE")
print ("La lletra introduïda és: "+str(llista[valor]==dni[8])+".")