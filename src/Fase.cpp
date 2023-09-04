#include "../Estados/Fase.h"

namespace Estados
{
    Fase::Fase():
    faixa(),
    bpm(),
    tamanho(),
    janela(sf::VideoMode(600, 600), "Guitar Healer")
    {

    }
    Fase::~Fase()
    {

    }
    void Fase::executar()
    {
        while(janela.isOpen())
        {
            sf::Event event;
            while (janela.pollEvent(event))
                if (event.type == sf::Event::Closed)
                    janela.close();

            janela.clear();
            janela.display();
        }
    }
    bool Fase::carregarFaixa()
    {
        return false;
    }
    void Fase::mudarVelocidade(const unsigned char v)
    {
        
    }
}