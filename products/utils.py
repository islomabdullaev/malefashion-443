def get_price_range(price_range):
    if price_range:
        price_range = price_range.split(";")
        from_price, to_price = price_range[0], price_range[1]
        return from_price, to_price
    else:
        return None