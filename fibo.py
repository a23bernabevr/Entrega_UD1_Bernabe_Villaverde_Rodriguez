
def fibonacci(limite):                  #definimos la función fibonacci
    a = 0  
    b = 1
    fibonacci_sequence = []             #creamos una lista vacía en la que iremos con el for añadiendo resultados 
    for iteracion in range(limite):     #creamos el for 
        fibonacci_sequence.append(a)    #agregamos el valor inicial de a (0) a la lista que hemos creadopor lo que tendríamos la lista así [0] 
        b = b + a                       #1+0 = 1
        a = b - a                       #1-0 = 1   a=1 esto lo añadirá en el siguiente bulce a la lista gracias al fibonacci_sequence.append(a)
    return fibonacci_sequence           #el return sirve para que devuelva la lista completa al hacer el print



#resultado = fibonacci(5)             #prueba de funcionamiento, metemos la función en una variable diciéndole que haga 10 veces la iteración
#print (resultado)                     #imprimimos el resultado   


# test_fibo.py
import unittest                                         #Importamos la librería unittest
from pruebafibo import fibonacci                              #Importamos la función que creamos

class Test(unittest.TestCase):                          #definimos la clase llamada Test que hereda las funcionalidades de la librería unittest 

    def test_quinto_numero_fibonacci(self):             #nombro la función con el prefijo "test_" para que el descubrimiento automático de pruebas de unittest funcione correctamente.
        resultado = fibonacci(5)                        #llama a la funcion indicando que haga 5 veces la iteración lo que hará que la lista tenga 5 números [0,1,1,2,3]
        self.assertEqual(resultado, [0, 1, 1, 2, 3])    #con assertEqual (método que viene de la librería unittest) verofica si el resultado de la función al darle el valor 5 es correcto
        
if __name__ == '__main__':                              #Ejecutamos la función quinto_numero_fibonacci y con el unittest 
    unittest.main()                                     #nos verifica si se genera correctamente la secuencia hasta el quinto número devolviendo un OK

