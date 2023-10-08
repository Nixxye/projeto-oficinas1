#pragma once 

#include <queue>
#include <RF24/nRF24L01.h>
#include <RF24/RF24.h>

#include "../T_class.h"

#define PIN_CE  17

#define PIN_CSN 0

uint8_t pipeNumber;

uint8_t payloadSize;

// Fazer singleton dps:
class Receptor: public T_class
{
private:
    std::queue<char> inputs;
public:
    Receptor();
    ~Receptor();
    // fazer const:
    std::queue<char>* getFila();
    void captarInputs();
    RF24 radio;
};
