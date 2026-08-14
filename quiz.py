class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 문자열
        self.choices = choices    # 선택지 리스트 [선택지1, 선택지2, 선택지3, 선택지4]
        self.answer = int(answer) # 정답 번호 (1~4)

    # Dictionary(dict) 형태로 변환 (JSON 저장용)
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    # Dictionary 데이터를 Quiz 객체로 복원하는 메서드
    @classmethod
    def from_dict(cls, data):
        return cls(data["question"], data["choices"], data["answer"])