#include <String.h>
#include <ESP8266WiFi.h>
#include <Wire.h>  

const char* ssid = "Bond"; 
const char* password = "balu006007"; 
WiFiServer server(80);



String putData(String count, String table="bask1") {
  String host_s=String("192.168.137.1");
  IPAddress IP;IP.fromString(host_s);
  Serial.print("Connecting to ");
  Serial.println(IP);
  String url = "http://"+host_s+"/writer.php?table="+table+"&count="+count;
  Serial.print("At ");
  Serial.println(url);
  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(IP, httpPort)) {
    Serial.println("connection failed");
   
  }
  
  Serial.print("Requesting URL: ");
  Serial.println(url);
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host_s + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
}


#define trigPin 5
#define echoPin  4
int flag = 0;
unsigned long start_time,end_time;
long duration,duration1,count_people = 0;
void setup() {

  Serial.begin(9600); 
  Serial.println("Start : \n");
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
  Serial.println("Server started");
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT);  
  start_time = millis();  
}

void loop() {
  end_time = millis();
  if(end_time - start_time > 600000)
  {
          putData(String(count_people));
          start_time = millis();     
          count_people = 0;              
  }
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);           
  if(int(duration) < 2000)          
  {     
          flag = 1;
          delay(1000);
   }
   else
   {
        if(flag == 1)     
        { 
            count_people ++;
            flag = 0;           
            delay(1000);   
        }
  }
  }
  
