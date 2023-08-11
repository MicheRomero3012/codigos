"""
Autor: Brian Michelle Romero Flores 
Fecha: 10/08/2023
--------------------------------------------------------------------------------------------
Escribe un programa  que muestre en pantalla los números del 1 al 100, 
sustituyendo los múltiplos de 3 por el palabro “Fizz” y, a su vez, 
los múltiplos de 5 por “Buzz”. Para los guarismos que, al tiempo,
son múltiplos de 3 y 5, utiliza el combinado “FizzBuzz”.
"""
#funciones 
def main(int_numero=1):
    
    if (int_numero<=100):
        if(int_numero%3==0):
            print("FIZZ")
            int_numero=int_numero+1
        elif(int_numero%5==0):
            print("BUZZ")
            int_numero=int_numero+1
        elif(int_numero%3==0 & int_numero%5==0):
            print("FIZZ-BUZZ")
            int_numero=int_numero+1
        else:
            print(int_numero)
            int_numero=int_numero+1
        #funcion recursiva
        main(int_numero)

#INICIO DEL PROGRAMA
main()
