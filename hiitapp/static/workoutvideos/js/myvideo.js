var action_name = document.getElementById("action-name");
var action_time = document.getElementById("action-time");

var timesets = [{
  type: "ON",
  duration: 20
},{
  type: "REST",
  duration: 10
},
{
  type: "ON",
  duration: 20
},{
  type: "REST",
  duration: 10
}]

var currentsec = 5;
var currentaction = "Get Ready!";
var currenttimeset_iteration = 0;
var interval;

action_name.innerHTML = currentaction;

function startCountdown(){
  interval = setInterval(function(){
    countdown();
  },1000);
}

function countdown(){
  checktime();
  action_name.innerHTML = currentaction;
  action_time.innerHTML = currentsec;
  console.log(currenttimeset_iteration);
  console.log(currentsec);
  console.log(currentaction);
  currentsec-= 1;
}

function checktime(){
  if(currentsec == 0){
    currentaction = timesets[currenttimeset_iteration].type;
    currentsec = timesets[currenttimeset_iteration].duration;
    currenttimeset_iteration++;
  }
}

function pauseCountdown(){
  clearInterval(interval);
}
