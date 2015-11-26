def check_valid_year(year):
    if year > 1895 and year < 2021:
        return True
    else:
        return False

def check_color_yes_no(color):
    if color.lower() == "yes" or color.lower() == "no":
        return True
    else:
        return False