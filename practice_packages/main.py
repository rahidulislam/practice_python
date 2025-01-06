from sales.order import create_sales_order
from sales.billing import create_billing
from sales.delivery import create_delivery
from sales import TAX_RATE
# from sales import *
create_sales_order()
create_billing()
create_delivery()
print(TAX_RATE)
# order.create_sales_order()
# billing.create_billing()
# delivery.create_delivery()
