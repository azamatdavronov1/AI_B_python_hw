import json
import csv

tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

with open("tasks.json", "w") as file:
    json.dump(tasks_data, file, indent=4)

print("'tasks.json' has been created.")

def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)

tasks = load_tasks()

print("\nTask List:")
print("ID | Task Name          | Completed | Priority")
print("-" * 40)
for task in tasks:
    print(f"{task['id']:2} | {task['task']:18} | {task['completed']} | {task['priority']}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

calculate_stats(tasks)

tasks[0]["completed"] = True
with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

print("\nChanges saved to 'tasks.json'.")

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, "r") as file:
        tasks = json.load(file)

    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

    print(f"'{csv_file}' has been created.")

convert_json_to_csv("tasks.json", "tasks.csv")

