from youcanpay import YouCanPay

def test_sdk():
    # Initialize the client with sandbox keys
    client = YouCanPay(
        private_key="pri_sandbox_your_key",  # Replace with your sandbox private key
        public_key="pub_sandbox_your_key",   # Replace with your sandbox public key
        sandbox=True
    )

    try:
        # Create a payment token
        token = client.create_payment_token(
            order_id="test_order_123",
            amount=1000,  # 10.00 MAD
            currency="MAD",
            customer_ip="127.0.0.1",
            success_url="https://yourdomain.com/success",
            error_url="https://yourdomain.com/error",
            customer_info={
                "name": "Test User",
                "email": "test@example.com",
                "phone": "+212600000000"
            }
        )
        print("Payment token created successfully:")
        print(f"Token ID: {token['id']}")
        print(f"Redirect URL: {token['redirect_url']}")

        # Get transaction details (replace with actual transaction ID)
        transaction_id = "your_transaction_id"
        transaction = client.get_transaction(transaction_id)
        print("\nTransaction details:")
        print(f"Status: {transaction['status']}")
        print(f"Amount: {transaction['amount']}")
        print(f"Currency: {transaction['currency']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_sdk() 