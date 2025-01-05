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
        {"guest_id": 3, "name": "Sam Lee", "feedback": "The food was okay, but it could be better."}
    ]

def analyze_sentiment(feedback):
    """
    Simulate sentiment analysis for the feedback.
    In practice, replace this with actual API call logic.
    """
    positive_keywords = ["amazing", "good", "come back", "great"]
    negative_keywords = ["dirty", "unhelpful", "could be better"]
    
    if any(word in feedback.lower() for word in positive_keywords):
        return "Positive"
    elif any(word in feedback.lower() for word in negative_keywords):
        return "Negative"
    else:
        return "Neutral"
def process_feedback(crm_data):
    """
    Process the feedback from CRM data and analyze sentiments.
    """
    results = []
    for record in crm_data:
        sentiment = analyze_sentiment(record["feedback"])
        results.append({
            "Guest ID": record["guest_id"],
            "Name": record["name"],
            "Feedback": record["feedback"],
            "Sentiment Analysis": sentiment
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

    print("Step 2: Processing feedback for sentiment analysis...")
    analyzed_data = process_feedback(crm_data)

    print("Step 3: Saving results to CSV...")
    save_to_csv(analyzed_data)

    print("Process complete!")
