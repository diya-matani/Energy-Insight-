document.addEventListener("DOMContentLoaded", function() {
    const questions = document.querySelectorAll(".question");
    const nextBtns = document.querySelectorAll(".next-btn");
    const prevBtns = document.querySelectorAll(".prev-btn");
    const predictBtn = document.getElementById("predict-btn");

    let currentQuestionIndex = 0;

    // Colors corresponding to each question
    const colors = [
        "#ffcccc",
        "#ccffcc",
        "#ccccff",
        "#ffccff",
        "#ffffcc",
        "#ccffff",
        "#ff99cc",
        "#99ffcc",
        "#cc99ff",
        "#ffcc99",
        "#99ccff",
        "#ccff99",
        "#ff6666",
        "#66ff66",
        "#6666ff",
        "#ff9966",
        "#66ff99",
        "#9966ff",
        "#ff66cc"
        // Add more colors for each question as needed
    ];
    
    // Show next question
    function showNextQuestion() {
        questions[currentQuestionIndex].classList.add("hidden");
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            questions[currentQuestionIndex].classList.remove("hidden");
        }

        if (currentQuestionIndex === questions.length - 1) {
            predictBtn.classList.remove("hidden");
            nextBtns[currentQuestionIndex].classList.add("hidden");
        }

        prevBtns[currentQuestionIndex].classList.remove("hidden");

        // Update background color based on current question index
        document.body.style.backgroundColor = colors[currentQuestionIndex];
    }

    // Show previous question
    function showPrevQuestion() {
        questions[currentQuestionIndex].classList.add("hidden");
        currentQuestionIndex--;
        questions[currentQuestionIndex].classList.remove("hidden");

        if (currentQuestionIndex === 0) {
            prevBtns[currentQuestionIndex].classList.add("hidden");
        }

        predictBtn.classList.add("hidden");
        nextBtns[currentQuestionIndex].classList.remove("hidden");

        // Update background color based on current question index
        document.body.style.backgroundColor = colors[currentQuestionIndex];
    }

    // Event listeners for next button clicks
    nextBtns.forEach(btn => {
        btn.addEventListener("click", showNextQuestion);
    });

    // Event listener for previous button click
    prevBtns.forEach(btn => {
        btn.addEventListener("click", showPrevQuestion);
    });

    // Event listener for input changes
    const inputs = document.querySelectorAll(".question input");
    inputs.forEach(input => {
        input.addEventListener("input", function() {
            const allFilled = Array.from(inputs).every(input => input.value !== "");
            predictBtn.disabled = !allFilled;
        });
    });

    // Set initial background color
    document.body.style.backgroundColor = colors[currentQuestionIndex];
});
