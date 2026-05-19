def greet(name):
    """Return a greeting string.

    Args:
        name (str): The name to greet. Can be empty or None.

    Returns:
        str: A personalized greeting, or "Hello, stranger!" if name is empty.
    """
    if not name or name.strip() == "":
        return "Hello, stranger!"
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print(greet(""))
