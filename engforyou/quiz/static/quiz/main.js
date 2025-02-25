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
    <div class="h5 mb-3"> Are you sure you want to begin?</div>
    <div class="text-muted">
        <ul>
            <li>
                difficulty: <b>${difficulty}</b>
                </li>
                 <li>
                num: <b>${number_of_questions}</b>
                </li>
                 <li>
                required_score_to_pass: <b>${required_score_to_pass}</b>
                </li>
                 <li>
                time: <b>${time} min</b>
            </li>
        </ul>
    </div>
    `

    startBtn.addEventListener('click', ()=> {
        window.location.href = url + pk
    })
}))
