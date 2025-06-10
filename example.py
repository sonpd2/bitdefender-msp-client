from bitdefender_msp import BitdefenderMSPClient

# Initialize the client
api_key = "52636a13-bdc2-4936-9488-9931ed49c8b5"
client = BitdefenderMSPClient(api_key=api_key)

# Create a new subscriber
try:
    new_subscriber = client.create_subscriber(email="test@example.com")
    subscriber_id = new_subscriber["subscriber_id"]
    print(f"Created subscriber with ID: {subscriber_id}")
    print(f"Enrollment URL: {new_subscriber.get('enrol_url')}")
    
    # Add a subscription to the subscriber
    subscription = client.add_subscription(
        subscriber_id=subscriber_id,
        product_id="your_product_id",  # Replace with an actual product ID
        trial=True
    )
    subscription_id = subscription["subscription_id"]
    print(f"Added subscription with ID: {subscription_id}")
    
    # Get subscriber details
    subscriber = client.get_subscriber(subscriber_id)
    print(f"Subscriber details: {subscriber}")
    
    # List all subscriptions for the subscriber
    subscriptions = client.list_subscriptions(subscriber_id)
    print(f"Subscriptions: {subscriptions}")
    
    # Suspend all subscriptions
    client.suspend_subscriptions(subscriber_id, suspended=True)
    print("Subscriptions suspended")
    
    # Resume all subscriptions
    client.suspend_subscriptions(subscriber_id, suspended=False)
    print("Subscriptions resumed")
    
except Exception as e:
    print(f"Error: {e}")