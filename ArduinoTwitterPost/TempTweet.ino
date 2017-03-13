/*=============================================================================
#  Author:          Fran Navarro Morales - https://github.com/fnavales
#  Description:     Program that read values of DHT sensor and tweet it!
#  Version:         0.0.1
#  LastChange:      05-03-2017
=============================================================================*/

#include <SPI.h> // needed in Arduino 0019 or later
#include <Ethernet.h>
#include <Twitter.h>
#include "DHT.h"

#define DHTPIN 5          // what digital pin we're connected to
#define DHTTYPE DHT11     // temperature sensor
#define TwitterToken "YOUR-TOKEN-HERE" // put here your own token (get it from http://arduino-tweet.appspot.com/)


// Initialize DHT sensor
DHT dht(DHTPIN, DHTTYPE); // Initialize DHT sensor.

// Ethernet Shield Settings
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

// If you don't specify the IP address, DHCP is used(only in Arduino 1.0 or later).
byte ip[] = { 192, 168, 1, 140 };

// Your Token to Tweet
Twitter twitter(TwitterToken);

void setup()
{
  delay(1000);
  Ethernet.begin(mac, ip);

  Serial.begin(9600);

  dht.begin();
}

void loop()
{

  String data = readSensor();
  char msg[140];
  data.toCharArray(msg, 140);

  sendTweet(msg);

  // Wait a hour between measurements
  delay(3600000);
}

String readSensor()
{
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float hic = dht.computeHeatIndex(t, h, false);

  if (isnan(h) || isnan(t) || isnan(hic)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  String stringMsg = "";

  stringMsg += "Humedad: ";
  stringMsg += (int) h;
  stringMsg += "%  ";
  stringMsg += "Temperatura: ";
  stringMsg += (int) t;
  stringMsg += "C  ";
  stringMsg += "Sensacion Termica: ";
  stringMsg += hic;
  stringMsg += "C";
  stringMsg += "  #oddgrx17";

  Serial.println(msg);

  return stringMsg;
}


void sendTweet(char msg[])
{
  Serial.println("connecting ...");
  if (twitter.post(msg)) {
    int status = twitter.wait(&Serial);
    if (status == 200) {
      Serial.println("OK.");
      Serial.println("Message Tweeted");
    } else {
      Serial.print("failed : code ");
      Serial.println(status);
    }
  } else {
    Serial.println("connection failed.");
    Serial.println("Message Not Tweeted");
  }
}
