#Simple web task manager
import os
from flask import Flask , render_template , request , url_for , redirect , flash , session
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

app.secret_key = "secret"

@app.route("/")
def index():
  todos = session.get("todos",[])
  print("=== FLASK DEBUG ===")
  print("Current working directory:", os.getcwd())
  print("app.root_path:", app.root_path)
  print("Template folder:", app.template_folder)
  print("Full path to todos.html:", os.path.join(app.template_folder, "todos.html"))
  print("File exists?", os.path.exists(os.path.join(app.template_folder, "todos.html")))
  print("Files in templates:", os.listdir(app.template_folder) if os.path.exists(app.template_folder) else "Folder missing")
  print("===================")
  return render_template("todos.html", todos=todos)

@app.route("/add", methods = ["POST"])
def add_todo():
  todo_text = request.form.get("todo" , "").strip()
  if not todo_text:
    flash("To do cannot be empty.","error")
    return redirect(url_for("index"))
  todos = session.get("todos",[])
  new_todo = {"id":len(todos),"text":todo_text,"done":False}
  todos.append(new_todo)
  session["todos"] = todos
  flash("Add todo lists successfully!","success")
  return redirect(url_for("index"))

@app.route("/delete/<todo_id>")
def delete_todo(todo_id):
  todos = session.get("todos",[])
  todos = [todo for todo in todos if todo["id"] != todo_id]
  session["todos"] = todos
  flash("Delete todo list successfully.","success")
  return redirect(url_for("index"))

@app.route("/toggle/<todo_id>")
def toggle_todo(todo_id):
  todos = session.get("todos",[])
  for todo in todos:
    if todo["id"] == todo_id:
      todo["done"] = not todo["done"]
      break
  session["todos"] = todos
  return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(debug=True)