#print("Convierte las siguientes expresiones a expresiones algorítmicas")  
#a=1
#b=3
#bx=6
#yx=5
#u=4
#w=4
#x=5
#y=5
#z=2

#pri=a**2+b**2
#seg=a(a+b)**2
#ter=b**1/3+34
#cua=b+34**1/3
#cin=bx/(yx/u)(w/b)
#sei=x/y(z+w)*3.1416
#sie=((x+y)/w)/u+(w/b)


print ("2. ¿Qué se obtiene en las variables A y B, después de la ejecución de las siguientes instrucciones?") 
A=5 
B= A +6 
A= A+ 1 
B=A-5

print(A, B)

print("3. ¿Qué se obtiene en las variables A, By C después de ejecutar las instrucciones siguientes?")
A=3 
B=20 
C=A+B 
B=A+B 
A=B-C 

print(A, B)
 
print("4. ¿Qué se obtiene en A y B tras la ejecución de lo siguiente?")
 
A=10 
B=5 
B=B 
B=A 

print(A, B) 

print("5. Determina los valores finales de X, Y y Z después de ejecutar el siguiente código:") 
X = 4 
Y = X * 3 
Z = Y // 2 
X = Z + Y 
Y = X % 5 
Z = X - Y

print(X, Y, Z) 
 
print("6. Calcula los valores de A, B y C tras la ejecución de estas instrucciones:")
A = 15 
B = A // 4 
C = A % 4 
A = B + C * 3 
B = A - B 
C = B + C 
 
print(A, B, C)

print("7. ¿Qué valores quedan en P, Q y R?") 
P = 8 
Q = P * 2 
R = Q - 5 
P = (R + P) // 3 
Q = P * R 
R = Q % 4

print(P, R, Q)
 
print("8. Encuentra los valores finales de M, N y O:") 
M = 9 
N = M + 6 
O = M * N 
M = O % 7 
N = (M + O) // 5 
O = N - M 

print(M, N, O)

print("9. Determina los valores finales de X, Y y Z después de ejecutar el siguiente código:") 
X = 8 
Y = X * 2 + 3 
Z = Y // 4 
X = Z + Y * 2 
Y = X % 6 + Z 
Z = X - Y + 5

print(X, Y, Z)
 
print("10. Calcula los valores de A, B y C tras la ejecución de estas instrucciones:") 
 
A = 20 
B = A // 5 + 2 
C = A % 7 + B * 3 
A = (B + C) // 2 
B = A * C - B 
C = (A + B) % 4

print(A, B, C)
 
print("11. ¿Qué valores quedan en P, Q y R?") 
P = 10 
Q = P * 3 - 4 
R = Q // 2 + P % 3 
P = (R + P) // 2 + Q % 5 
Q = P * R + Q // 3 
R = (Q - P) % 6 
 
print(P, R, Q)
  
print("12. Encuentra los valores finales de M, N y O:") 
M = 15 
N = M + 7 - M % 4 
O = M * N // 5 + 2 
M = (O % 3 + N) * 2 
N = (M + O) // 4 - 3 
O = N - M % 5 + 10 

print(M, N, O) 
 
print("13. ¿Qué valor (True o False) tiene la variable R después de ejecutar las siguientes instrucciones?") 
A = 10 
B = 5 
R = (A > B) and (A != 0) 
 
print(R)

print("14. ¿Qué valor tiene C después de ejecutar este código?") 
X = 7 
Y = 12 
C = (X < 5) or (Y > 10) 

print(C)

print("15. ¿Qué valor tiene D después de ejecutar el siguiente código?") 
Z = 8 
D = not (Z > 10) 

print(D)

print("16. Determina los valores finales de R1 y R2:") 
A = 4 
B = 9 
 
R1 = (A < 5) and (B > 8) 
R2 = not (A == 4)

print(R1, R2)
 
print("17. ¿Qué valor tendrá la variable R al final?") 
A = 6 
B = 3 
C= 10 
 
R = (A > B) and (C < 15) or (B == 3) 

print(R)

print("18. ¿Qué valor tendrá X y Y al final del código?")  
X = 8 
Y = 4 
 
X = not (X < 10)  # Se evalúa como True o False Y = (Y != 5) and not (X) 
 
print(X)
 
print("19. Completa el siguiente código para que la variable resultado sea True solo si edad está entre 18 y 30 años (inclusive):") 
 
edad = 25  # Puedes cambiar este valor para probar resultado = 
resultado1= (edad >18)and(edad<30)

print(resultado1)
 
print("20. Determina si un estudiante aprueba el examen solo si su nota está entre 7 y 10 (inclusive).") 
 
nota = 8  # Puedes cambiar este valor para probar aprueba = 
resultado2=(nota>7)and(nota<10)

print(resultado2)
 
print("21. Escribe un código que determine si un número X está entre 10 y 20 (inclusive), o si está fuera de ese rango pero es un múltiplo de 5. El resultado debe ser True en estos dos casos.") 
x = 15  # Puedes cambiar este valor para probar resultado = 
Resultado3=(x>10)and(x<20)or(x % 5==0)

print(Resultado3)
 
print("22. Escribe un código que devuelva True si una persona es mayor de 18 años y lleva más de 2 años con su suscripción a un servicio. De lo contrario, debe devolver False.")
edad = 20  # Puedes cambiar este valor 
suscripción=3
resultado4=(edad>18)and(suscripción>2)
print(resultado4)