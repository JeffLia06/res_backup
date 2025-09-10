# lec 1
"""
    Interest calculation:
    Simple set up:
        Principal (P): the initial amount of money
        Interest rate (I): the duration for which the money is borrowed or invested
        Time (T): the duration for which the money is borrowed or invested

    Amount of interest charged (for time): P * I (per certain kind of time period)
    Effective rate of interest: P * I * 1t (for 1 unit of certain time period)
    Interest = I * T
    Total amount = I * T

    Simple Interest: (integer amount of time)
    Total Amount = P + I * T

    Compound Interest: (decimal amount of time)
    Total Amount = P * (1 + i)^(T/C)
    for example, for annual interest rate is 12%, we want to compute total amount in date of 180
    Total Amount = P * (1 + 0.12)^(180/365)

    Accumulation function/future value function:
    A(t): Total amount at time t
    Assume: A(0) = 1
    Amount earned at t is: A(t) - 1
    Amount  earned between t1 and t2 (t2 > t1): A(t2) - A(t1)
    FV = PV * (1 + r)^n
    FV: future value
    PV: present value
    r: interest rate per period
    n: number of period

    Present value:
    PV = FV/(1 + r)^m

    Net present value:
"""
