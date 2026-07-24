import random

q1 = '''
Q1. 리눅스에서 파일/폴더의 권한을 바꾸는 명령어는?

'''

q1_answer = "chmod"


q2 = '''
Q2. 새로운 사용자 계정을 추가하는 명령어는?

'''

q2_answer = "adduser"


q3 = '''
Q3. 현재 로그인(접속) 중인 사용자명을 출력하는 명령어는 무엇인가?

'''

q3_answer = "whoami"

q4 = '''
Q4. 지금까지 터미널에 입력했던 명령어 목록(이력)을 순서대로 보여주는 명령어는 무엇인가?

'''

q4_answer ="history"

q5 = '''
Q5. 리눅스에서 현재 날짜와 시간을 출력하는 명령어는 무엇인가?

'''
q5_answer = "date"

quiz_list = [q1, q2, q3, q4, q5]

selected = random.sample(quiz_list, 3)

for quiz in selected:
    print(quiz)