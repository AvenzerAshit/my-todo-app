import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+'\n')
    function.write_todos(todos)

st.title("My Todo App")

for index,todo in enumerate(todos):
    checkbox= st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add todo", on_change= add_todo, key= 'new_todo')
