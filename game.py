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