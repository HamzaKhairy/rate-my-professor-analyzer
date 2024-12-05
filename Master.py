import ratemyprofessor
import google.generativeai as genai
from tkinter import Tk, Label, Entry, Button, Text, END

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


# Define the function to process professor reviews
def process_professor_reviews(professor_name, school_name):
    try:
        professor = ratemyprofessor.get_professor_by_school_and_name(
            ratemyprofessor.get_school_by_name(school_name), professor_name
        )
        if professor is not None:
            reviews_text = ""
            reviews = professor.get_ratings()
            for review in reviews:
                reviews_text += review.comment + "\n"

            # Summarize the reviews
            summary = summarize_comments(reviews_text)

            # Sentiment analysis
            sentiment_results = classify_sentiment(reviews_text)

            # Display professor details
            details = (
                f"Rating: {professor.rating} / 5.0\n"
                f"Difficulty: {professor.difficulty} / 5.0\n"
                f"Total Ratings: {professor.num_ratings}\n"
                "\nSummary of Reviews:\n"
                f"{summary}\n"
                "\nSentiment Analysis:\n"
                f"{sentiment_results}"
            )
            return details
        else:
            return "Professor not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


# GUI Implementation
def generate_response():
    university = university_entry.get()
    professor = professor_entry.get()

    if university and professor:
        response = process_professor_reviews(professor, university)
    else:
        response = "Please provide both university and professor names."

    # Display response in the text box
    response_text.delete("1.0", END)
    response_text.insert(END, response)


# Create main window
root = Tk()
root.title("Professor Sentiment Analysis")
root.geometry("600x500")

# University Name Label and Entry
university_label = Label(root, text="University Name:")
university_label.pack(pady=5)
university_entry = Entry(root, width=50)
university_entry.pack(pady=5)

# Professor Name Label and Entry
professor_label = Label(root, text="Professor Name:")
professor_label.pack(pady=5)
professor_entry = Entry(root, width=50)
professor_entry.pack(pady=5)

# Generate Response Button
generate_button = Button(root, text="Analyze Sentiment", command=generate_response)
generate_button.pack(pady=10)

# AI Response Text Box
response_label = Label(root, text="Analysis Result:")
response_label.pack(pady=5)
response_text = Text(root, height=150, width=300)
response_text.pack(pady=5)

# Run the main event loop
root.mainloop()