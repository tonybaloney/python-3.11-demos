from multiprocessing.sharedctypes import Value


def process_order(order):
    if len(order) > 2: 
        raise ValueError("Too many items in order")
    elif len(order) < 2:
        raise ValueError("Not enough items in order")

orders = [
    ["eggs", "spam"],
    ["ham"],
    ["spinach", "ricotta", "salad"],
    ["cola", "rice"]
]

def process_orders(orders):
    errors = []
    for order in orders:
        try:
            process_order(order)
        except Exception as ex:
            ex.add_note(", ".join(order))
            errors.append(ex)

    if errors:
        raise ExceptionGroup("Order issues", errors)


try:
    process_orders(orders)
except* ValueError as ve:
    print("Invalid orders")
    for e in ve.exceptions:
        print(" - ", e.__notes__)
