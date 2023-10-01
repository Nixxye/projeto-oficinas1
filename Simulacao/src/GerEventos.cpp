#include "../Gerenciadores/GerEventos.h"
#include <thread>

namespace Gerenciadores
{
    GerEventos::GerEventos():
    inputs()
    {

    }
    GerEventos::~GerEventos()
    {

    }
    std::queue<char>* GerEventos::getFila()
    {
        return &inputs;
    }
    void GerEventos::captarInputs()
    {
        bool pressionado = false;
        while (!terminar)
        {
            pressionado = false;
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::A))
            {
                pressionado = true;
                inputs.push('1');
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::S))
            {
                pressionado = true;
                inputs.push('2');
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::D))
            {
                pressionado = true;
                inputs.push('3');
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::F))
            {
                pressionado = true;
                inputs.push('4');
            }
            if (pressionado)
                std::this_thread::sleep_for(std::chrono::milliseconds(200));         
        }
    }
}