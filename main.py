from game import QuizGame

def main():
    game = QuizGame()

    while True:
        try:
            print("\n====================")
            print("  나만의 퀴즈 게임")
            print("====================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("====================")

            choice = input("선택: ").strip()

            if choice == "1":
                game.play_quiz()
            elif choice == "2":
                game.add_quiz()
            elif choice == "3":
                game.list_quizzes()
            elif choice == "4":
                game.show_score()
            elif choice == "5":
                print("프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
                break
            else:
                print("잘못된 입력입니다. 1~5 사이의 숫자를 입력해 주세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n\n프로그램을 안전하게 종료합니다.")
            break

if __name__ == "__main__":
    main()