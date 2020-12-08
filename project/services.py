from . import stripe


def create_customer(name=None):
    name = name if name else 'Stranger'
    customer = stripe.Customer.create(name=name)
    return customer
