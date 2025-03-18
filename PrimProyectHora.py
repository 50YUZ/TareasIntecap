#El usuario ingresa una hora y despues ingresa unos segundos que se le deben sumar a la hora 
#antes añadida y la salida debe de dar la hora correta con los segundos sumados.


hh=int(input("Ingrese la hora: "))
mm=int(input("Ingrese los minutos: "))
ss=int(input("Ingrese los segundos: "))
sps=int(input("Ingrese los segundos por sumar: "))

if (hh <= 24 and hh >= 0):
    if (mm <= 60 and mm >= 0):
        if (ss <= 60 and ss >= 0):
          print(hh,":",mm,":",ss,"+",sps,"segundos:")
        else:
           print("Segundos Invalidos")
    else:
       print("Minutos Invalidos")
else:
   print("Horas Invalidas")

sumaseg=ss+sps

if sumaseg > 59:
   aus= sumaseg - 60
   mm= mm + 1
   ss= aus
   if sumaseg > 119:
        aus2=sumaseg - 120
        mm= mm + 2
        ss= aus2
        if mm > 59:
            aum=mm-60
            hh=hh+1
            mm=aum
else:
   ss=sumaseg

print(hh,":",mm,":",ss)