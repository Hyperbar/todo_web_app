# Import necessary libraries
import streamlit as st
import functions

# Get the list of todos from the functions module
todos = functions.get_todos()

# Define a function to add a new todo
def add_todo():
    # Get the new todo from the session state and add a newline
    todo = st.session_state["new_todo"] + "\n"
    # Append the new todo to the list
    todos.append(todo)
    # Write the updated list of todos
    functions.write_todos(todos)

# Set the title of the Streamlit app
st.title("Planify")
# Set the subheader
st.subheader("Stop wasting, start planning!")

# Iterate through the list of todos
for index, todo in enumerate(todos):
    # Create a checkbox for each todo
    checkbox = st.checkbox(todo, key=todo)
    # If the checkbox is checked
    if checkbox:
        # Remove the todo from the list
        todos.pop(index)
        # Write the updated list of todos
        functions.write_todos(todos)
        # Remove the todo from the session state
        del st.session_state[todo]
        # Rerun the app to update the UI
        st.rerun()

# Create a text input for adding new todos
st.text_input(
    label="todo input",
    label_visibility="hidden",
    placeholder="Add new todo...",
    on_change=add_todo,
    key='new_todo'
)