function createAnswer(){
    var bubble = document.createElement("div");
    bubble.classList.add("bubble");

    var bubbleText = document.createElement("div");
    bubbleText.classList.add("bubble-text");

    var answer = document.createElement("h4");
    answer.textContent = "blabla";

    bubbleText.appendChild(answer);

    bubble.appendChild(bubbleText);

    var answers = document.getElementById("answers");
    answers.appendChild(bubble);
};

function generateResponse() {
    var input = document.getElementById('question');

    input.addEventListener('keyup',function(e){
        if (e.keyCode === 13) {
        createAnswer();
  }
});

};






