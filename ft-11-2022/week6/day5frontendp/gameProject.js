

const searchGames = async () =>{
const topGameContainer = document.querySelector(".topGameContainer");
topGameContainer.innerHTML = "";
const inputField = document.querySelector(".searchField").value.replace(/\s/g, "-");
console.log(inputField)
const gameURL = `https://rawg.io/api/games/${inputField}?key=6510d2e2abd840f3991d0c506e2d48c4`

const rawData = await fetch(gameURL);
const json = await rawData.json();
console.log(json)


// json.(async(game) =>{
    const gameCard = document.createElement("div")

    const gameMature = document.createElement("h1")

    const gameTitle = document.createElement("h1")

    const gamePoster = document.createElement("img")

    const gameDescription = document.createElement("p")

    const gameYear = document.createElement("p")

    const gameRating = document.createElement("p")
    
    const gameType = document.createElement("p")

    const gameDev = document.createElement("h3")

    
     const allGamesData = `https://rawg.io/api/games/${inputField}?key=6510d2e2abd840f3991d0c506e2d48c4`
      const fetchAllGames = await fetch(allGamesData);
      const individualJson = await fetchAllGames.json();
    //   console.log(json.description);

      gameCard.classList = "gameCard"
      gamePoster.classList = "gamePoster"
      gameMature.classList = "gameMature"
      gameDescription.classList = "gameDescription"
      gameYear.classList = "gameYear"
      gameRating.classList = "gameRating"
      gameType.classList = "gameType"
      gameDev.classList = "gameDev"
      gameTitle.classList = "gameTitle"
      gameDev.innerHTML = "Created By... " + json.developers[0].name
      if(json.esrb_rating=== null){
        gameMature.innerHTML = "Maturity Ranking not specified"     
      } else{

      
      gameMature.innerHTML = "Maturity Ranking: " + json.esrb_rating.name;
    }
      gameType.innerHTML = "Genre: " + json.genres[0].name;
      if(json.genres.name === ""){
        gameType.innerHTML = "Genre Not Specified"     
      } else{

      
        gameType.innerHTML = "Genre: " + json.genres[0].name;
    }


      gameTitle.innerText = json.name;
      gamePoster.src = json.background_image;
      gameDescription.innerText = json.description.replace(/<[^>]*>/g, '');
      gameYear.innerText = "Release Date: "+ json.released;
      gameRating.innerHTML = "Gamers Overall Rating: " + json.rating

      gameCard.append(gameTitle, gamePoster, gameMature,  gameDescription, gameYear, gameRating, gameType, gameDev);
      topGameContainer.append(gameCard)
      


}
const searchButton = document.querySelector(".searchButton")
searchButton.addEventListener("click",searchGames);

const menu = document.querySelector("#mobileMenu")
const menuLinks = document.querySelector(".navBarMenu")

menu.addEventListener("click", function(){
    menu.classList.toggle("is-active")
    menuLinks.classList.toggle("active")
})