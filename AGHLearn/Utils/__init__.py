def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_positive_int(value):
    try:
        integer = int(value)
        return  integer >0
    except ValueError:
        return  False