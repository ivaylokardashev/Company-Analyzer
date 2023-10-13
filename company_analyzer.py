def gross_profit_margin(balance_sheet):
    return balance_sheet.get("gross_profit") / balance_sheet.get("total_revenue") * 100


def debt_to_equity_ratio(balance_sheet):
    return balance_sheet.get("total_liabillities") / balance_sheet.get("stock_equity")


'''Example'''
balance_sheet = {"gross_profit": 104956000, "total_revenue": 274515000, "net_income": 57411000,
                 "stock_equity": 201442000, "total_liabillities": 74467231, "total_assets": 96334, "inventar": 20497,
                 "current_liabilities": 87812}


