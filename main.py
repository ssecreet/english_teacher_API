from fastapi import FastAPI, Path
import uvicorn
from fastapi.responses import HTMLResponse, JSONResponse

from helper import Helper
from models import AnswerRequestBody, LetterRequestBody

# Endpoints:
# word/guess,   word/check,    word/result
# letter/guess,   letter/check,    letter/result

app = FastAPI()  # create API service
helper = Helper()  # database, questions

@app.get("/info")
def get_info_about_project():
    return {"About": "simple app", "Project founder": "Mokaev Biyaslan", "Location": "Nalchik", "Phone": "88005553535"}

#===================WORD====================
@app.get("/word/guess")
def guess_word():
    return helper.generate_question_word()

@app.post("/word/check")
def guess_word_check(user_answer: AnswerRequestBody):
    return helper.check_answer_word(user_answer.question_id, user_answer.answer)

@app.get("/result/guess_word/{question_id}")
def guess_word_check_result(question_id: int):
    return helper.get_correct_result_word(question_id)

#==================LETTER====================
@app.get("/letter/guess")
def guess_letter():
    return helper.generate_question_letter()

@app.post("/letter/check")
def guess_letter_check(user_answer: LetterRequestBody):
    return helper.check_answer_letter(user_answer.question_id, user_answer.letter)

@app.get("/result/guess_letter/{question_id}")
def guess_letter_check_result(question_id: int = Path(1000, gt=0, description="question id from response")):
    return helper.get_correct_result_letter(question_id)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)