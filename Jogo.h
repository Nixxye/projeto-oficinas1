#include <SFML/Graphics.hpp>
#include "Estados/Fase.h"

class Jogo
{
private:
    Estados::Fase fase;    
public:
    Jogo();
    ~Jogo();
    void executar();
};