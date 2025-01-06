__all__ = ["send", "attach_file"]


def send(email, message):
    print(f"sending {message} to {email}")


def _attach_file(filename):
    print(f"attaching {filename}")


def attach_file(filename):
    _attach_file(filename)
