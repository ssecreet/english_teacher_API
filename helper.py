import random
import numpy as np
from fastapi.responses import JSONResponse

class Helper:
    def __init__(self):
        self.question_id = 1000
        self.db = {}

        with open("db_ru_en.txt", encoding='utf-8') as f:
            data = f.readlines()

        self.dictionary = {}
        for line in data:
            ru, en = line.split("-")
            self.dictionary[en.strip()] = ru.strip()

    #   =================== GENERATE ======================

    def generate_question_word(self):
        rus = list(self.dictionary.values())
        en_word = random.choice(list(self.dictionary.keys()))
        ru_word = self.dictionary[en_word]
        rus.remove(ru_word)
        var = [ru_word] + random.sample(rus, 3)
        np.random.shuffle(var)

        question_id = self.get_question_id()
        self.db[question_id] = ru_word

        return JSONResponse(status_code=200, content={"question_id": question_id, "variance": var, "english": en_word})

    def generate_question_letter(self):
        self.en_word_l = random.choice(list(self.dictionary.keys()))
        self.lett = [i for i in self.en_word_l if self.en_word_l.count(i) == 1]
        self.rn_ch = random.choice(self.lett)
        self.en_word_l = self.en_word_l.replace(self.rn_ch, "*")

        question_id = self.get_question_id()
        self.db[question_id] = self.rn_ch

        return JSONResponse(status_code=200, content={"question_id": question_id, "en_word": self.en_word_l, "right_answer": self.rn_ch}) #''.join(self.lett)

    #   =================== CHECK ======================

    def check_answer_word(self, question_id, answer):
        if question_id in self.db:
            correct_answer = self.db[question_id]
            return JSONResponse(status_code=201, content={"is_correct": correct_answer == answer})
        else:
            return JSONResponse(status_code=400, content={"is_correct": False, "error": "entered question_id not existing"})

    def check_answer_letter(self, question_id, answer):
        if question_id in self.db:
            correct_answer = self.db[question_id]
            return JSONResponse(status_code=201, content={"is_correct": correct_answer == answer})
        else:
            return JSONResponse(status_code=400, content={"is_correct": False, "error": "entered question_id not existing"})

    #   =================== READ ======================

    def get_correct_result_word(self, question_id):
        if question_id in self.db:
            correct_answer = self.db[question_id]
            return JSONResponse(status_code=200, content={"correct_answer": correct_answer})
        else:
            return JSONResponse(status_code=404, content={"error": "entered question_id not existing"})

    def get_correct_result_letter(self, question_id):
        if question_id in self.db:
            correct_answer = self.db[question_id]
            return JSONResponse(status_code=200, content={"correct_answer": correct_answer})
        else:
            return JSONResponse(status_code=404, content={"error": "entered question_id not existing"})

    def get_question_id(self):
        self.question_id += 1
        return self.question_id