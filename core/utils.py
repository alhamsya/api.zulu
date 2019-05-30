def validate_int(param) -> bool:
    try:
        val = int(param)
        if val < 1:
            return False
        return True
    except ValueError:
        return False

def validate_int_between(param, smallest, biggest) -> bool:
    try:
        if int(smallest) <= int(param) <= int(biggest):
            return True
        return False
    except ValueError:
        return False