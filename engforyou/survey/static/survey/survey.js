
const url = window.location.href
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
let userAnswers = [];
let learningProfile = [];


function startQuiz() {
    

    document.getElementById("intro-section").style.display = "none";
    document.getElementById("quiz-section").style.display = "block";

    loadQuestions();
}

function loadQuestions() {
    const questionsContainer = document.getElementById("questions-container");
    questionsContainer.innerHTML = ""; 

    questions.forEach((q, index) => {
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


document.getElementById("quiz-form").addEventListener("submit", function(event) {
    event.preventDefault();

    userAnswers = [];
    questions.forEach((_, index) => {
        const answer = document.querySelector(`input[name="question_${index}"]:checked`);
        if (answer) userAnswers.push(answer.value);
    });

    displayResults();

});


function displayResults() {
    const resultSection = document.getElementById("result-section");
    const quizSection = document.getElementById("quiz-section");
    quizSection.style.display = "none";
    resultSection.style.display = "block";

    const counts = { A: 0, B: 0, C: 0, D: 0 };
userAnswers.forEach(answer => counts[answer]++);

const totalAnswers = userAnswers.length;

const styles = [
    { type: 'Визуал', count: counts.A },
    { type: 'Аудиал', count: counts.B },
    { type: 'Читатель/писатель', count: counts.C },
    { type: 'Кинестетик', count: counts.D }
];

const visualPercent = (styles[0].count / totalAnswers * 100).toFixed(1);
const audioPercent = (styles[1].count / totalAnswers * 100).toFixed(1);
const readerPercent = (styles[2].count / totalAnswers * 100).toFixed(1);
const kinestheticPercent = (styles[3].count / totalAnswers * 100).toFixed(1);

const sortedStyles = [...styles].sort((a, b) => b.count - a.count);

const mainStyle = sortedStyles[0];
const secondaryStyle = sortedStyles[1];

let tips = [];
switch(true) {
    case mainStyle.type === 'Визуал':
        tips = [
            "Используйте диаграммы, графики и видео.",
            "Выделяйте важное цветами.",
            "Обсуждайте идеи с другими.",
            "Слушайте подкасты или записанные лекции."
        ];
        break;
    case mainStyle.type === 'Аудиал':
        tips = [
            "Используйте диаграммы, графики и видео.",
            "Выделяйте важное цветами.",
            "Пишите заметки.",
            "Читайте и пишите конспекты, чтобы лучше запомнить материал."
        ];
        break;
    case mainStyle.type === 'Читатель/писатель':
        tips = [
            "Используйте диаграммы, графики и видео.",
            "Выделяйте важное цветами.",
            "Погружайтесь в практику.",
            "Используйте физические объекты или ролевые игры для обучения."
        ];
        break;
    case mainStyle.type === 'Кинестетик':
        tips = [
            "Используйте диаграммы, графики и видео.",
            "Выделяйте важное цветами.",
            "Погружайтесь в практику.",
            "Используйте физические объекты или ролевые игры для обучения."
        ];
        break;
}

document.getElementById("result-text").innerHTML = `
    <div>Ваши основные стили обучения (${mainStyle.type} + ${secondaryStyle.type}):</div>
    <div>1. ${mainStyle.type} (${(mainStyle.count / totalAnswers * 100).toFixed(1)}%)</div>
    <div>2. ${secondaryStyle.type} (${(secondaryStyle.count / totalAnswers * 100).toFixed(1)}%)</div>
    <div>Распределение остальных стилей:</div>
    <div>${styles.map(style => `${style.type}: ${(style.count / totalAnswers * 100).toFixed(1)}%`).join(', ')}</div>
`;

document.getElementById("learning-tips").innerHTML = tips.map(tip => `<li>${tip}</li>`).join('');

learningProfile = {
    visual_percent: parseFloat(visualPercent),
    audio_percent: parseFloat(audioPercent),
    reader_percent: parseFloat(readerPercent),
    kinesthetic_percent: parseFloat(kinestheticPercent),
    primary_style: mainStyle.type,
    secondary_style: secondaryStyle.type,
};

const csrf = document.getElementsByName('csrfmiddlewaretoken')
const data = {csrfmiddlewaretoken: getCookie('csrftoken'),
    visual_percent: learningProfile.visual_percent,
    audio_percent: learningProfile.audio_percent,
    reader_percent: learningProfile.reader_percent,
    kinesthetic_percent: learningProfile.kinesthetic_percent,
    primary_style: learningProfile.primary_style,
    secondary_style: learningProfile.secondary_style}
$.ajax({
    type: 'POST',
    url: `${url}save/`,
    data: data,
    success: function(response) {
        console.log('Профиль обучения сохранен успешно');
    },
    error: function(xhr, status, error) {
        console.error('Ошибка AJAX запроса:', error);
        console.log('Ответ сервера:', xhr.responseText);
        console.log(data);
    }
});

}



function resetQuiz() {
    document.getElementById("result-section").style.display = "none";
    document.getElementById("intro-section").style.display = "block";

}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}