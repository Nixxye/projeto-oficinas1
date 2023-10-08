#include "../Lcd/Lcd.h"

Lcd::Lcd(char* m):
fd(wiringPiI2CSetup(I2C_ADDR))
{
    strcpy(music, m);
    size = strlen(music);
    if (wiringPiSetup () == -1) exit (1);

    lcd_init();
}
Lcd::Lcd():
music(NULL),
size(0),
fd(wiringPiI2CSetup(I2C_ADDR))
{
    if (wiringPiSetup () == -1) exit (1);

    lcd_init();
}
Lcd::~Lcd()
{

}

void Lcd::execute()
{
    while (!terminar)
    {
        lcdLoc(LINE1);
        typeln("Guitar Healer");
        lcdLoc(LINE2);
        typeln(music);
        moveText(music, size);
        std::this_thread::sleep_for(std::chrono::milliseconds(200)); 
        //ClrLcd();
        ClrScnd();     
    }
}

void Lcd::changeMusic(char* m)
{
    if (m)
        strcpy(music, m);
}
void Lcd::lcd_toggle_enable(int bits)   
{
    // Toggle enable pin on LCD display
    delayMicroseconds(500);
    wiringPiI2CReadReg8(fd, (bits | ENABLE));
    delayMicroseconds(500);
    wiringPiI2CReadReg8(fd, (bits & ~ENABLE));
    delayMicroseconds(500);
}
void Lcd::moveText(char *txt, int tam)
{
  char aux = txt[0];
  for (int i = 0; i < tam - 1; i++)
  {
    txt[i] = txt[i+1];
  }
  txt[tam] = aux;  
}

void Lcd::lcd_init()
{
    // Initialise display
    lcd_byte(0x33, LCD_CMD); // Initialise
    lcd_byte(0x32, LCD_CMD); // Initialise
    lcd_byte(0x06, LCD_CMD); // Cursor move direction
    lcd_byte(0x0C, LCD_CMD); // 0x0F On, Blink Off
    lcd_byte(0x28, LCD_CMD); // Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD); // Clear display
    delayMicroseconds(500);
}
void Lcd::lcd_byte(int bits, int mode)
{
    //Send byte to data pins
    // bits = the data
    // mode = 1 for data, 0 for command
    int bits_high;
    int bits_low;
    // uses the two half byte writes to LCD
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT ;
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT ;

    // High bits
    wiringPiI2CReadReg8(fd, bits_high);
    lcd_toggle_enable(bits_high);

    // Low bits
    wiringPiI2CReadReg8(fd, bits_low);
    lcd_toggle_enable(bits_low);
}
void Lcd::typeInt(int i)
{
    char array1[20];
    sprintf(array1, "%d",  i);
    typeln(array1);
}
void Lcd::typeFloat(float myFloat)
{
  char buffer[20];
  sprintf(buffer, "%4.2f",  myFloat);
  typeln(buffer);    
}
void Lcd::lcdLoc(int line) //move cursor
{
    lcd_byte(line, LCD_CMD);
}
void Lcd::ClrLcd(void) // clr LCD return home
{
    lcd_byte(0x01, LCD_CMD);
    lcd_byte(0x02, LCD_CMD);
}
void Lcd::ClrScnd()
{
    lcdLoc(LINE2);
    typeln("                    ");
    lcdLoc(LINE2);
}
void Lcd::typeln(const char *s)
{
    for (int i = 0; *s && i < 16; i++) lcd_byte(*(s++), LCD_CHR);
}
void Lcd::typeChar(char val)
{
    lcd_byte(val, LCD_CHR);
}


