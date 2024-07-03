#include "main.hpp"

int main(int argc, char const *argv[])
{
    ComprobarError comprobacion;
    int resultado;
    float numeroUno, numeroDos;

    do{
        system("cls");
        std::cout << "Ingrese el dividendo: " << std::endl;
        std::cin >> numeroUno;
        std::cout << "Ingrese el divisor: " << std::endl;
        std::cin >> numeroDos;

        resultado = comprobacion.Comprobacion(numeroUno, numeroDos);
        system("pause");
    } while(resultado == 0);
    
    return 0;
}