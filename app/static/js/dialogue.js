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
    answer.textContent = "blbala";

    bubbleText.appendChild(answer);

    bubble.appendChild(bubbleText);

    return bubble;


};

function display() {
    var input = document.getElementById("question");

    if (input){
        input.addEventListener("keyup",function(e){
            if (e.keyCode === 13) {

                var answers = document.getElementById("answers");

                var inputBubble = displayInput();
                answers.appendChild(inputBubble);

                input.value = "";

                var url = "https://grandpy-bot-oc.herokuapp.com";

                var response = ajax(url);

                var answerBubble = displayAnswer(response);
                answers.appendChild(answerBubble);

                answers.scrollTop = answers.scrollHeight;

                setLocation(35.689487, 139.691706);
            }
        });
    }
};


window.onload = display;
