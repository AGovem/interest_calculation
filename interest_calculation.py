def interest_calc(main_money,interest_rate,maturity_year=None,maturity_month=None):
    f_money = main_money*(1+interest_rate/100)**(maturity_year or maturity_month)
    print(f_money)
interest_calc(100,5,1)