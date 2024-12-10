import ratemyprofessor
import google.generativeai as genai
from tkinter import Tk, Label, Entry, Button, Text, END, messagebox
import threading

# Configure Google AI model
genai.configure(api_key="AIzaSyAhScXimIELR9bq7evzWGUlNZzmRhOsWXc")
model = genai.GenerativeModel("gemini-1.5-flash")

# Define function for summarizing comments with advanced prompt engineering
def summarize_comments(reviews_text, qualities):
    prompt = f'''As a diligent student who highly values qualities like {qualities}, 
    analyze the professor reviews and generate a short concise summary with key insights. 
    Create bullet points highlighting the professor’s strengths and weaknesses based on the reviews, 
    and provide a percentage match for each quality mentioned.
    Reviews:
    {reviews_text}'''
    response = model.generate_content(prompt)
    return response.text

# Define function for sentiment classification with more detailed output
def classify_sentiment(reviews_text):
    prompt = '''For each of the following reviews, classify the sentiment as one of the following:
    "Positive," "Neutral," or "Negative." Also, provide a brief reasoning for each classification:
    Review:'''
    response = model.generate_content(prompt + reviews_text)
    return response.text

# Define the function to process professor reviews
def process_professor_reviews(professor_name, school_name, quality_1, quality_2, quality_3):
    try:
        professor = ratemyprofessor.get_professor_by_school_and_name(
            ratemyprofessor.get_school_by_name(school_name), professor_name
        )
        if professor is not None:
            reviews_text = ""
            reviews = professor.get_ratings()
            if len(reviews) < 6:
                reliability_warning = "\nNote: Limited reviews, results may not be fully representative."
            else:
                reliability_warning = ""
            for review in reviews:
                reviews_text += review.comment + "\n"

            # Combine all qualities into a single string for the prompt
            qualities = f"{quality_1}, {quality_2}, {quality_3}"

            # Summarize the reviews
            summary = summarize_comments(reviews_text, qualities)

            # Sentiment analysis
            sentiment_results = classify_sentiment(reviews_text)

            # Display professor details
            details = (
                f"Rating: {professor.rating} / 5.0\n"
                f"Difficulty: {professor.difficulty} / 5.0\n"
                f"Total Ratings: {professor.num_ratings} {reliability_warning}\n"
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

# Function to call the review processing in a separate thread to avoid UI freezing
def generate_response_threaded():
    university = university_entry.get()
    professor = professor_entry.get()
    quality_1 = quality_1_entry.get()
    quality_2 = quality_2_entry.get()
    quality_3 = quality_3_entry.get()

    if university and professor:
        progress_label.config(text="Processing reviews... Please wait.")
        threading.Thread(target=generate_response, args=(university, professor, quality_1, quality_2, quality_3)).start()
    else:
        messagebox.showerror("Input Error", "Please provide both university and professor names.")

# Generate response function to update the GUI
def generate_response(university, professor, quality_1, quality_2, quality_3):
    response = process_professor_reviews(professor, university, quality_1, quality_2, quality_3)
    response_text.delete("1.0", END)
    response_text.insert(END, response)
    progress_label.config(text="Analysis Complete.")

# Create main window
root = Tk()
root.title("Professor Sentiment & Review Analyzer")
root.geometry("700x700")

# University Name Label and Entry
university_label = Label(root, text="University Name:")
university_label.pack(pady=5)
university_entry = Entry(root, width=60)
university_entry.pack(pady=5)

# Professor Name Label and Entry
professor_label = Label(root, text="Professor Name:")
professor_label.pack(pady=5)
professor_entry = Entry(root, width=60)
professor_entry.pack(pady=5)

# Desired Quality 1 Label and Entry
quality_1_label = Label(root, text="Desired Quality 1 (e.g., Clarity):")
quality_1_label.pack(pady=5)
quality_1_entry = Entry(root, width=60)
quality_1_entry.pack(pady=5)

# Desired Quality 2 Label and Entry
quality_2_label = Label(root, text="Desired Quality 2 (e.g., Helpfulness):")
quality_2_label.pack(pady=5)
quality_2_entry = Entry(root, width=60)
quality_2_entry.pack(pady=5)

# Desired Quality 3 Label and Entry
quality_3_label = Label(root, text="Desired Quality 3 (e.g., Engagement):")
quality_3_label.pack(pady=5)
quality_3_entry = Entry(root, width=60)
quality_3_entry.pack(pady=5)

# Generate Response Button
generate_button = Button(root, text="Analyze Sentiment", command=generate_response_threaded)
generate_button.pack(pady=15)

# Progress Label
progress_label = Label(root, text="")
progress_label.pack(pady=5)

# AI Response Text Box
response_label = Label(root, text="Analysis Result:")
response_label.pack(pady=5)
response_text = Text(root, height=150, width=300)
response_text.pack(pady=5)

# Run the main event loop
root.mainloop()
