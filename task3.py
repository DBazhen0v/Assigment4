def process_prices(prices, discount_percent):
    result = []
    for price in prices:
        if price >0:
            new_price= price-(price*discount_percent/100)
            new_price= round(new_price)
            result.append(new_price)
    return result

old_prices = [1000, -50,300, 0, 500]

print(process_prices(old_prices,20))