hora_formal=int(40)    #la hora se paga a Q40
horas_trabajadas=int(input("Ingrese las horas totales trabajadas: "))   #las horas que totales que trabajo


if horas_trabajadas>hora_formal:
   horas_extras=horas_trabajadas-hora_formal    #calulo si trabajo horas extras
   pago_de_extras=horas_extras*1.5
   pago_de_formal=(horas_trabajadas-horas_extras)*hora_formal
   pagon_neto_con_extras=pago_de_formal+pago_de_extras
   print("El pago neto on las horas etra es de: ", pagon_neto_con_extras)
else:
    horas_faltantes=hora_formal-horas_trabajadas
    