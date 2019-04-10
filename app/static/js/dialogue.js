function displayInput(){

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

function displayAnswer(response){

    var bubble = document.createElement("div");
    bubble.classList.add("bubble");

    var bubbleText = document.createElement("div");
    bubbleText.classList.add("bubble-text", "bubble-text-answer");

    var answer = document.createElement("h4");
    answer.textContent = response;

    bubbleText.appendChild(answer);

    bubble.appendChild(bubbleText);

    return bubble;


};

function readData(data) {

    var jsonData = JSON.parse(data)

    var answers = document.getElementById("answers");

    var answerBubbleAddress = displayAnswer(jsonData["locationDetails"]["address"]);
    answers.appendChild(answerBubbleAddress);

    var answerBubbleData = displayAnswer(jsonData["locationData"]);
    answers.appendChild(answerBubbleData);

    answers.scrollTop = answers.scrollHeight;

    setLocation(jsonData["locationDetails"]["latitude"], jsonData["locationDetails"]["longitude"]);
};

function run() {
    var input = document.getElementById("question");

    if (input){
        input.addEventListener("keyup",function(e){
            if (e.keyCode === 13) {

                var answers = document.getElementById("answers");

                var inputBubble = displayInput();
                answers.appendChild(inputBubble);

                var url = "http://127.0.0.1:5000/answer?question=" + input.value;

                ajax(url, readData);
                input.value = "";

                answers.scrollTop = answers.scrollHeight;
            }
        });
    }
};


window.onload = run;
