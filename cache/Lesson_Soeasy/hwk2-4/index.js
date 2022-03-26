var rolling, random = 1;
var pos = 1;
var animal;
// 開始抽
function spin() {
  var ck = document.getElementById("name_in").value;
  if (ck == "null") {
    alert("你沒有輸入名字");
  }
  else {
    setTimeout(function stoptoroll() { stop(); }, 1000);
    rolling = setInterval(roll, 20);
  }
}
function roll() {
  document.getElementById(pos).style.opacity = 1;
  pos = Math.floor(Math.random() * 12) + 1;
  document.getElementById(pos).style.opacity = 0.6;
  document.getElementById("in").innerHTML = pos;
}
function stop() {
  clearInterval(rolling);
}
function show() {
  var animal_out;
  var ck = document.getElementById("name_in").value;
  var animal_in = pos;
  if (ck == "null") {
    alert("你沒有輸入名字");
    document.getElementById("name_out").innerHTML = "請輸入名字後，再試一次！";
  }
  else {
    if (animal_in == 1) {
      animal_out = "北極熊";
    } else if (animal_in == 2) {
      animal_out = "牛";
    } else if (animal_in == 3) {
      animal_out = "猴子";
    } else if (animal_in == 4) {
      animal_out = "狗";
    } else if (animal_in == 5) {
      animal_out = "浣熊";
    } else if (animal_in == 6) {
      animal_out = "狼";
    } else if (animal_in == 7) {
      animal_out = "河馬";
    } else if (animal_in == 8) {
      animal_out = "羊";
    } else if (animal_in == 9) {
      animal_out = "貓";
    } else if (animal_in == 10) {
      animal_out = "鹿";
    } else if (animal_in == 11) {
      animal_out = "魷魚";
    } else if (animal_in == 12) {
      animal_out = "馬";
    }
    document.getElementById("name_out").innerHTML = ck + " 的命運動物是：" + animal_out;
  }
}
