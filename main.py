def greet(name):
    if not name or name.strip() == "":
        return "Hello, stranger!"
    return f"Hello, {name}!"
