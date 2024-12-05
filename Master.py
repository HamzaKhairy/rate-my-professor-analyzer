import ratemyprofessor
import google.generativeai as genai
import json
from collections import defaultdict

# Configure Google AI model
genai.configure(api_key="AIzaSyAhScXimIELR9bq7evzWGUlNZzmRhOsWXc") 
model = genai.GenerativeModel("gemini-1.5-flash")

# Define function for summarizing comments
def summarize_comments(reviews_text):
    prompt = '''Summarize the key insights from the following reviews of a professor in three bullet points. 
    Provide a concise list of points that reflect the overall sentiment:'''
    response = model.generate_content(prompt + reviews_text)
    return response.text

# Define function for sentiment classification
def classify_sentiment(reviews_text):
    prompt = '''Classify the sentiment of each of the following comments as Positive, Neutral, or Negative:
    Review:'''
    response = model.generate_content(prompt + reviews_text)
    return response.text

# Define function to suggest professors based on feedback and preferences
def suggest_professors(preferences):
    # Sample preference-based suggestions algorithm
    professors = ratemyprofessor.get_professors_by_school_and_preference(preferences['school'])
    recommendations = []
    for professor in professors:
        aggregated_feedback = aggregate_feedback(professor)
        if matches_preferences(aggregated_feedback, preferences):
            recommendations.append(professor)
    return recommendations

# Define function to aggregate feedback
def aggregate_feedback(professor):
    reviews = professor.get_ratings()
    sentiment_scores = defaultdict(int)
    for review in reviews:
        sentiment = classify_sentiment(review.comment)  # Classify sentiment of the comment
        sentiment_scores[sentiment] += 1
    return sentiment_scores

# Define function to check if professor matches preferences
def matches_preferences(aggregated_feedback, preferences):
    # Check if the professor matches the user's preferences based on aggregated feedback
    # For example: does the sentiment align with "Positive" preference?
    if aggregated_feedback["Positive"] > preferences['min_positive_reviews']:
        return True
    return False

# Define the function to handle the collection and summarization of reviews
def process_professor_reviews(professor_name, school_name):
    professor = ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name(school_name), professor_name)
    
    if professor is not None:
        reviews_text = ""
        reviews = professor.get_ratings()

        for review in reviews:
            reviews_text += review.comment + "\n"

        # Summarize the reviews
        summary = summarize_comments(reviews_text)

        # Print key insights
        print("Professor Summary: ", summary)
        
        # Collect sentiment analysis of reviews
        sentiment_results = classify_sentiment(reviews_text)
        print("Sentiment Analysis: ", sentiment_results)

        # Professor Details
        print(f"{professor.name} works in the {professor.department} Department of {professor.school.name}")
        print(f"Rating: {professor.rating} / 5.0")
        print(f"Difficulty: {professor.difficulty} / 5.0")
        print(f"Total Ratings: {professor.num_ratings}")
        print(f"Would Take Again: {professor.would_take_again if professor.would_take_again is not None else 'N/A'}")
    else:
        print("Professor not found.")

# Sample preferences for professor recommendation
preferences = {
    'school': 'University of Cincinnati',
    'min_positive_reviews': 50,
    'max_difficulty': 3
}

# Example of using the new functionality
process_professor_reviews("Anca", "University of Cincinnati")
