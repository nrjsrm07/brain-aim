// myjs.js

let currentPlayerKey = Number.parseInt(sessionStorage.getItem("bcd_value"));


function score_update(level, type) {
  const key = "score" + (currentPlayerKey - 1);
  let points = Number.parseInt(sessionStorage.getItem(key));
  if (level == "soft" && type == "truth") {
    points += 5;
  } else if (level == "hard" && type == "truth") {
    points += 7;
  } else if (level == "extreme" && type == "truth") {
    points += 10;
  } else if (level == "soft" && type == "dare") {
    points += 6;
  } else if (level == "hard" && type == "dare") {
    points += 9;
  } else if (level == "extreme" && type == "dare") {
    points += 13;
  }
  sessionStorage.setItem(key, points);
}


function taskDone(level, type) {
  score_update(level, type);
  window.location = "QuestionPage.html";
}

function taskNotDone() {
  window.location = "QuestionPage.html";
}
