

def fibonacci(limite):                  #definimos la función fibonacci
    a = 0  
    b = 1
    fibonacci_sequence = []             #creamos una lista vacía en la que iremos con el for añadiendo resultados 
    for iteracion in range(limite):     #creamos el for 
        fibonacci_sequence.append(a)    #agregamos el valor inicial de a (0) a la lista que hemos creadopor lo que tendríamos la lista así [0] 
        b = b + a                       #1+0 = 1
        a = b - a                       #1-0 = 1   a=1 esto lo añadirá en el siguiente bulce a la lista gracias al fibonacci_sequence.append(a)
    return fibonacci_sequence           #el return sirve para que devuelva la lista completa al hacer el print



##resultado = fibonacci(10)             #prueba de funcionamiento, metemos la función en una variable diciéndole que haga 10 veces la iteración
##print (resultado)                     imprimimos el resultado
