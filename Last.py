from slack_sdk.webhook import WebhookClient

# Slack Webhook URL
slack_webhook_url = "https://hooks.slack.com/services/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"

def send_slack_notification(review, sentiment, next_steps, area_responsible):
    """
    Sends a notification to Slack using the Slack WebhookClient.
    """
    # Format the message
    alert_message = (
        f"⚠️ *Attention Required: Guest Feedback Alert* \n"
        f"*Review:* {review}\n"
        f"*Sentiment:* {sentiment}\n"
        f"*Next Steps:* {next_steps}\n"
        f"*Area Responsible:* {area_responsible}\n"
    )
    
    # Send the message via Slack webhook
    webhook = WebhookClient(slack_webhook_url)
    response = webhook.send(text=alert_message)
    
    if response.status_code == 200 and response.body == "ok":
        print("Slack notification sent successfully!")
    else:
        print(f"Failed to send Slack notification. Response: {response.body}")

# Example Usage
if __name__ == "__main__":
    # Example input details for a Dining Services issue
    review = "The food served at the buffet was cold and lacked flavor."
    sentiment = "Negative sentiment detected."
    next_steps = (
        "Ensure proper heating of dishes before serving and conduct a review of the menu "
        "to enhance the quality and flavor of the dishes with the culinary team."
    )
    area_responsible = (
        "Dining Services: Kitchen Staff and Buffet Management Team are responsible for addressing this issue. "
        "Kitchen Staff should improve food preparation standards, and the Buffet Management Team should ensure proper food quality checks."
    )
    
    # Send the notification
    send_slack_notification(review, sentiment, next_steps, area_responsible)
