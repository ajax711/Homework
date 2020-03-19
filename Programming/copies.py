rate = 289.50 
discount = 0.4
discount_rate = rate - (rate*0.4)
total_copies = 60 
shipping = 100 + 25*(total_copies-1)
total_price = ((discount_rate*total_copies)+shipping)
print total_price
