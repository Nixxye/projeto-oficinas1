#include <iostream>
#include <fstream>
#include <vector>
#include <SFML/Graphics.hpp>
#include <iostream>
#include <thread>
// Constantes para a simulação:
#define N_COLUNAS 4
#define N_BOLINHAS 36

namespace Estados
{
    class Fase
    {
    private:
        char* faixa;
        unsigned char bpm;
        unsigned char tamanho;
        int contador;
        bool encerrar;
        // Apenas para simulação;
        std::vector<sf::CircleShape*> bolinhas;

        sf::RenderWindow janela;
    public:
        Fase();
        ~Fase();

        void executar();
        bool carregarFaixa(std::string endereco);
        void mudarVelocidade(const unsigned char v);
        void girarEsteira();
        // Talvez mudar o contador para ser atributo:
        void atualizarLeds();
        // void mudarPontuação(bool p);
    };    
}
