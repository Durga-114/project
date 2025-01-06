import os
import pandas as pd
from datetime import datetime


API_KEY = os.getenv("TOGATHER_API_KEY") or "1be60ea7db96823b0ea0745a9b6402c0091ac15be3912fcaf760179b826f21d9"

if not API_KEY:
    raise ValueError("API key not found! Set the 'TOGATHER_API_KEY' environment variable.")


def load_mock_crm_data():
    """
    Simulate CRM data with guest profiles and feedback.
    """
    return [
        {"guest_id": 1, "name": "John Doe", "feedback": "The service was amazing! I'll come back for sure."},
        {"guest_id": 2, "name": "Jane Smith", "feedback": "The room was dirty and the staff was unhelpful."},
        {"guest_id": 3, "name": "Sam Lee", "feedback": "The food was okay, but it could be better."},
        {"guest_id": 4, "name": "Tom Harris", "feedback": "The check-in was delayed, and the room was too hot."}
    ]

def analyze_sentiment(feedback):
    """
    Simulate sentiment analysis for the feedback.
    """
    positive_keywords = ["amazing", "good", "come back", "great"]
    negative_keywords = ["dirty", "unhelpful", "could be better", "late", "broken", "poor"]
    
    sentiment_score = 0
    for word in negative_keywords:
        if word in feedback.lower():
            sentiment_score += 1

    # Sentiment classification based on the number of negative keywords found
    if sentiment_score == 0:
        return "Positive"
    elif sentiment_score == 1:
        return "Neutral"
    else:
        return "Negative"

def detect_service_issues(feedback):
    """
    Detect specific service-related issues in the feedback.
    """
    issues = []
    service_issues_keywords = ["broken", "late", "dirty", "unhelpful", "too hot", "poor"]

    for issue in service_issues_keywords:
        if issue in feedback.lower():
            issues.append(issue)

    return issues

def send_alert(guest_name, feedback, issues):
    """
    Simulate an alert for service-related issues or negative feedback.
    In a real application, this could be an email, SMS, or notification.
    """
    print(f"ALERT: Service issues detected for {guest_name}: {feedback}")
    print(f"Identified issues: {', '.join(issues)}")

def process_feedback(crm_data):
    """
    Process the feedback from CRM data, analyze sentiments, and detect service issues.
    """
    results = []
    for record in crm_data:
        sentiment = analyze_sentiment(record["feedback"])
        issues = detect_service_issues(record["feedback"])

        # Trigger an alert if sentiment is negative or there are service-related issues
        if sentiment == "Negative" or len(issues) > 0:
            send_alert(record["name"], record["feedback"], issues)  # Send an alert for issues

        results.append({
            "Guest ID": record["guest_id"],
            "Name": record["name"],
            "Feedback": record["feedback"],
            "Sentiment Analysis": sentiment,
            "Service Issues": ", ".join(issues) if issues else "None"
        })
    return results

def save_to_csv(data):
    """
    Save processed data to a CSV file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"guest_feedback_analysis_{timestamp}.csv"
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    print("Step 1: Loading CRM data...")
    crm_data = load_mock_crm_data()

    print("Step 2: Processing feedback for sentiment analysis and service issues...")
    analyzed_data = process_feedback(crm_data)

    print("Step 3: Saving results to CSV...")
    save_to_csv(analyzed_data)

    print("Process complete!")
