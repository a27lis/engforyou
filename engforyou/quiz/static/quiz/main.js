const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=> {
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-name')
    const number_of_questions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const time = modalBtn.getAttribute('data-time')
    const required_score_to_pass = modalBtn.getAttribute('data-pass')

    const url = window.location.href

    modalBody.innerHTML = `
    <div class="h5 mb-3">Вы готовы начать?</div>
    <div class="text-muted">
        <ol class="modal-quiz-ul">
            <li  class="modal-quiz-ul">
                Сложность: <b>${difficulty}</b>
                </li>
                 <li>
                Количество вопросов: <b>${number_of_questions}</b>
                </li>
                 <li>
                Успешное прохождение от: <b>${required_score_to_pass}%</b>
                </li>
                 <li>
                Время: <b>${time} минут</b>
            </li>
        </ol>
    </div>
    `

    startBtn.addEventListener('click', ()=> {
        window.location.href = url + pk
    })
}))
