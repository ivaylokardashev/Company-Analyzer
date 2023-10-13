from math import ceil

def gross_profit_margin(balance_sheet):
    return balance_sheet.get("gross_profit") / balance_sheet.get("total_revenue") * 100


def net_profit_margin(balance_sheet):
    return balance_sheet.get("net_income") / balance_sheet.get("total_revenue") * 100


def debt_to_equity_ratio(balance_sheet):
    return balance_sheet.get("total_liabillities") / balance_sheet.get("stock_equity")


def current_ratio(balance_sheet):
    return balance_sheet.get("total_assets") / balance_sheet.get("current_liabilities")


def quick_ratio(balance_sheet):
    return (balance_sheet.get("total_assets") - balance_sheet.get("inventar")) / balance_sheet.get("current_liabilities")


def sign_for_companies_finance_health(balance_sheet):
    if 0.5 < debt_to_equity_ratio(balance_sheet) < 1 or \
            debt_to_equity_ratio(balance_sheet) < 0.5:
        return "The company is in good finance state."
    else:
        return "The company isn't in good finance state."


def price_to_average_earn(earnings_for_last_seven_years):
    UPPER_LIMIT = 25
    total_earnings_for_last_seven_years = sum(earnings_for_last_seven_years)
    price_for_average_earnings_per_share = total_earnings_for_last_seven_years / 7
    real_price_of_share = ceil(price_for_average_earnings_per_share * UPPER_LIMIT * 100) / 100

    return real_price_of_share


'''Example'''
balance_sheet = {"gross_profit": 104956000, "total_revenue": 274515000, "net_income": 57411000,
                 "stock_equity": 201442000, "total_liabillities": 74467231, "total_assets": 96334, "inventar": 20497,
                 "current_liabilities": 87812}

print(sign_for_companies_finance_health(balance_sheet))
print(f"{quick_ratio(balance_sheet):.2f}")
print(f"{current_ratio(balance_sheet):.3f}")

earnings_for_last_seven_years = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 3]

print(price_to_average_earn(earnings_for_last_seven_years))

