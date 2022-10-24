def ensure_integer(x):
    try:
        x_as_int = int(x)
        return x_as_int
    except ValueError:
        return None
        