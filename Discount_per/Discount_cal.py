def get_per(price,discount):
    discount = price - ((price*discount)/100)
    return discount


dis=get_per(500,50)
print("50% discount for price 500",dis)