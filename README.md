# 📝 To-Do Application CRUD

This is a simple application for managing to-do tasks using CRUD (Create, Read, Update, Delete) operations. The code is written in Python and allows users to manage tasks through a command-line interface.

## 📄 Description

The application allows:
- **➕ Add Task:**  Add a new task with a unique identifier, description, status, and estimated time.
- **📋List Tasks:** Show all tasks with their details.
- **✏️ Update Task: ** Modify the information of an existing task.
- **❌Delete Task:** Remove an existing task from the list.

## 🗃️ Data Structure

Tasks are stored in a Python dictionary with the following format:

tasks = {
  "01": {
    "description": "Requirements gathering",
    "status": "pending",
    "time": 60
  },
  "02": {
    "description": "Schedule medical appointments",
    "status": "pending",
    "time": 180
  },
  "03": {
    "description": "CRUD Customers",
    "status": "pending",
    "time": 50
  }
}
##🔧 Main Functions
- read(tasks): Prints all tasks.

- create(tasks, identifier, newTask): Adds a new task to the dictionary..

- update(tasks, identifier, updatedTask): Updates an existing task in the dictionary.
- delete(tasks, identifier): Removes a task from the dictionary.

## 🛠️Usage
PTo run the application, simply run the script in a Python environment. An interactive menu will be presented where you can select the different options:

➕ Add Task
📋 List Tasks
✏️ Update Task
❌ Delete Task
🚪 Exit
###▶️ Execution Example
python tallerDiccionarios2.py 
###➕ Add Task	
- Enter Task ID:04
- Enter Task Description: Review documentation
- Enter Task Status: in progress
- Enter Task Time: 90
- Task 04 created successfully !!

### 📋 List Tasks
Task List:
-  01 -Requirements gathering, pending, 60,
- 02 -Schedule medical appointments, pending, 180,
- 03 -CRUD Customers, pending, 50, 
- 04 -Review documentation, in progress, 90

### ✏️ Update Task
->Update Task
- Enter Task ID:04
(Do not enter anything to keep it the same) - Enter new Task Description: 
- Enter new Task Status: completed
- Enter new Task Time: 120
- Task 04 updated successfully !!

### ❌  Delete Task
- Enter the ID of the task you want to delete: 04
Task deleted successfully

### 🤝 Contribuciones
Contributions are welcome. Feel free to fork the repository, make improvements, and submit a pull request.



