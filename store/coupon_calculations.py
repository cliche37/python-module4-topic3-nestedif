def calculate_price(price, cash_coupon, percent_coupon):
    percent_coupon = percent_coupon / 100.00

    price_after_cash_coupon = price - cash_coupon
    price_after_percent_coupon = price_after_cash_coupon - (price_after_cash_coupon * percent_coupon)
    tax_amount = price_after_percent_coupon * 0.06

    if price_after_percent_coupon > 10.00:
        if price_after_percent_coupon > 30.00:
            if price_after_percent_coupon > 50.00:
                shipping = 0.00
            else:
                shipping = 11.95
        else:
            shipping = 7.95
    else:
        shipping = 5.95

    return round((price_after_percent_coupon + tax_amount + shipping), 2)
