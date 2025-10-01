const int motor = 3;
const int start = 8;
const int stop = 9;
bool status = 0;

void setup()
{
  pinMode(stop, INPUT_PULLUP);
  pinMode(start, INPUT_PULLUP);
  pinMode(motor, OUTPUT);
}

void loop()
{
  int lectura_start = digitalRead(start);
  int lectura_stop = digitalRead(stop);

  if (lectura_start == LOW)
  {
    delay(500);
    status = 1;
  }

  if (lectura_stop == LOW)
  {
    status = 0;
  }

  if (status == 0)
  {
    digitalWrite(motor, LOW);
  }
  else
  {
    digitalWrite(motor, HIGH);
  }
}
