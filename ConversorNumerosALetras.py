#Cadenas
esp=["","once", "doce","trece","catorce","quince","diesiseis","diesisiete","diesiocho","diesinueve"]
esp2=["veinte","veintiuno","veintidos","veintitres","veinticuatro","veinticinco","veintiseis","veintisiete","veintiocho","veintinueve"]
uni=["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
dec=["","diez","veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
cen=["","ciento ","dosientos ","tresientos ","cuatrosientos ","quinientos ","seisientos ","setecientos ","ochocientos ","novecientos "]
#Número ingresado por el usuario
num=int(input("Ingrese un número de dos cifras: "))

#Separación de unidades, decenas y centenas
if num < 100:                #Si es de dos numeros
    unidad=num % 10
    decena=num//10
else:                        #Si es de tres números
    centena = num //100
    cent2=num%100
    decena=cent2//10
    unidad=cent2%10
text=""

#Conversor de numeros a textos
if num < 10:                                    #Conversor de un número
    text = uni[num]
elif num < 100 and num >= 30:                   #Conversor de dos números
    text = [dec[decena]+" y "+uni[unidad]]
elif num >= 10 and num <= 29:
    text = [esp[num%10]]
    if num>=20:
        text = [esp2[num%10]]
elif num == 100:                                #Conversor de tres números
    print("cien")
elif num > 100 and num < 1000:
    text = [cen[centena]+dec[decena]+uni[unidad]]
    if num >110 and num < 120:
        text = [cen[centena]+esp[decena]]
    elif num >= 120 and num < 130:
        text = [cen[centena]+esp2[unidad]]
else:
    print("ERROR")

final="".join(text)                              #Salida
print(final)