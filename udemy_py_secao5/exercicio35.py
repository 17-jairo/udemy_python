def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def is_valid_date(year, month, day):
    if month < 1 or month > 12:
        return False

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[2] = 29

    if day < 1 or day > days_in_month[month]:
        return False

    return True


def main():
    year = int(input("Digite o ano: "))
    month = int(input("Digite o mês: "))
    day = int(input("Digite o dia: "))

    if is_valid_date(year, month, day):
        print("A data é válida.")
    else:
        print("A data é inválida.")


if __name__ == "__main__":
    main()
