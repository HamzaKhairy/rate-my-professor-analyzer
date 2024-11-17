import requests
from bs4 import BeautifulSoup
import openai

# Step 1: Get Input
university = input("Enter the university name: ")
professor = input("Enter the professor's name: ")

# Step 2: Scrape RateMyProfessors
def scrape_comments(university, professor):
    try:
        search_url = f"https://www.ratemyprofessors.com/search.jsp?query={professor} {university}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first result's URL (adjust selector based on RateMyProfessors structure)
        prof_url = soup.find('a', class_='TeacherCard__StyledTeacherCard').get('href')
        prof_page = requests.get(f"https://www.ratemyprofessors.com{prof_url}")
        prof_soup = BeautifulSoup(prof_page.text, 'html.parser')

        # Extract comments
        comments = [comment.text for comment in prof_soup.find_all('div', class_='Comments__StyledComment')]
        return comments
    except Exception as e:
        print(f"Error scraping data: {e}")
        return []

comments = scrape_comments(university, professor)

# Step 3: Use ChatGPT for Sentiment Analysis
def analyze_sentiment(comments):
    openai.api_key = "your_openai_api_key_here"  # Replace with your OpenAI API key
    prompt = f"Analyze the sentiment of the following comments about a professor and classify them as Positive, Neutral, or Negative:\n{comments}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

if comments:
    sentiment_results = analyze_sentiment(comments)
    print("Sentiment Analysis Results:")
    print(sentiment_results)
else:
    print("No comments found.")

# Optional: Visualize Results
# Use matplotlib or seaborn to create charts based on the results
