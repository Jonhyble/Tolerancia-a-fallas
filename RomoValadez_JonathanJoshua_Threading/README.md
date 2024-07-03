# Hilos
_Romo Valadez Jonathan Joshua_

_Computación tolerante a fallas_

_Universidad de Guadalajara_

_CUCEI_

_Departamento de ciencias computacionales_

---

## Introducción
En ocasiones se puede llegar a ejecutar codigo que ocasione errores, por lo que se puede recurrir a los hilos, que también nos permitirán realizar varias tareas a la vez, por asi decirlo, de forma asincronica, pues se van ejecutando de forma independiente al hilo principal.

---

## Desarrollo
En esta practica se utilizaran los hilos para detectar letras especificas en un documento, con cada letra aumentar un segundo en el timer de cada hilo, y así comprobar que aun así los hilos no se esperan entre sí, sino que termina cada uno de forma individiual.

_Para la lectura del texto se toma en cuenta el siguiente código_

~~~python
if __name__ == "__main__":
    archivo = open("texto.txt", "r")
    i = 2
    for letra in archivo.read():
        if letra == "e" or letra == "o":
            x = threading.Thread(target=thread_function, args=(i, letra))
            x.start()
            i = i + 1
        else:
            print(letra, end = "")
    print("\nLetras encontradas: ")
~~~

_Para cada hilo se ejecutará el siguiente código_

~~~python
def thread_function(tiempo, letra):
    time.sleep(tiempo)
    print("Thread", tiempo - 2, "finishing")
    print(letra)
~~~

_El resultado sería el siguiente_

![Uso de nssm](./imagenes/Hilos.gif "Resultado")

---

## Conclusión
Esta actividad sirve mucho para realizar distintas tareas en las que necesitamos optimizar tiempo, pues un hilo no espera a otro para ejecutarse, sino que se pueden ejecutar simultaneamente, lo que lo hace muy útil.
Además de esto, sirve para evitar que algún error nos deje inservible el programa.
