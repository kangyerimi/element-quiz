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


def get_default_quizzes():
    """처음 실행할 때 사용할 기본 원소 퀴즈 목록을 돌려준다."""
    return [
        Quiz(
            "원소 기호 'Fe'는 어떤 원소일까요?",
            ["금", "은", "철", "구리"],
            3,
        ),
        Quiz(
            "원자 번호 1번, 우주에서 가장 많고 가장 가벼운 원소는?",
            ["수소", "헬륨", "산소", "탄소"],
            1,
        ),
        Quiz(
            "원소 기호 'Au'는 어떤 원소일까요?",
            ["은", "금", "구리", "알루미늄"],
            2,
        ),
        Quiz(
            "풍선에 넣으면 둥둥 떠오르는 가벼운 기체 원소는?",
            ["산소", "질소", "헬륨", "염소"],
            3,
        ),
        Quiz(
            "실온에서 유일하게 액체 상태인 금속 원소는?",
            ["철", "수은", "납", "아연"],
            2,
        ),
        Quiz(
            "다이아몬드와 연필심(흑연)을 이루는 원자 번호 6번 원소는?",
            ["규소", "질소", "탄소", "붕소"],
            3,
        ),
        Quiz(
            "원소 기호 'Na'는 어떤 원소일까요?",
            ["네온", "니켈", "질소", "나트륨"],
            4,
        ),
        Quiz(
            "우리가 숨 쉴 때 꼭 필요한 원자 번호 8번 원소는?",
            ["질소", "산소", "수소", "아르곤"],
            2,
        ),
    ]


# 이 파일을 직접 실행했을 때만 동작하는 테스트 코드
if __name__ == "__main__":
    quizzes = get_default_quizzes()
    print(f"📚 기본 퀴즈 {len(quizzes)}개")

    for number, quiz in enumerate(quizzes, start=1):
        quiz.display(number)
        correct_text = quiz.choices[quiz.answer - 1]
        print(f"  ✅ 정답: {quiz.answer}번 {correct_text}")