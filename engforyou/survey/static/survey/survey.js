
const questions = [
    {
        question: "Если вы учитесь готовить, что вам подходит:",
        options: [
            "A) Посмотреть видео-рецепт.",
            "B) Послушать как кто-то объясняет рецепт.",
            "C) Прочитать рецепт.",
            "D) Готовлю и дегустирую блюдо самостоятельно."
        ]
    },
    {
        question: "Что вам больше всего помогает при решении проблемы?",
        options: [
            "A) Посмотреть на графики и диаграммы.",
            "B) Послушать чье-то объяснение.",
            "C) Прочитать инструкцию по шагам.",
            "D) Просто пробовать, пока не получится."
        ]
    },
    {
        question: "Как вы лучше всего запоминаете вещи?",
        options: [
            "A) Рисуя картинки или рассматривая изображения.",
            "B) Повторяя информацию вслух.",
            "C) Записывая и пересматривая.",
            "D) Используя в реальной жизни."
        ]
    },
    {
        question: "Как вы предпочитаете запоминать свои домашние задания?",
        options: [
            "A) Записывать их в яркий планнер.",
            "B) Проговаривать их самому себе вслух.",
            "C) Записывать в списко в записной книге.",
            "D) Ассоциировать их с чем-то, сделанным в классе."
        ]
    },
    {
        question: "Если вы хотите узнать о чем то больше, как вы это делаете?",
        options: [
            "A) Смотрю на картинки и диаграммы.",
            "B) Обсужу этот вопрос с кем-то.",
            "C) Почитаю об этом или напишу.",
            "D) Просто попробую сделать что-то новое."
        ]
    },
    {
        question: "Когда ваш преподаватель объясняет что-то, на чем вы фокусируетесь?",
        options: [
            "A) Смотрю как он пишет или рисует на доске.",
            "B) Слушаю его голос.",
            "C) Читаю заметки по теме.",
            "D) Делаю упражнение, которое он объясняет."
        ]
    },
    {
        question: "Когда вы работаете над проектом, что помогает вам систематизировать ваши идеи?",
        options: [
            "A) Рисовать блок-схему или маинд-карту.",
            "B) Обсуждение моих идей с другими.",
            "C) Написание пошагово плана.",
            "D) Создание чего-либо, связанного с проектом."
        ]
    },
    {
        question: "Как вы предпочитаете знакомиться с различными культурами другого народа?",
        options: [
            "A) Рассматривать традиционную одежду или фотографии.",
            "B) Слушать, как кто-то рассказывает о культуре.",
            "C) Читать истории о культуре.",
            "D) Съездить в путешествие и познакомиться с другим народом лично."
        ]
    },
    {
        question: "Когда вы работаете в группе, как вы вносите наибольший вклад?",
        options: [
            "A) Создаю красочную презентацию.",
            "B) Объясняю всем идею вслух.",
            "C) Записываю все идеи и потом делюсь ими.",
            "D) Реализую идеи."
        ]
    },
    {
        question: "Что вам больше всего нравится в обучении?",
        options: [
            "A) Рисовать или рассматривать картинки того, чему я учусь.",
            "B) Слушать, как кто-то объясняет что-то новое и неизвестное.",
            "C) Читать книги и писать конспекты.",
            "D) Выполнение таких действий, как создание или ролевые игры."
        ]
    },

];

// Store user answers
let userAnswers = [];

// Start the quiz
function startQuiz() {
    

    document.getElementById("intro-section").style.display = "none";
    document.getElementById("quiz-section").style.display = "block";

    loadQuestions();
}

// Load questions dynamically with horizontal lines
function loadQuestions() {
    const questionsContainer = document.getElementById("questions-container");
    questionsContainer.innerHTML = ""; // Clear any existing content

    questions.forEach((q, index) => {
        // Build the question HTML with a horizontal line
        const questionHTML = `
            <div class="question">

                <p><strong>${index + 1}. ${q.question}</strong></p>
                
                ${q.options.map((option, i) => `
                    
                   
                    <div class="row">
                        <div class="col-8">
                             <div class="radio-text">${option}</div>
                        </div>
                        <div class="col-4">
                            <input type="radio" class="radio" name="question_${index}" value="${option.charAt(0)}" required>
                        </div>
                    </div>                    
                `).join('')}
                
            </div>
            ${index < questions.length - 1 ? '<hr>' : ''} <!-- Add an <hr> except after the last question -->
        `;

        questionsContainer.insertAdjacentHTML("beforeend", questionHTML);
    });
}


// Handle form submission
document.getElementById("quiz-form").addEventListener("submit", function(event) {
    event.preventDefault();

    userAnswers = [];
    questions.forEach((_, index) => {
        const answer = document.querySelector(`input[name="question_${index}"]:checked`);
        if (answer) userAnswers.push(answer.value);
    });

    displayResults();
});

// Calculate and display results
function displayResults() {
    const resultSection = document.getElementById("result-section");
    const quizSection = document.getElementById("quiz-section");
    quizSection.style.display = "none";
    resultSection.style.display = "block";

    // Count answers
    const counts = { A: 0, B: 0, C: 0, D: 0 };
    userAnswers.forEach(answer => counts[answer]++);

    // Determine learning style
    let result = "";
    let tips = [];
    const maxAnswer = Math.max(counts.A, counts.B, counts.C, counts.D);

    if (counts.A === maxAnswer) {
        result = "Визуал";
        tips = ["Используйте диаграммы, графики и видео.", "Выделяйте важное цветами."];
    } else if (counts.B === maxAnswer) {
        result = "Аудиал";
        tips = ["Обсуждайте идеи с другими.", "Слушайте подкасты или записанные лекции."];
    } else if (counts.C === maxAnswer) {
        result = "Читатель/писатель";
        tips = ["Пишите заметки.", "Читайте и пишите конспекты, чтобы лучше запомнить материал."];
    } else if (counts.D === maxAnswer) {
        result = "Кинестетик";
        tips = ["Погружайтесь в практику.", "Используйте физические объекты или ролевые игры для обучения."];
    }

    // Display result
    document.getElementById("result-text").innerText = `Ваш стиль обучения: ${result}`;
    document.getElementById("learning-tips").innerHTML = tips.map(tip => `<li>${tip}</li>`).join('');
}

// Reset the quiz
function resetQuiz() {
    document.getElementById("result-section").style.display = "none";
    document.getElementById("intro-section").style.display = "block";

}