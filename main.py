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


def main():
    """프로그램 전체 흐름을 담당한다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            print("📝 퀴즈 풀기 기능은 준비 중입니다.")
        elif choice == "2":
            print("📌 퀴즈 추가 기능은 준비 중입니다.")
        elif choice == "3":
            print("📋 퀴즈 목록 기능은 준비 중입니다.")
        elif choice == "4":
            print("🏆 점수 확인 기능은 준비 중입니다.")
        elif choice == "5":
            print("👋 게임을 종료합니다. 다음에 또 만나요!")
            break
        else:
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")


if __name__ == "__main__":
    main()