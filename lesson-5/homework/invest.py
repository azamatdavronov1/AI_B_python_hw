def invest(amount, rate, years):
    i = 1
    while i <= years:
        part = amount * rate
        amount = amount + part
        if i < 10:
            print(f"year 0{i}:  ${amount:.2f}")
        else:
            print(f"year {i}:  ${amount:.2f}")
        i += 1



invest(100, 0.1, 12)