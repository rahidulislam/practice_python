# import priceing
# import priceing as selling_price
# from priceing import get_net_price
from priceing import get_net_price as calculate_net_price
from priceing import get_tax

# net_price = selling_price.get_net_price(price=100,tax_rate=0.01)
# net_price = get_net_price(price=100,tax_rate=0.01)
net_price = calculate_net_price(price=100,tax_rate=0.01)
print(net_price)
tax = get_tax(100,0.01)
print(tax)