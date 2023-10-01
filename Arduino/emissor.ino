//#include <nRF24L01.h>
#include <RF24.h>

#define PIN_CE  9
#define PIN_CSN 10

#define POT_PIN A0

uint8_t pipeNumber;
uint8_t payloadSize;

const uint64_t pipeNum = 0x7878787878LL;

RF24 radio(PIN_CE, PIN_CSN);

void setup() {

  // pinMode(GREEN_PIN, INPUT);
  // pinMode(RED_PIN, INPUT);
  pinMode (POT_PIN, INPUT);
  Serial.begin(9600);
  // Serial.begin(115200);
  radio.begin();
  radio.setChannel(115);
  radio.setDataRate (RF24_1MBPS);
  radio.setPALevel(RF24_PA_HIGH);
  radio.enableDynamicPayloads();

  radio.openWritingPipe(pipeNum);

}

char text[] = "00";
int v = 0;
void loop() {
  // if (radio.write(&text, sizeof(text))) {
  //   Serial.println("Delivered " + String(sizeof(text)) + " byte");
  // }
  // else {
  //   Serial.println("Data not delivered");
  // }
  // delay(1000);
  // Serial.println(analogRead(POT_PIN));
  // Serial.print(" ");
  v = analogRead(POT_PIN);
  Serial.println(v);
  if (v <= 255)
    v = 0;
  else if (v <= 512)
    v = 1;
  else if (v <= 767)
    v = 2;
  else 
    v = 3;
  radio.write(&v, sizeof(int));

  delay(200);
}