import datetime


def current_date():
    """
    Get the current date and return it.
    :return: string
    """
    tday = str(datetime.datetime.now())
    elements = tday.split(" ")
    date_sections = elements[0]
    return date_sections

# Testing
# print(current_date())