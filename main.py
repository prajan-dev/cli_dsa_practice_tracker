from tracker import add_problem, view_problems, update_problem, delete_problem


def main():
    print("=== DSA Practice Tracker ===")

    print("1. Add Problem")
    print("2. View Problems")
    print("3. Update Problem")
    print("4. Delete Problem")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_problem()
    elif choice == "2":
        view_problems()
    elif choice == "3":
        update_problem()
    elif choice == "4":
        delete_problem()
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()