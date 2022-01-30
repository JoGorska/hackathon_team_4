/* Script for bored.html flip game */

var logoptio2url = logoptio2url

var bored_dark_url = bored_dark_url 
var bored_url = bored_url 
var happy_dark_url = happy_dark_url
var happy_url = happy_url
var redness_dark_url = redness_dark_url
var redness_url = redness_url
var sleep_dark_url = sleep_dark_url
var sleep_url = sleep_url

document.addEventListener('DOMContentLoaded', () =>{

    //load all card options
    const allCardsArray = [{
        name: 'Bored',
        img: bored_url
    },
    {
        name: 'Bored - Dark',
        img: bored_dark_url 
    },
    {
        name: 'Happy',
        img: happy_url
    },
    {
        name: 'Happy - Dark',
        img: happy_dark_url
    },
    {
        name: 'Redness',
        img: redness_url
    },
    {
        name: 'Redness - Dark',
        img: redness_dark_url
    },
    {
        name: 'Sleep',
        img: sleep_url
    },
    {
        name: 'Sleep - Dark',
        img: sleep_dark_url
    }
    ];
  
    //array to hold randomly selected cards
    const gameCards = [];
  
    //randomise allCardsArray positioning
    for (let run=0; run < 100000; run++){
        allCardsArray.sort(() => 0.5 - Math.random())
    }
  
    //select first 10 randomised teams for game 
    for(var imgs = 0; imgs < 8; imgs++) {
        gameCards[imgs] = allCardsArray[imgs]
    }
  
    //duplicate first 8 indexs from allCardsArray to back 8 indexs within gameCards array
    for (var j = 8; j <16; j++){
        gameCards[j] = allCardsArray[j-8]
    }
  
    // randomise cards for loading to grid
    gameCards.sort(() => 0.5 - Math.random())
  
    const grid = document.querySelector('.grid')
    
    // Empty arrays for comparing cards and cards IDs
    var cardsToCompare = []
    var cardsToCompareId = []
  
    var matches = 0;
  
    //create game board
    function createBoard() {
        for (let i=0; i<gameCards.length; i++)
        {
            var card = document.createElement('img')
            card.setAttribute('src', logoptio2url)
            card.setAttribute('data-id', i)
            card.setAttribute('class', 'flip-card')
            card.addEventListener('click', flipCard)
            grid.appendChild(card)
        }
  
    }
  
  
    // checking selected cards for a match
    function checkForMatch() {
        var cards = document.querySelectorAll('.flip-card')
        const cardOneId = cardsToCompareId[0]
        const cardTwoId = cardsToCompareId[1]
  
        if(cardOneId === cardTwoId){
            alert('You have selected the same card twice, please only select different cards for matching!')
              cards[cardOneId].setAttribute('src', logoptio2url)
              cards[cardTwoId].setAttribute('src', logoptio2url)
            }
  
        if (cardsToCompare[0] === cardsToCompare[1] && cardOneId != cardTwoId ) {
  
            cards[cardOneId].style.opacity = "0"
            cards[cardTwoId].style.opacity = "0"
            cards[cardOneId].removeEventListener('click', flipCard)
            cards[cardTwoId].removeEventListener('click', flipCard)
            matches++; 
        }
        else {
          cards[cardOneId].setAttribute('src', logoptio2url)
          cards[cardTwoId].setAttribute('src', logoptio2url)
        }
        cardsToCompare = []
        cardsToCompareId = []
  
        if (matches === 8) {
            clearTimeout(interval);
            $('#congratsModal').modal('toggle')
            winningModal(flips, minute, second)
        }
  
    }
  
    // flip card function 
    function flipCard(){
  
        var cardId = this.getAttribute('data-id')
        cardsToCompare.push(gameCards[cardId].name)
        cardsToCompareId.push(cardId)
        this.setAttribute('src', gameCards[cardId].img)
        
        if (cardsToCompare.length === 2 ){
            setTimeout(checkForMatch, 1000)
        }
        // start flip counter
        flipCounter();
        
    }

    createBoard();
  
    let flips = 0
    let counter = document.querySelector('.flips')
  
    // count flips made - inspired from https://scotch.io/tutorials/how-to-build-a-memory-matching-game-in-javascript#toc-3-moves
    function flipCounter() {
        flips++;
        counter.innerHTML = `Flips: ${flips}` 
        if(flips == 1) {
            startTimer()
        }
    }
  
  
    //game timer - code basis from https://github.com/sandraisrael/Memory-Game-fend
    //started second at 1 as it takes 1 second to load new format before continuing to increment
  
    var second = 1, minute = 0
    var timer = document.querySelector("#timer")
    var interval
    function startTimer(){
        interval = setInterval(function(){
            timer.innerHTML = minute+" mins "+second+" secs"
            second++
            if(second == 60){
                minute++
                second = 0;
            }
            if(minute == 60){
                hour++
                minute = 0;
            }
        },1000);
        
    }
  
    // game winning modal - final second count showing as 1 more than it should, so minused 1 second for equality of data
    function winningModal(flips, minute, second) {
        let winModal = document.querySelector('.win')
        winModal.style.visibility = 'visible'
        winModal.querySelector('#totalFlips').innerHTML = `You made ${flips} card flips and `
        winModal.querySelector('#winTime').innerHTML = `you completed the game in ${minute} minutes and ${second - 1} seconds`
  
        matches = 0;
    }
  
  })