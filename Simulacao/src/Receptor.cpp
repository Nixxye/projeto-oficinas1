#include "../Receptor/Receptor.h"
#include <thread>
#include <iostream>
using namespace std;

Receptor::Receptor():
radio(PIN_CE, PIN_CSN),
inputs()
{
    radio.begin();

    radio.setChannel(115);

    radio.setPALevel(RF24_PA_HIGH);

    radio.setDataRate(RF24_1MBPS);

    radio.enableDynamicPayloads();

    radio.openReadingPipe(0, 0x7878787878LL);

    radio.printDetails();
}
Receptor::~Receptor()
{

}
std::queue<char>* Receptor::getFila()
{
    return &inputs;
}
void Receptor::captarInputs()
{
    radio.startListening(); 

    cout << "Start listening..." << endl;

    int receivedData;

    while (!terminar) 
    {

        if (radio.available(&pipeNumber)) 
        {        
            payloadSize = radio.getDynamicPayloadSize();

            int payload[payloadSize];

            receivedData = 0;

            radio.read(&payload, sizeof(payload));

            for (uint8_t i = 0; i < payloadSize; i++) 
            {
                receivedData += payload[i];
            }

            cout << "Pipe : " << (int) pipeNumber << " ";

            cout << "Size : " << (int) payloadSize << " ";

            cout << "Data : " << receivedData << endl;
            
            inputs.push(receivedData);

            std::this_thread::sleep_for(std::chrono::milliseconds(100));     

        }

    }
        
}
