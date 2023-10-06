#include "../Estados/Fase.h"


namespace Estados
{
    Fase::Fase():
    faixa(nullptr),
    bpm(0),
    tamanho(0),
    // janela(sf::VideoMode(600, 600), "Guitar Healer"),
    contador(0),
    receptor(),
    lcd("How to save a life - The Fray - "),
    inputs(receptor.getFila())
    {
        // // janela.setFramerateLimit(60);

        // sf::CircleShape* aux;
        // for (int i = 0; i < N_BOLINHAS; i++)
        // {
        //     aux = new sf::CircleShape(30.f);
        //     aux->setFillColor(sf::Color::White);  
        //     aux->setPosition(sf::Vector2f(100 * (1 + (i % 4)), (100 * ((int) i / 4))));
        //     // bolinhas.push_back(aux);
        // }
    }
    Fase::~Fase()
    {
        // for (int i = 0; i < N_BOLINHAS; i++)
        //     delete bolinhas[i];  
    }
    void Fase::executar()
    {
        carregarFaixa("Musicas/faixa.txt");

        std::thread girar(&Fase::girarEsteira, this);
        std::thread att(&Fase::atualizarLeds, this);
        std::thread atInpts(&Fase::verificarInputs, this);
        std::thread evInputs(&Receptor::captarInputs, &receptor);
        std::thread evInputs(&Lcd::executar, &lcd);


        // if (botão fechar)
        // {
        //     terminar = true;
        //     girar.join();
        //     att.join();
        //     atInpts.join();
        //     evInputs.join();
        //     janela.close();
        // }
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
        while (!terminar)
        {

            std::this_thread::sleep_for(std::chrono::milliseconds(1));         
        }
    }
    void Fase::verificarInputs()
    {
        char rcpt;

        while (!terminar)
        {
            if (!(inputs->empty()))
            {
                rcpt = inputs->front();
                inputs->pop();
                switch (rcpt)
                {
                    case '1':
                        std::cout << "1" << std::endl;
                        break;
                    case '2':
                        std::cout << "2" << std::endl;
                        break;
                    case '3':
                        std::cout << "3" << std::endl;
                        break;
                    case '4':
                        std::cout << "4" << std::endl;
                        break;
                    default:
                        break;
                }
            }
        }
    }
    void Fase::atualizarLeds()
    {
        contador = 8;
        while (!terminar)
        {
            // contador -= 4;
            // if (contador < 0)
            //     contador = N_BOLINHAS - 4;

            // sf::Color cor = sf::Color(rand() % 255, rand() % 255, rand() % 255);
            // bolinhas[contador]->setFillColor(cor);
            // bolinhas[contador + 1]->setFillColor(cor);
            // bolinhas[contador + 2]->setFillColor(cor);
            // bolinhas[contador + 3]->setFillColor(cor);
            // // std::cout << "Pintando " << contador << std::endl;
            std::this_thread::sleep_for(std::chrono::milliseconds(3600/bpm));         
        }
    }
}