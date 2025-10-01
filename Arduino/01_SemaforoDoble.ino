const int green1   = 3;
const int yellow1  = 4;
const int red1     = 5;

const int green2   = 10;
const int yellow2  = 11;
const int red2     = 12;

void setup() {
  pinMode(green1, OUTPUT);
  pinMode(yellow1, OUTPUT);
  pinMode(red1, OUTPUT);
  pinMode(green2, OUTPUT);
  pinMode(yellow2, OUTPUT);
  pinMode(red2, OUTPUT);
}

void loop() {
  digitalWrite(green1, HIGH);
  digitalWrite(red2, HIGH);
  delay(4000);

  digitalWrite(green1, LOW);
  digitalWrite(yellow1, HIGH);
  delay(1000);

  digitalWrite(red2, LOW);
  digitalWrite(green2, HIGH);
  digitalWrite(yellow1, LOW);
  digitalWrite(red1, HIGH);
  delay(4000);

  digitalWrite(green2, LOW);
  digitalWrite(yellow2, HIGH);
  delay(1000);

  digitalWrite(yellow2, LOW);
  digitalWrite(red1, LOW);
}
