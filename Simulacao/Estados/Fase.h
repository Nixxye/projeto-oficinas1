#pragma once

#include <iostream>
#include <fstream>
#include <vector>
#include <SFML/Graphics.hpp>
#include <iostream>
#include <thread>
#include <queue>
#include "../T_class.h"
#include "../Gerenciadores/GerEventos.h"
// Constantes para a simulação:
#define N_COLUNAS 4
#define N_BOLINHAS 36

namespace Estados
{
    class Fase: public T_class
    {
    private:
        char* faixa;
        unsigned char bpm;
        unsigned char tamanho;
        int contador;
        Gerenciadores::GerEventos ge;
        // Apenas para simulação;
        std::vector<sf::CircleShape*> bolinhas;
        std::queue<char>* inputs;
        sf::RenderWindow janela;
    public:
        Fase();
        ~Fase();

        void executar();
        bool carregarFaixa(std::string endereco);
        void mudarVelocidade(const unsigned char v);
        void girarEsteira();
        void verificarInputs();
        // Talvez mudar o contador para ser atributo:
        void atualizarLeds();
        // void mudarPontuação(bool p);
    };    
}
