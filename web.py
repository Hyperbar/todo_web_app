import streamlit as st
import functions


# Define the function to add a new todo
def add_todo():
    # Get the new todo from the session state, capitalize, and add a period
    todo = st.session_state["new_todo"].capitalize().strip() + ".\n"
    # Append the new todo to the list
    todos.append(todo)
    # Write the updated list of todos
    functions.write_todos(todos)
    # Clear the input by resetting the session state
    st.session_state["new_todo"] = ""


# Get the list of todos from the functions module
todos = functions.get_todos()

# Set the title of the Streamlit app
st.title("Planify")
# Set the subheader
st.subheader("Stop wasting, start planning!")

# Iterate through the list of todos
for index, todo in enumerate(todos, start=1):
    # Capitalize the first letter, remove trailing newline, and format with number
    formatted_todo = f"{index}. {todo.strip().capitalize()}"  # Ensure only one period

    # Create a checkbox for each todo
    checkbox = st.checkbox(formatted_todo, key=todo)

    # If the checkbox is checked
    if checkbox:
        # Remove the todo from the list
        todos.pop(index - 1)  # Adjust index because enumeration starts at 1
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
    key='new_todo',
    value=st.session_state.get("new_todo", "")  # Use the session state value
)