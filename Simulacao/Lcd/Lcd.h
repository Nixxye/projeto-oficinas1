#pragma once

#include "../T_class.h"
//SDA -> GPIO2
//SLC -> GPIO3
#include <wiringPiI2C.h>
#include <wiringPi.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define I2C_ADDR   0x27 // I2C device address

// Define some device constants
#define LCD_CHR  1 // Mode - Sending data
#define LCD_CMD  0 // Mode - Sending command

#define LINE1  0x80 // 1st line
#define LINE2  0xC0 // 2nd line

#define LCD_BACKLIGHT   0x08  // On
// LCD_BACKLIGHT = 0x00  # Off

#define ENABLE  0b00000100 // Enable bit

class Lcd: public T_class
{
private:
    void lcd_init();
    void lcd_byte(int bits, int mode);
    void lcd_toggle_enable(int bits) 
    void typeInt(int i);
    void typeFloat(float myFloat);
    void lcdLoc(int line); //move cursor
    void ClrLcd(void); // clr LCD return home
    void ClrScnd();
    void moveText(char *txt, int tam);
    void typeln(const char *s);
    void typeChar(char val);
    int fd;
    char *music; 
    int size;
public:
    Lcd(char* m = " ");
    ~Lcd();
    void changeMusic(char* m);
    void execute();
};