// Change the variable c to your birth year which will represent the number of circles in the pattern
// Variable c is located directly below

int c = 2002;
int a, b;
float windowWidth = 1.5;
boolean capture;

void setup() {
  size(800, 800);
  colorMode(HSB, 200);
}

void draw() {
  float x, y, r;
  if (capture) {
    size(4000, 4000);
  } else {
    size(800,800);
  }
  background(0);

  if (! capture) {
    a = int(map(mouseX, 0, width, 1, 13));
    b = int(map(mouseY, height, 0, 1, 33));
  }
  fill(255, 100);
  textAlign(LEFT, CENTER);
  textSize(12);
	text("Birth Month (a) = " + str(a), 0, height-90);
	text("Birth Day (b) = " + str(b), 0, height-75);
  text("Birth Year (c) = " + str(c), 0, height-60);
  text("X(k)= cos((a*2*PI*k)/c) * (1-0.5*pow(cos((b*PI*k)/c),4))", 0, height-45);
  text("Y(k)= sin((a*2*PI*k)/c) * (1-0.5*pow(cos((b*PI*k)/c),4))", 0, height-30);
  text("R(k)= 1.0/20 + 1.0/18 * pow(sin((52*PI*k)/c),4)", 0, height-15);


  for (float k = 0; k <= 1986; k+=1) {
    y = sin((a*2*PI*k)/c) * (1-0.5*pow(cos((b*PI*k)/c), 4));
    x = cos((a*2*PI*k)/c) * (1-0.5*pow(cos((b*PI*k)/c), 4));
    r = 1.0/20 + 1.0/18 * pow(sin((52*PI*k)/c), 4);    


    float h = map(k, 0, c/3, 0, 255);
    h %= 255;
    if (capture){
      stroke(h,200,255,120);
    } else {
      stroke(h, 200, 255, 40);
    }
    noFill();
    x = map(x, -1*windowWidth, windowWidth, 0, width);
    y = map(y, -1*windowWidth, windowWidth, height, 0);
    r = map(r, 0, windowWidth, 0, width/2);

    ellipse(x, y, 2*r, 2*r);
  }
  if (capture) {
    save("Frame_a-"+str(a)+"_b-"+str(b)+"_c-"+str(c)+".png");
    capture = false;
  }
}

void keyPressed() {
  if (keyCode == UP) {
    c++;
  } else if (keyCode == DOWN) {
    c--;
  } else {
    capture = true;
  }
}
