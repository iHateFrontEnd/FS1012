int TP1 = A1;
int TP2 = A2;
float TP1_Value = 0;
float TP2_Value = 0;
float diff = 0;
void setup() {
  // put your setup code here, to run once:
pinMode(TP1,INPUT);
pinMode(TP2,INPUT);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  TP1_Value = analogRead(TP1);
  TP1_Value = TP1_Value*(5.0/1023.0);
  TP2_Value = analogRead(TP2);
  TP2_Value = TP2_Value*(5.0/1023.0);
  diff = TP1_Value - TP2_Value;
Serial.print("TP1 ");
Serial.print(TP1_Value);

Serial.print("  TP2 ");
Serial.print(TP2_Value);

Serial.print("  diff ");
Serial.println(diff);
delay(500);
}