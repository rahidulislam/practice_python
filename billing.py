def calculate_tax(price,tax):
    return price * tax

def print_billing_doc():
    tax_rate = 0.1
    products =[{'name':'apple','price':100},{'name':'banana','price':50}]
    # print billing header
    print(f"Name\tPrice\tTax")

    # print the billing details
    for product in products:
        tax = calculate_tax(product['price'],tax_rate)
        print(f"{product['name']}\t{product['price']}\t{tax}")

print(__name__)
if __name__ == '__main__':
    print_billing_doc()