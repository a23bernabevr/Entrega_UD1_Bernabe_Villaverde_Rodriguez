# test_fibo.py
import unittest                                         #Importamos la librería unittest
from ejerciciofibo.fibo import fibonacci                              #Importamos la función que creamos

class Test(unittest.TestCase):                          #definimos la clase llamada Test que hereda las funcionalidades de la librería unittest 

    def test_quinto_numero_fibonacci(self):             #nombro la función con el prefijo "test_" para que el descubrimiento automático de pruebas de unittest funcione correctamente.
        resultado = fibonacci(5)                        #llama a la funcion indicando que haga 5 veces la iteración lo que hará que la lista tenga 5 números [0,1,1,2,3]
        self.assertEqual(resultado, [0, 1, 1, 2, 3])    #con assertEqual (método que viene de la librería unittest) verofica si el resultado de la función al darle el valor 5 es correcto
        
if __name__ == '__main__':                              #Ejecutamos la función quinto_numero_fibonacci y con el unittest 
    unittest.main()                                     #nos verifica si se genera correctamente la secuencia hasta el quinto número devolviendo un OK


