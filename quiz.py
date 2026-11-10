class Quiz:
    """퀴즈 한 문제를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        self.question = question  # 문제 (글자, str)
        self.choices = choices    # 선택지 4개 (목록, list)
        self.answer = answer      # 정답 번호 1~4 (숫자, int)

    def display(self, number):
        """문제 번호, 문제, 선택지를 화면에 보여준다."""
        print("-" * 40)
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")
        print()

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False를 돌려준다."""
        return user_answer == self.answer


# 이 파일을 직접 실행했을 때만 동작하는 테스트 코드
if __name__ == "__main__":
    sample = Quiz(
        "원소 기호 'Fe'는 어떤 원소일까요?",
        ["금", "은", "철", "구리"],
        3,
    )
    sample.display(1)
    print("3번을 골랐을 때:", sample.is_correct(3))
    print("1번을 골랐을 때:", sample.is_correct(1))