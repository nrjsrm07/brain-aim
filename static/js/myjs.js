// let numberOfPlayers = sessionStorage.getItem("np");
// let scoreTableContent = document.getElementById("scorecard");

// const score_table = () => {
//   try {
//     let listOfPlayers = "";
//     for (let i = 0; i < numberOfPlayers; i++) {
//       let name = sessionStorage.getItem("name" + i);
//       let score = sessionStorage.getItem("score" + i);
//       let playerDetails =
//         "<tr><td>" + name + "</td><td>" + score + "</td></tr>";
//       listOfPlayers += playerDetails;
//     }
//     scoreTableContent.innerHTML = listOfPlayers;
//   } catch (error) {
//     console.log(error);
//   }
// };

let currentPlayerKey = Number.parseInt(sessionStorage.getItem("bcd_value"));

// function cpNameKey() {
//   let currentPlayerNameKey = "";
//   if (currentPlayerKey == numberOfPlayers) {
//     currentPlayerKey = 0;
//   }
//   currentPlayerNameKey = "name" + currentPlayerKey;
//   sessionStorage.setItem("bcd_value", currentPlayerKey + 1);
//   return currentPlayerNameKey;
// }

// function print_name() {
//   try {
//     const currentPlayerNameKey = cpNameKey();
//     const name = sessionStorage.getItem(currentPlayerNameKey);
//     const turnid = document.getElementById("turn_id");
//     const htmlContent =
//       "<h1> <b>" +
//       name +
//       "</b>, choose level and than anyone from Truth or Dare</h1>";
//     turnid.innerHTML = htmlContent;
//   } catch (error) {
//     console.log(error);
//   }
// }

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

// score_table();

// print_name();

function taskDone(level, type) {
  score_update(level, type);
  window.location = "QuestionPage.html";
}

function taskNotDone() {
  window.location = "QuestionPage.html";
}
