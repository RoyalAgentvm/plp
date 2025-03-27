price = float(input('input the original price: '))
discount_percent = float(input('input the discount percent: '))

def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount=price*discount_percent/100
        new_price=price-discount
        return new_price
    else:
        return price
    
print(calculate_discount(price,discount_percent))
