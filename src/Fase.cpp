#include "../Estados/Fase.h"


namespace Estados
{
    Fase::Fase():
    faixa(nullptr),
    bpm(0),
    tamanho(0),
    janela(sf::VideoMode(600, 600), "Guitar Healer"),
    contador(0),
    encerrar(false)
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
        std::thread girar(&Fase::girarEsteira, this);
        std::thread att(&Fase::atualizarLeds, this);
        while(janela.isOpen())
        {
            sf::Event event;
            while (janela.pollEvent(event))
                if (event.type == sf::Event::Closed)
                {
                    encerrar = true;
                    girar.join();
                    att.join();
                    janela.close();
                }


            janela.clear();
            for (int i = 0; i < N_BOLINHAS; i++)
            {
                janela.draw(*bolinhas[i]);
            }

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
        while (!encerrar)
        {
            for (int i = 0; i < N_BOLINHAS; i++)
            {
                bolinhas[i]->setPosition(bolinhas[i]->getPosition() + sf::Vector2f(0.f, bpm));
                if (bolinhas[i]->getPosition().y >= 600)
                {
                    bolinhas[i]->setPosition(sf::Vector2f(bolinhas[i]->getPosition().x , -100.f));
                    
                }
                std::this_thread::sleep_for(std::chrono::milliseconds(1));         
            }
        }
    }
    void Fase::atualizarLeds()
    {
        while (!encerrar)
        {
            contador++;
            if (contador % (int) (bpm) == 0)
            {
                int p = contador / bpm*100;
                sf::Color cor = sf::Color(rand() % 255, rand() % 255, rand() % 255);
                bolinhas[(4 * p)%N_BOLINHAS]->setFillColor(cor);
                bolinhas[(4 * p)%N_BOLINHAS + 1]->setFillColor(cor);
                bolinhas[(4 * p)%N_BOLINHAS + 2]->setFillColor(cor);
                bolinhas[(4 * p)%N_BOLINHAS + 3]->setFillColor(cor);
            }   
            std::this_thread::sleep_for(std::chrono::milliseconds(50));         
        }
    }
}