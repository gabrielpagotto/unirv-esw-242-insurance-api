def check_age(values: str, age: int) -> bool:
    # Checking greater or equal age values
    if values.endswith("+"):
        age_int = int(values.replace("+", ""))
        if age >= age_int:
            return True

    # Checking values ​​between two ages
    if values.__contains__("-"):
        start, end = values.split("-")
        if age >= int(start) and age <= int(end):
            return True

    return False


def check_driving_experience(values: str, driving_experience: int) -> bool:
    values = values.replace("y", "")

    # Checking greater or equal driving experience values
    if values.endswith("+"):
        de_int = int(values.replace("+", ""))
        if driving_experience >= de_int:
            return True

    # Checking values ​​between two driving experience values
    if values.__contains__("-"):
        start, end = values.split("-")
        if driving_experience >= int(start) and driving_experience <= int(end):
            return True

    return False


def check_vehicle_year(values: str, vehicle_year: int) -> bool:
    vehicle_year_compare = int(values.split(" ")[1])
    if values.startswith("before"):
        return vehicle_year <= vehicle_year_compare
    elif values.startswith("after"):
        return vehicle_year >= vehicle_year_compare
    return False
