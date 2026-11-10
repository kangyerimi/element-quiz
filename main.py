def show_menu():
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


def get_number(prompt, min_value, max_value):
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


def main():
    """프로그램 전체 흐름을 담당한다."""
    try:
        while True:
            show_menu()
            choice = get_number("선택: ", 1, 5)

            if choice == 1:
                print("📝 퀴즈 풀기 기능은 준비 중입니다.")
            elif choice == 2:
                print("📌 퀴즈 추가 기능은 준비 중입니다.")
            elif choice == 3:
                print("📋 퀴즈 목록 기능은 준비 중입니다.")
            elif choice == 4:
                print("🏆 점수 확인 기능은 준비 중입니다.")
            elif choice == 5:
                print("👋 게임을 종료합니다. 다음에 또 만나요!")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램이 중단되었습니다. 안전하게 종료합니다.")


if __name__ == "__main__":
    main()