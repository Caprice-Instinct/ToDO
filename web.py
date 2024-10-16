import streamlit as st
from modules import functions


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    if todo_local not in todos:
        todos.append(todo_local)
        functions.write_todos(todos)
        st.session_state['new_todo'] = ''


todos = functions.get_todos()
st.title("Todo App")
st.subheader("This is your todo app.")
st.write("The app increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Todo...",
              on_change=add_todo, key='new_todo')


st.session_state