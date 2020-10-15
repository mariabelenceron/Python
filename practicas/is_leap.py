def is_leap(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False

def run():
    leap_year = int(input('Ingrese un año: '))
    if is_leap(leap_year):
        print('Año Bisciesto')
    else:
        print('Año no Bisciesto')

if __name__ == "__main__":
    run()
