from sales.order import create_sales_order
from sales.billing import create_billing
from sales.delivery import create_delivery
from sales import TAX_RATE

create_sales_order()
create_billing()
create_delivery()
print(TAX_RATE)

# from sales import *
# order.create_sales_order()
# billing.create_billing()
# delivery.create_delivery()

from mail_private_function.email import *
send("b9K2l@example.com","hello")
attach_file("file.txt")
# _attach_file("file.txt")

