#include <iostream>
#include <fstream>

#include <SFML/Graphics.hpp>

namespace Estados
{
    class Fase
    {
    private:
        char** faixa;
        unsigned char bpm;
        unsigned char tamanho;

        sf::RenderWindow janela;
    public:
        Fase();
        ~Fase();

        void executar();
        bool carregarFaixa();
        void mudarVelocidade(const unsigned char v);
        // void mudarPontuação(bool p);
    };    
}
