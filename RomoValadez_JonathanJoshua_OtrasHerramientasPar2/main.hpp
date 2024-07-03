#include <iostream>

class ComprobarError
{
    private:

    public:
        int Comprobacion(const float&, const float&);
};

int ComprobarError::Comprobacion(const float& numeroUno, const float& numeroDos) {
    float resultado;
    int repetir;
    try {
        if (numeroDos != 0) {
            resultado = numeroUno / numeroDos;
            std::cout << "Resultado de la operacion: " << resultado << std::endl;
            repetir = 1;
        }
        else {
            throw (numeroDos);
        }
    } catch (float error) {
        std::cout << "No se puede realizar una division entre 0" << std::endl;
        repetir = 0;
    }
    return repetir;
}
