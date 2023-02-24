import datetime


class Pricing:
    def calculate_price(rented_date, return_date):
        # print(rented_date, return_date, type(rented_date), type(return_date))
        calculate_days = (return_date.date() -
                          rented_date.date()).days
        # print('calculate_days:', calculate_days)
        if calculate_days <= 7:
            fine = 5
        else:
            fine = 5 + (calculate_days - 7) * 10
        return fine
