import requests
from models import *

# user_answer = AnswerRequestBody()


domain = "http://127.0.0.1:8000"
r = requests.request("GET", f"{domain}/word/guess")
print(r.status_code)
print(r.json())
qi = r.json()['question_id']
print("-"*30)

r = requests.request("POST", f"{domain}/word/check", json={"question_id": qi, "answer": r.json()['english']})
print(r.status_code)
print(r.json())
print("-"*30)

r = requests.request("GET", f"{domain}/result/guess_word/{qi}")
print(r.status_code)
print(r.json())
print("-"*30)


#=======================================================================================
r = requests.request("GET", f"{domain}/letter/guess")
print(r.status_code)
print(r.json())
qi = r.json()['question_id']
print("-"*30)

r = requests.request("POST", f"{domain}/letter/check", json={"question_id": qi, "letter": r.json()['right_answer']})
print(r.status_code)
print(r.json())
print("-"*30)

r = requests.request("GET", f"{domain}/result/guess_letter/{qi}")
print(r.status_code)
print(r.json())
print("-"*30)