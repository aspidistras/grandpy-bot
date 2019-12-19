function displayInput(){ // create bubble to display user input

    var bubble = document.createElement("div");
    bubble.classList.add("bubble");

    var bubbleText = document.createElement("div");
    bubbleText.classList.add("bubble-text", "bubble-text-input");

    var input = document.createElement("h4");
    var userInput = document.getElementById("question").value;
    input.textContent = userInput;

    bubbleText.appendChild(input);

    bubble.appendChild(bubbleText);

    return bubble;
};

function displayAnswer(text, response){ // create bubble to display GrandPy Bot answer

    var bubble = document.createElement("div");
    bubble.classList.add("bubble");

    var bubbleText = document.createElement("div");
    bubbleText.classList.add("bubble-text", "bubble-text-answer");

    var answer = document.createElement("h4");

    if(response != null){
        answer.textContent = text + response;
    }
    else {
        answer.textContent = text;
    }
    

    bubbleText.appendChild(answer);

    bubble.appendChild(bubbleText);

    return bubble;


};

function displayLink(link) { // creates the bubble to display wiki links

    var bubble = document.createElement("div");
    bubble.classList.add("bubble");

    var bubbleText = document.createElement("div");
    bubbleText.classList.add("bubble-text", "bubble-text-answer");

    var answer = document.createElement("h4");

    var linkText = document.createElement("a");
    linkText.classList.add("link");
    linkText.textContent = "Clique si tu veux en savoir plus sur Wikipédia !";
    linkText.href = link;

    answer.appendChild(linkText);

    bubbleText.appendChild(answer);

    bubble.appendChild(bubbleText);

    return bubble;
};

function readData(data) { // handle returned data

    var jsonData = JSON.parse(data)

    var answers = document.getElementById("answers");

    if(jsonData !== null){ // if app returned data

        if(jsonData["locationDetails"] !== null){
            var answerBubbleAddress = displayAnswer("Voici l'adresse : ", jsonData["locationDetails"]["address"]); // display google maps address
            answers.appendChild(answerBubbleAddress);

            setLocation(jsonData["locationDetails"]["latitude"], jsonData["locationDetails"]["longitude"]); // change marker location
        }
        else {
            var answerBubbleAddress = displayAnswer("Je ne me rappelle plus de l'adresse mais voici quelques informations !", null); // display google maps address
            answers.appendChild(answerBubbleAddress);
        }

        if(jsonData["locationData"] !== null){
            var answerBubbleData = displayAnswer("", jsonData["locationData"]["content"]); // display wiki data
            answers.appendChild(answerBubbleData);

            var answerBubbleLink = displayLink(jsonData["locationData"]["link"]); // display wiki link bubble
            answers.appendChild(answerBubbleLink);
        }
        else {
            var answerBubbleData = displayAnswer("Malheureusement, je ne me rappelle plus de l'histoire de cet endroit.", null); // display wiki data
            answers.appendChild(answerBubbleData);
        }

        answers.scrollTop = answers.scrollHeight;

    }
    else {

        var noResponseAnswersArray = ["Désolé, je n'ai pas trouvé ! Essaye de me poser une autre question", "Je me fais vieux, je ne me rappelle plus de cet endroit, désolé !",
        "Je suis trop fatigué pour répondre à cette question, essaye un autre endroit !"];

        var answerBubbleNoResponse = displayAnswer("", noResponseAnswersArray[Math.floor(Math.random()*noResponseAnswersArray.length)]); // if data == null, display random no reponse answer
        answers.appendChild(answerBubbleNoResponse);

        answers.scrollTop = answers.scrollHeight; // to adjust the scroll to the latest bubbles
    }
};

function run() {
    var input = document.getElementById("question");

    if (input){
        input.addEventListener("keyup",function(e){
            if (e.keyCode === 13) { // if the enter key is pressed

                var answers = document.getElementById("answers");

                var inputBubble = displayInput();
                answers.appendChild(inputBubble); // to display the user input

                var url = "http://" + window.location.host + "/answer?question=" + input.value;

                ajax(url, readData); // calling ajax request

                input.value = ""; // to reset the form

                answers.scrollTop = answers.scrollHeight; // to adjust the scroll to the latest bubbles
            }
        });
    }
};


window.onload = run; // calls the run function on window load
