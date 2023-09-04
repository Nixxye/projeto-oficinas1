#include "../Estados/Fase.h"

namespace Estados
{
    Fase::Fase():
    faixa(nullptr),
    bpm(0),
    tamanho(0),
    janela(sf::VideoMode(600, 600), "Guitar Healer"),
    contador(0)
    {
        janela.setFramerateLimit(60);

        sf::CircleShape* aux;
        for (int i = 0; i < N_BOLINHAS; i++)
        {
            aux = new sf::CircleShape(30.f);
            aux->setFillColor(sf::Color::White);  
            aux->setPosition(sf::Vector2f(100 * (1 + (i % 4)), (100 * ((int) i / 4))));
            bolinhas.push_back(aux);
        }
    }
    Fase::~Fase()
    {
        for (int i = 0; i < N_BOLINHAS; i++)
            delete bolinhas[i];  
    }
    void Fase::executar()
    {
        carregarFaixa("Musicas/faixa.txt");
        while(janela.isOpen())
        {
            sf::Event event;
            while (janela.pollEvent(event))
                if (event.type == sf::Event::Closed)
                    janela.close();

            janela.clear();
            // Núcleo de execução da simulação:
            girarEsteira();
            
            janela.display();
        }
    }
    bool Fase::carregarFaixa(std::string endereco)
    {
        std::ifstream arquivo(endereco);
        
        if (!arquivo)
        {
            std::cout << "Arquivo não encontrado" << std::endl;
            return false;
        }

        std::string linha;

        std::getline(arquivo, linha);
        tamanho = stoi(linha);
        faixa = (char*) malloc(sizeof(char) * tamanho * N_COLUNAS);

        std::getline(arquivo, linha);
        bpm = stoi(linha);

        for (int i = 0; std::getline(arquivo, linha); i += N_COLUNAS)
        {
            faixa[i] = linha[0];
            faixa[i + 1] = linha[1];
            faixa[i + 2] = linha[2];
            faixa[i + 3] = linha[3];
        }

        for (int i = 0; i < tamanho * N_COLUNAS; i++)
        {
            if (i % N_COLUNAS == 0 && i != 0)
                std::cout << std::endl;
            std::cout << faixa[i] << " ";
        }

        return true;
    }
    void Fase::mudarVelocidade(const unsigned char v)
    {
        
    }
    void Fase::girarEsteira()
    {
        contador++;

        for (int i = 0; i < N_BOLINHAS; i++)
        {
            bolinhas[i]->setPosition(bolinhas[i]->getPosition() + sf::Vector2f(0.f, bpm));
            if (bolinhas[i]->getPosition().y >= 600)
            {
                bolinhas[i]->setPosition(sf::Vector2f(bolinhas[i]->getPosition().x , -100.f));
                
            }
            if (i >= N_BOLINHAS % contador && i <= N_BOLINHAS % contador + 3)
            {
                bolinhas[i]->setFillColor(sf::Color::Red);
            }
            janela.draw(*bolinhas[i]);
        }
    }
}