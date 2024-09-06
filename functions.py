# Define the default file path for the todos file
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of to-do items.

    :param filepath: Path to the file containing todo items (default is FILEPATH)
    :return: A list of todo items
    """
    # Open the file in read mode using a context manager
    with open(filepath, "r") as file_local:
        # Read all lines from the file into a list
        todos_local = file_local.readlines()
    # Return the list of todos
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list to the text file.

    :param todos_arg: List of todo items to write
    :param filepath: Path to the file to write to (default is FILEPATH)
    :return: None
    """
    # Open the file in write mode using a context manager
    with open(filepath, "w") as file:
        # Write the list of todos to the file
        file.writelines(todos_arg)
    # No return statement needed as this function modifies the file directly


# This block only runs if the script is executed directly (not imported)
if __name__ == "__main__":
    print("Hello")
    # Print the list of todos when the script is run directly
    print(get_todos())