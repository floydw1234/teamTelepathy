var x, yBall;
var a = .1; //acceleration
var v = 0;
var dead = 0;
var score;
var jump = 4; // jump speed
var rectSpeed = 1;

var ballRadius = 24;

var rectPosition = [];



function setup() {
    console.log(windowWidth);
    console.log(windowHeight);
    var w = windowWidth/2;
    var h = windowHeight/2;

  createCanvas(w, h);
  document.getElementsByTagName('canvas')[0].style = "position: fixed;" + "left: 20%;" + "top: 20%;";
  rectPosition = [];
  // Starts in the middle
  x = width/3;
  yBall = height/2;
  rectPosition.push([700, 200 + random(height/2), height]);
  score = 0;

}

function keyPressed() {
  if (key === "A") {
    v = -jump;
  }

  if (keyCode === UP_ARROW) {
    v = -jump;
  }
  if (keyCode === ENTER){
    dead = 0;
    setup();
  }
}
function draw() {
  //console.log(key);
  if(dead === 0){
    background(200);

    // Draw a circle
    stroke(50);
    fill(100);
    ellipse(x, yBall, ballRadius, ballRadius);


    for(i = 0; i < rectPosition.length; i++){
      //moves each pipe
      rect(rectPosition[i][0],rectPosition[i][1], 30, rectPosition[i][2]);
      rectPosition[i][0] = rectPosition[i][0] - rectSpeed;

      //checks for a collision
      detectCollision(i);

    }
    //this checks if it is time for a new "pipe"
    if(rectPosition[rectPosition.length - 1][0] < width- 400){
      var tempHeight = 200 + random(height/2);
      rectPosition.push([width, tempHeight, height]);
      //rectPosition.push([700, 0, tempHeight - 75]);  //

    }
    //if the array is longer than the screen then shorten it
    if(rectPosition.length > 20){//adjust this based on how big the screen is
      rectPosition.splice(0,1);
    }



    //moves iny direction
    yBall = yBall + v;
    //change in velocity
    v = v + a;


    // Reset to the bottom
    if (yBall > height -1) {
      v = -v + 1.2;
      yBall = height - 1;
    }
  score += 0.02;
  textSize(15);
    text("score: " + parseInt(score), 10, 20);
  }else{
    background(255);
    textSize(32);
    text("Game Over. Press Enter to start again!", 10, 30);
    text("your score was: " + parseInt(score), 10, 100);
  }
}


function detectCollision(i){
  //check lower corners
  //console.log(x);
  if(rectPosition.length != 0 && x){
    if(rectPosition[i][1] != 0){    // if it is not an upper pipe == (it is a lower pipe)
      var cornerLx = rectPosition[i][0];
      var cornerLy = rectPosition[i][1];
      var cornerRx = rectPosition[i][0] + 30;
      var cornerRy = rectPosition[i][1];
      if(dist(x, yBall,cornerLx,cornerLy) <= ballRadius -10 || dist(x,yBall,cornerRx,cornerRy) <= ballRadius -10){
        dead = 1;
        return;
      }else if(Math.abs(x - cornerLx) < ballRadius - 10 && yBall > cornerLy){
        dead = 1;
        return;
      }
    }else{  // if it is not an upper pipe then it is a lower pipe
      // check Upper Corners
      cornerLx = rectPosition[i][0];
      cornerLy = rectPosition[i][1] + rectPosition[i][2];
      cornerRx = rectPosition[i][0] + 30;
      cornerRy = rectPosition[i][1] + rectPosition[i][2];

      if(dist(x, yBall,cornerLx,cornerLy) <= ballRadius -15 || dist(x,yBall,cornerRx,cornerRy) <= ballRadius -15){
        dead = 1;
        return;
      }else if(Math.abs(x - cornerLx) < ballRadius - 10 && yBall < cornerLy){
        dead = 1;
        return;
      }
    }
  }
}
