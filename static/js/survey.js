/*const quizData = [
    {
        question: "Which language runs in a web browser?",
        a: "Java",
        b: "C",
        c: "Python",
        d: "JavaScript",
        correct: "d",
    }
];*/

const quizData = {
    int_learn: [
        {
            question: "Blockchain projects development increases my opportunities for a better job."
        },
        {
            question: "I earn respect from others by participating in Blockchain project."
        },
        {
            question: "Participation in Blockchain project improves my reputation in the profession."
        }
    ],
    fin_gain: [
        {
            question: "I am paid in the form of cryptocurrency to work for the Blockchain project."
        },
        {
            question: "I receive some form of compensation in the form of crypto for participating in the Blockchain project."
        },
        {
            question: "For me, working for the Blockchain project is extremely profitable."
        },
        {
            question: "Comparing to other programming jobs, working for the Blockchain project is very poorly paid."
        }
    ],
    tech_norm: [
        {
            question: "I think that, it is wrong to hard fork a Blockchain project."
        },
        {
            question: "I believe it is inappropriate to distribute Blockchain code changes without going through the proper channels."
        },
        {
            question: "I believe that with enough developers working on a particular Blockchain project, any bug can be quickly found and fixed."
        },
        {
            question: "I place great value on technical knowledge in a Blockchain project."
        },
        {
            question: "I think co-operation in Blockchain community is important."
        }
    ]
    ,
    sys_int: [
        {
            question: "I synthesize and integrate my expertise at the Blockchain implementation level."
        },
        {
            question: "I believe members of the Blockchain project on which I work span several areas of expertise to develop shared Blockchain project concepts."
        },
        {
            question: "I can clearly see how different pieces of Blockchain project fit together."
        },
        {
            question: "I competently blend new Blockchain project-related knowledge with what I have already know."
        }
    ],
    code_test: [
        {
            question: "The more difficult the Blockchain code testing problem, the more I enjoy trying to solve it."
        },
        {
            question: "I enjoy relatively complex, complicated Blockchain software code testing tasks."
        },
        {
            question: "I enjoy tackling Blockchain testing problems that are completely new to me."
        },
        {
            question: "I prefer software testing work I know whether I can do well, over software testing that stretched my abilities."
        },
        {
            question: "I enjoy trying to solve complex Blockchain problems."
        }
    ],
    cont_code: [
        {
            question: "To what extent the relationship between your contributed code and the Blockchain core project was characterized by plug-and-play."
        },
        {
            question: "To what extent the relationship between your contributed code and the Blockchain core project was characterized by highly modular."
        },
        {
            question: "To what extent the relationship between your contributed code and the Blockchain core project was characterized by highly interoperable."
        },
        {
            question: "To what extent the relationship between your contributed code and the Blockchain core project was characterized by loosely coupled."
        },
        {
            question: "To what extent the relationship between your contributed code and the Blockchain core project was characterized by small number of interdependencies."
        }
    ],
    dec_right: [
        {
            question: "To what extent the responsibility was distributed between you and the core developers for making decisions about the project features extension."
        },
        {
            question: "To what extent the responsibility was distributed between you and the core developers for making decisions about the functionality extension."
        },
        {
            question: "To what extent the responsibility was distributed between you and the core developers for making decisions about the Design extension."
        },
        {
            question: "To what extent the responsibility was distributed between you and the core developers for making decisions about the implementation extension."
        },
        {
            question: "To what extent the responsibility was distributed between you and the Blockchain community for making decisions about the user interface extension."
        }
    ],
    dev_inv: [
        {
            question: "I consider the Blockchain project to be significant."
        },
        {
            question: "The Blockchain project means a lot to me."
        },
        {
            question: "The Blockchain project is of concern to me."
        },
        {
            question: "I consider the Blockchain project to be relevant to me."
        },
        {
            question: "The Blockchain project matters to me."
        }
    ],
    proj_desert: [
        {
            question: "How frequently do you desert a Blockchain project after having created code patch for the same project implementation?"
        },
        {
            question: "How often do you leave your created code patch for a Blockchain project without contributing them?"
        },
        {
            question: "How often do you create code patch for a Blockchain project, but do not contribute it to the same project?"
        },
        {
            question: "How often do you close your project user ID, before you contribute the code patches to a Blockchain project?"
        },
        {
            question: "How often do you desert a Blockchain project?"
        }
    ]
}

const quizKeys = Object.keys(quizData)

const quiz = document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const submitBtn = document.getElementById('submit')
const errorElem = document.getElementById('error')

let currentKey = 0
let currentCat = quizData[quizKeys[currentKey]]

let currentQuiz = 0
let score = 0

loadQuiz()




















function loadQuiz() {
    deselectAnswers()

    const currentQuizData = currentCat[currentQuiz]


    questionEl.innerText = currentQuizData.question
    
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}

function getSelected() {
    let answer

    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })

    return answer
}

submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    console.log(answer)    
    //set error elem display to none
    errorElem.style.display = 'none';

    //if question is answered get the next question
    if(answer == undefined){
        // go to the next question
        currentQuiz++;

        if(currentQuiz < currentCat.length) {
            loadQuiz()
        }
        else
        {
            currentKey++;
            //reset currentQuiz
            if(currentKey < quizKeys.length){
                currentQuiz = 0

                //set current cat to next cat
                currentCat = quizData[quizKeys[currentKey]]
                loadQuiz()
            }
            else
            {
                //last cat
                if(currentQuiz === currentCat.length){
                    //do something
                    let form = `
                    <form>
                        <h4 style="text-align: center;">Enter your Name & Email Address</h4>
                        <br/>
                        <div class="row">
                            <div class="col-md-6" style="margin: 0 auto;">
                                <div class="form-floating mb-3">
                                    <input class="form-control" id="name" name="name" type="text" placeholder="Enter your name..." required />
                                    <label for="name">Full name</label>
                                    <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6" style="margin: 0 auto;">
                                <div class="form-floating mb-3">
                                    <input class="form-control" id="email" name="email" type="email" placeholder="Email Address..." required />
                                    <label for="email">Email</label>
                                    <div class="invalid-feedback" data-sb-feedback="name:required">Email.</div>
                                </div>
                            </div>
                        </div>
                        <div class="row gx-4 gx-lg-5 justify-content-center mt-5 mb-5">
                            <div class="col-lg-6">
                                <div class="d-grid"><button class="btn btn-success btn-xl" id="submitButton" type="submit">Submit</button></div>
                            </div>
                        </div>
                    </form>
                    `
                    document.getElementById('details-form').innerHTML = form
                }
            }
        }
    }
    else
    {
        errorElem.style.display = 'block';
    }

})