# -*- coding: utf-8 -*-
import pandas as pd


def main():
    """Run loan calculator."""
    print("Loan Calculator")
    borrowed = float(input("Amount borrowed: "))
    interest_rate = float(input("Interest rate: "))
    term_in_years = int(input("Term (years): "))

    borrowed_cents = borrowed * 100
    interest_paid = ((interest_rate) * term_in_years)
    remaining_balance = borrowed + interest_paid
    rows = term_in_years * 12

    payment_numbers = [row for row in range(term_in_years * 12)]
    individual_payments = [remaining_balance / rows for row in range(
    term_in_years * 12)]
    individual_payments[0] = 0
    remaining_balances = [remaining_balance - (
    remaining_balance / rows) * row for row in payment_numbers]

    print("Amount borrowed:\t{}\nTotal interest paid:\t{}".format(
    borrowed, interest_paid
    ))

    schedule_data = {
    "pymt#": payment_numbers,
    "Amount Paid": individual_payments,
    "Remaining Balance": remaining_balances
    }

    schedule = pd.DataFrame(schedule_data)
    schedule.style.format({"Amount Paid": })
    print(schedule)


if __name__ == '__main__':
    main()
