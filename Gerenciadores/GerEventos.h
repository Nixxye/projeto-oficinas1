#pragma once 

#include <queue>
#include <SFML/Graphics.hpp>
#include "../T_class.h"

// Fazer singleton dps:
namespace Gerenciadores
{
    class GerEventos: public T_class
    {
    private:
        std::queue<char> inputs;
    public:
        GerEventos();
        ~GerEventos();
        // fazer const:
        std::queue<char>* getFila();
        void captarInputs();
    };
}