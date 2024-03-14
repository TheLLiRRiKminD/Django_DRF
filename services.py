import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


def stripe_product_create(course):
    product = stripe.Product.create(name=f"{course}")
    # print(product)
    return product


# stripe_product_create('Python')
# stripe.Product.delete("prod_Pjhxn1O4eySlo3")


def stripe_price_create(product, price):
    price_of_course = stripe.Price.create(
        currency="rub",
        unit_amount=price,
        recurring={"interval": "month"},
        product_data={"name": f"{product}"},
    )
    # print(price_of_course['id'])
    return price_of_course


def stripe_session_create(price):
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": f"{price}", "quantity": 1}],
        mode="subscription",
    )
    # print(session['url'])
    return session['url']
# stripe_price_create('Python', 500)
