class Date:
    @staticmethod
    def validate_date(day, month, year):
        if 0 <= day <= 31:
            if 1 <= month <= 12:
                if year >= 0:
                    print(f"дата {day}-{month}-{year} валидна")
                else:
                    print(f"дата {day}-{month}-{year} невалидна.")
            else:
                print(f"дата {day}-{month}-{year} невалидна.")
        else:
            print(f"дата {day}-{month}-{year} невалидна.")

    @classmethod
    def date_to_number(cls, date):
        day, month, year = date.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        return day, month, year

    def __init__(self, date):
        self.date_str = date
        Date.validate_date(*Date.date_to_number(self.date_str))


a = Date("21-03-343")
