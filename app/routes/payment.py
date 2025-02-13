from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# ✅ Replace this with your real Stripe secret key
stripe.api_key = "sk_test_your_secret_key"

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    data = request.json
    asset = data.get("asset")
    package_name = data.get("packageName")

    # Define investment package prices in cents (Stripe uses cents)
    package_prices = {
        "Starter": 50000,  # $500
        "Pro": 200000,  # $2000
        "Basic": 10000,  # $100
        "Advanced": 100000,  # $1000
        "Gold Saver": 20000,  # $200
        "Gold Max": 150000,  # $1500
        "Investor": 30000,  # $300
        "Stock Expert": 250000,  # $2500
        "AI Beginner": 40000,  # $400
        "AI Master": 500000  # $5000
    }

    amount = package_prices.get(package_name, 0)
    if amount == 0:
        return jsonify({"error": "Invalid package"}), 400

    # ✅ Create Stripe Checkout Session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': f"{asset} - {package_name}"},
                'unit_amount': amount
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url="https://yourwebsite.com/success",
        cancel_url="https://yourwebsite.com/cancel"
    )

    return jsonify({"url": session.url})

if __name__ == '__main__':
    app.run(debug=True)
