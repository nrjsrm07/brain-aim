// Function to start the game
function startgame() {
    // Get the number of players entered by the user
    const numberOfPlayers = document.getElementById("nbp").value;
    
    // Store the number of players in session storage
    sessionStorage.setItem("np", numberOfPlayers)
    
    // Loop through each player input field to get their names
    for (let i = 0; i < numberOfPlayers; i++) {
        let name = document.getElementById("form" + i).value;
        // Store each player's name in session storage with a unique key
        sessionStorage.setItem("name" + i, name);
    }
    
    // Set a default value for bcd_value in session storage
    sessionStorage.setItem('bcd_value', 0);
    
    // Redirect the user to the QuestionPage.html
    window.location = 'QuestionPage.html';
}

// Function to add input fields for player names
function addName() {
    // Get the number of players entered by the user
    const numberOfPlayers = document.getElementById("nbp").value;
    
    // Get the container where input fields will be added
    let inputContainer = document.getElementById("inutContainer");
    
    // Define HTML for input fields and start game button
    const ibe1 = '<input type="text" class="form-control mb-1" style="margin:20px" id="form';
    const ibe2 = '" placeholder="Name of the player">';
    let bv = '';
    
    // Generate input fields for each player
    for (let i = 0; i < numberOfPlayers; i++) {
        bv += (ibe1 + i + ibe2);
    }
    
    // Add start game button
    bv += '<button style="margin:20px" id="startbtn" class="btn btn-primary" onclick="startgame()">Start the Game</button>';
    
    // Set the generated HTML to the input container
    inputContainer.innerHTML = bv;
    
    // Initialize scores for each player in session storage
    for (let i = 0; i < numberOfPlayers; i++) {
        sessionStorage.setItem('score' + i, 0);
    }
}
