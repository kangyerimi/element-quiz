import json

from quiz import Quiz, get_default_quizzes

STATE_FILE = "state.json"  # 저장 파일 이름 (프로젝트 폴더에 생김)


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스 (게임 진행자)"""

    def __init__(self):
        self.quizzes = []        # 퀴즈 목록 (Quiz 객체들)
        self.best_score = None   # 최고 점수 (아직 없으면 None)
        self.load_state()        # 시작하자마자 저장 파일 불러오기

    # ==================== 입력 처리 ====================

    def get_number(self, prompt, min_value, max_value):
        """min_value~max_value 사이의 숫자를 입력받아 돌려준다.
        잘못 입력하면 안내 메시지를 보여주고 다시 입력받는다."""
        while True:
            text = input(prompt).strip()

            # 1) 빈 입력 (그냥 Enter)
            if text == "":
                print("⚠️ 입력이 비어 있습니다. 숫자를 입력하세요.")
                continue

            # 2) 숫자로 바꿀 수 없는 입력 (예: abc)
            try:
                number = int(text)
            except ValueError:
                print(f"⚠️ 숫자만 입력하세요. ({min_value}-{max_value})")
                continue

            # 3) 범위 밖 숫자 (예: 메뉴에서 9)
            if number < min_value or number > max_value:
                print(f"⚠️ {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue

            # 모든 검사를 통과하면 숫자를 돌려준다
            return number

    def get_text(self, prompt):
        """비어 있지 않은 글자를 입력받아 돌려준다."""
        while True:
            text = input(prompt).strip()

            if text == "":
                print("⚠️ 내용이 비어 있습니다. 다시 입력하세요.")
                continue

            return text

    # ==================== 파일 저장/불러오기 ====================

    def load_state(self):
        """state.json에서 퀴즈 목록과 최고 점수를 불러온다.
        파일이 없거나 손상되면 기본 퀴즈로 시작한다."""
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            quizzes = []
            for item in data["quizzes"]:
                quiz = Quiz(item["question"], item["choices"], item["answer"])
                quizzes.append(quiz)

            self.quizzes = quizzes
            self.best_score = data["best_score"]

            if self.best_score is None:
                print(f"📂 저장된 데이터를 불러왔습니다. "
                      f"(퀴즈 {len(self.quizzes)}개)")
            else:
                print(f"📂 저장된 데이터를 불러왔습니다. "
                      f"(퀴즈 {len(self.quizzes)}개, "
                      f"최고 점수 {self.best_score}점)")

        except FileNotFoundError:
            # 첫 실행: 파일이 아직 없음
            print("📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.reset_to_default()

        except (ValueError, KeyError, TypeError):
            # 파일 내용이 깨졌거나 형식이 이상함
            print("⚠️ 저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            self.reset_to_default()

        except OSError:
            # 그 밖에 파일을 읽을 수 없는 경우
            print("⚠️ 저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
            self.reset_to_default()

    def reset_to_default(self):
        """기본 퀴즈와 빈 최고 점수로 초기화한다."""
        self.quizzes = get_default_quizzes()
        self.best_score = None

    def save_state(self):
        """퀴즈 목록과 최고 점수를 state.json에 저장한다."""
        quiz_list = []
        for quiz in self.quizzes:
            quiz_list.append(quiz.to_dict())

        data = {
            "quizzes": quiz_list,
            "best_score": self.best_score,
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print("💾 데이터를 저장했습니다.")
        except OSError:
            print("⚠️ 데이터를 저장하지 못했습니다.")

    # ==================== 화면 & 기능 ====================

    def show_menu(self):
        """메뉴 화면을 출력한다."""
        print()
        print("=" * 40)
        print("        🧪 원소 퀴즈 게임 🧪")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def play_quiz(self):
        """퀴즈를 순서대로 출제하고, 최고 점수를 갱신해 저장한다."""
        # 퀴즈가 하나도 없는 경우
        if len(self.quizzes) == 0:
            print("📭 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        correct_count = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.display(number)
            user_answer = self.get_number("정답 입력 (1-4): ", 1, 4)

            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                correct_text = quiz.choices[quiz.answer - 1]
                print(f"❌ 아쉬워요! 정답은 {quiz.answer}번 {correct_text}입니다.")

        score = int(correct_count / total * 100)
        print()
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
        self.update_best_score(score)
        print("=" * 40)
        self.save_state()

    def update_best_score(self, score):
        """이번 점수가 최고 점수보다 높으면 갱신한다."""
        if self.best_score is None or score > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score
        else:
            print(f"💪 최고 점수는 {self.best_score}점이에요. 다음엔 꼭 넘어봐요!")

    def add_quiz(self):
        """새 퀴즈를 입력받아 목록에 추가하고 저장한다."""
        print("\n📌 새로운 퀴즈를 추가합니다.\n")

        question = self.get_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = self.get_text(f"선택지 {i}: ")
            choices.append(choice)

        answer = self.get_number("정답 번호 (1-4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        print(f"\n✅ 퀴즈가 추가되었습니다! (총 {len(self.quizzes)}개)")
        self.save_state()

    def show_quiz_list(self):
        """등록된 퀴즈의 문제 목록을 보여준다."""
        # 퀴즈가 하나도 없는 경우
        if len(self.quizzes) == 0:
            print("📭 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def show_score(self):
        """최고 점수를 보여준다."""
        # 아직 한 번도 풀지 않은 경우
        if self.best_score is None:
            print("\n📭 아직 퀴즈를 푼 기록이 없습니다. 1번 메뉴에서 도전해 보세요!")
            return

        print(f"\n🏆 최고 점수: {self.best_score}점")

    # ==================== 게임 실행 ====================

    def run(self):
        """메뉴를 반복해서 보여주며 게임을 진행한다."""
        try:
            while True:
                self.show_menu()
                choice = self.get_number("선택: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    self.save_state()
                    print("👋 게임을 종료합니다. 다음에 또 만나요!")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 프로그램이 중단되었습니다.")
            self.save_state()
            print("안전하게 종료합니다.")