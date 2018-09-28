# -*- coding: utf-8 -*-
def leap_year_finder(year: int) -> bool:
    """Return True if input integer year is leap year."""
    if year % 4 == 0 and (year % 100 != 0 or year % 400) == 0:
        return True
    else:
        return False


def main() -> str:
    """Run leap year finder."""
    try:
        input_year = int(input("What year: ").strip().lower())
        is_leap_year = leap_year_finder(input_year)
        if is_leap_year:
            return "{} is a leap year.".format(input_year)
        return "{} is not a leap year.".format(input_year)
    except ValueError as e:
        print("Check your input, should be integer: {}".format(e))


if __name__ == "__main__":
    print(main())
