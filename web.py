import streamlit as st
from modules import functions


todos = functions.get_todos()
st.title("Todo App")
st.subheader("This is your todo app.")
st.write("The app increase your productivity.")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)

st.text_input(label="Enter a todo:", placeholder="Todo...")
