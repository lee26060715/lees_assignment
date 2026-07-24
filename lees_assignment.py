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

while True:
    re = input("리눅스 간단퀴즈. 총 3문제 나갑니다. 준비되셨나요?(y/n)")

    if re == "n":
        print("아쉽네요. 프로세스를 종료합니다.")
        break
    elif re == "y" :
        def check_answer(user_answer, correct_answer):
            if user_answer.lower() == correct_answer.lower():
                print("정답입니다.")
                return 1
            else:
                print(f"틀렸습니다. 정답은 {correct_answer} 였습니다.")
                return 0


        quiz_list = [q1, q2, q3, q4, q5]

        selected = random.sample(quiz_list, 3)

        score = 0

        for quiz in selected:
            print(quiz)
            user_answer = input("위 문제의 정답은? ").strip()

            if quiz == q1:
                score += check_answer(user_answer, q1_answer)
            elif quiz == q2:
                score += check_answer(user_answer, q2_answer)
            elif quiz == q3:
                score += check_answer(user_answer, q3_answer)
            elif quiz == q4:
                score += check_answer(user_answer, q4_answer)
            elif quiz == q5:
                score += check_answer(user_answer, q5_answer)

        print()
        print(f"수고하셨습니다. 총 {score} 문제맞추셨습니다.")
        rank = {0: "F", 1: "C", 2: "B", 3: "A"}
        print(f"등급: {rank[score]}")
        print()
        print("혹시 다시 하시겠습니까?")