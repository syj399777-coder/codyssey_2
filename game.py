import json
import os
from quiz import Quiz  # 같은 폴더의 quiz.py에서 Quiz 클래스를 가져옴

class QuizGame:
    def __init__(self, filename="state.json"):
        self.filename = filename
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    # 안전하게 정수 입력을 받는 도우미 함수
    def input_int(self, prompt, min_val, max_val):
        while True:
            try:
                raw_input = input(prompt).strip()
                if not raw_input:
                    print("빈 값은 입력할 수 없습니다. 다시 입력해 주세요.")
                    continue
                val = int(raw_input)
                if min_val <= val <= max_val:
                    return val
                else:
                    print(f"{min_val}~{max_val} 사이의 숫자를 입력해 주세요.")
            except ValueError:
                print("숫자만 입력 가능합니다. 다시 입력해 주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되었습니다. 메인 메뉴로 돌아갑니다.")
                return None

    # 기본 초기 퀴즈 생성 (파일이 없을 경우)
    def create_default_quizzes(self):
        default_data = [
            Quiz("파이썬의 창시자는 누구일까요?", ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Steve Jobs"], 1),
            Quiz("다음 중 파이썬의 기본 자료형이 아닌 것은?", ["list", "dict", "str", "array"], 4),
            Quiz("파이썬에서 화면에 내용을 출력하는 함수는?", ["console.log()", "print()", "printf()", "Write-Output"], 2),
            Quiz("파이썬 파일의 확장자는 무엇일까요?", [".java", ".cpp", ".py", ".html"], 3),
            Quiz("조건문을 작성할 때 사용하는 키워드는?", ["if", "for", "while", "def"], 1)
        ]
        self.quizzes = default_data
        self.best_score = 0
        self.save_data()

        # 데이터 저장 (state.json)
    def save_data(self):
        try:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score
            }
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"데이터 저장 실패: {e}")

            # 데이터 불러오기 (state.json)
    def load_data(self):
        if not os.path.exists(self.filename):
            self.create_default_quizzes()
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)
        except Exception:
            print("데이터 파일이 손상되었거나 읽을 수 없어 기본 데이터로 초기화합니다.")
            self.create_default_quizzes()

            # 1. 퀴즈 풀기
    def play_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print(f"\n▶ 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0

        for idx, q in enumerate(self.quizzes, 1):
            print(f"\n[문제 {idx}] {q.question}")
            for i, choice in enumerate(q.choices, 1):
                print(f"  {i}. {choice}")

            user_ans = self.input_int("정답 입력 (1-4): ", 1, 4)
            if user_ans is None:
                print("퀴즈 풀기가 중단되었습니다.")
                return

            if user_ans == q.answer:
                print("정답입니다!")
                score += 1
            else:
                print(f"틀렸습니다. 정답은 {q.answer}번입니다.")

        print(f"\n결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        if score > self.best_score:
            self.best_score = score
            self.save_data()
            print("★ 새로운 최고 점수입니다! ★")

            # 2. 퀴즈 추가
    def add_quiz(self):
        print("\n--- 새로운 퀴즈 추가 ---")
        question = input("문제를 입력하세요: ").strip()
        while not question:
            print("문제 내용은 비어있을 수 없습니다.")
            question = input("문제를 입력하세요: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            while not choice:
                print("선택지는 비어있을 수 없습니다.")
                choice = input(f"선택지 {i}: ").strip()
            choices.append(choice)

        answer = self.input_int("정답 번호 (1-4): ", 1, 4)
        if answer is None:
            return

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("퀴즈가 추가되었습니다!")

        # 3. 퀴즈 목록
    def list_quizzes(self):
        print(f"\n■ 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for idx, q in enumerate(self.quizzes, 1):
            print(f"[{idx}] {q.question}")

    # 4. 점수 확인
    def show_score(self):
        print(f"\n 최고 점수: {self.best_score}점 (총 {len(self.quizzes)}문제 기준)")