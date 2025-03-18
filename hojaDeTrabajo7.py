#1. Escribe un programa que extraiga la ultima y primer palabra de una oracioN
#oracion="Python es un lenguaje poderoso"
#oracionSeparada=oracion.split()
#print("La primera palabra de la oracion es: ", oracionSeparada[0], "y la última palabra de la oración es: ", oracionSeparada[6])


# 2. Crear un programa que elimine los espacios repetidos en una cadena
#ora="Hola  mundo  en python"
#oraList=" ".join(ora.split())
#print(oraList)


#3. Dado un correo electronico extrae el siguiente dominio 
#correo= "usuario@gmail.com"
#dominio=correo.split("@")[1]
#print(dominio)

#4. Dado un nombre de documento, verifica si tiene extencion correcta (pdf)
#nombre=input("Ingrese el nombre del documento: ")
#extencion=nombre.endswith(".pdf")
#print(extencion)


#5. Dado un texto invierte el orden de las palabras
#orac="Me gusta python"
#oracCad=" ".join(orac.split()[::-1])
#print(oracCad)


#6. Dado un texto ingresado por el usuario detectar palabras claves y responder
selec=input("¿Que deseas buscar?")

poemaamor="Podra nublarse el sol eternamente;Podra secarse el mar en un instante; Prodra romperse el eje de lña tierra; Como un debil cristal"
cancionalegria="Eres como la noche, callada y constelada. Tu silencioes de estrella, tan lejano y sencillo. Me gustas cuando callas porque estás como ausente. Distante y dolorosa como si hubieras muerto"
poematriste="No hay espacios mas anchos que el dolor, no hay universo como aquel que sangra."
cancionsoledad="En algunas personas amamos a personas que no existen ya; en otras; amamos a nadie ni a esa misma persona."
poemaenojo="En este crimen soy la víctima que de ti se a enamoradoy tu eres la víctima que impetuosa destierras y con desamor me castigas."
if "amor" in selec:
    print(poemaamor)
elif "alegria" in selec:
    print(cancionalegria)
elif "triste" in selec:
    print(poematriste)
elif "soledad" in selec:
    print(cancionsoledad)
elif "enojo" in selec:
    print(poemaenojo)
else:
    print("ERROR, no encuentro lo que buscas en mi base se datos")