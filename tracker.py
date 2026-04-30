import json
from models import Problem

# Load Data from JSON
def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            return [Problem.from_dict(item) for item in data]
    except:
        return []

# Save Data to JSON

def save_data(problems):
    with open('data.json', 'w') as file:
        json.dump([p.to_dict() for p in problems], file, indent=4)

# Add New Problem

def add_problem():
    problems = load_data()

    id = len(problems) + 1
    title = input('Enter title: ')
    platform = input('Enter platform: ')
    difficulty = input('Enter difficulty: ')
    topic = input('Enter topic: ')
    status = "Unsolved"
    notes = input('Enter notes: ')
    date_added = input ("Enter date: ")

    new_problem = Problem(id, title, platform, difficulty, topic, status, notes, date_added)
    problems.append(new_problem)
    save_data(problems)

    print("Problem added Successfully!" )

def view_problems():
    problems = load_data()

    if not(problems):
        print("No problems found!")
        return
    for p in problems:
        print("-------------------------------------")
        print(f"ID:{p.id}")
        print(f"Title:{p.title}")
        print(f"Platform:{p.platform}")
        print(f"Difficulty:{p.difficulty}")
        print(f"Topic:{p.topic}")
        print(f"Status:{p.status}")
        print(f"Notes:{p.notes}")
        print(f"Date Added:{p.date_added}")


# Update Problem
def update_problem():
    problems = load_data()

    if not problems:
        print("No problem found!")
        return
    #Show all problem first
    for p in problems:
        print(f"{p.id} - {p.title} ({p.status})")
    try:
        problem_id = int(input("Enter problem id to update: "))
    except ValueError:
        print("Invalid input!")
        return

    for p in problems:
        if p.id == problem_id:
            print("1. Mark as Solved")
            print("2. Mark as Unsolved")
            print("3. Revisiting")

            choice = input("Enter choice: ")

            if choice == "1":
                p.status = "Solved"
            elif choice == "2":
                p.status = "Unsolved"
            elif choice == "3":
                p.status = "Revisiting"
            else:
                print("Invalid choice")
                return

            save_data(problems)
            print("Problem updated successfully!")
            return
    print("Problem not found!")

def delete_problem():
    problems = load_data()

    if not problems:
        print("No problem found!")
        return

    # Show all Problems
    for p in problems:
        print(f"{p.id} - {p.title} ")

    try:
        problem_id = int(input("Enter problem id to delete: "))
    except ValueError:
        print("Invalid input!")
        return

    for p in problems:
        if p.id == problem_id:
            problems.remove(p)
            save_data(problems)
            print("Problem deleted successfully!")
            return
    print("Problem not found!")