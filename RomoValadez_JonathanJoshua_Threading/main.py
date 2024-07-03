import threading
import time

def thread_function(tiempo, letra):
    time.sleep(tiempo)
    print("Thread", tiempo - 2, "finishing")
    print(letra)

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