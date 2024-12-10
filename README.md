
# Professor Sentiment & Review Analyzer

## Overview

The **Professor Sentiment & Review Analyzer** is a Python application designed to retrieve and analyze professor reviews from RateMyProfessor.com. By integrating Google Generative AI, the tool provides detailed summaries and sentiment analysis of professor reviews based on user-defined qualities (e.g., Clarity, Helpfulness, Engagement). This project aims to help students make informed decisions about professors by highlighting key strengths and weaknesses.

---

## Features

1. **Review Retrieval**:
   - Fetches reviews for a specific professor from RateMyProfessor.com.
   
2. **Summarization**:
   - Generates concise summaries of reviews with bullet points based on user-selected qualities.

3. **Sentiment Analysis**:
   - Classifies reviews as Positive, Neutral, or Negative with reasoning for each classification.

4. **User-Friendly GUI**:
   - Built with Tkinter for easy interaction.

5. **Real-time Processing**:
   - Ensures a responsive user experience by running heavy tasks in a background thread.

---

## Requirements

### Software Requirements
- Python 3.8 or above

### Python Libraries
Install the required Python libraries using the following command:
```bash
pip install ratemyprofessor google-generativeai
```

### Google Generative AI
1. Obtain an API key for Google Generative AI.
2. Replace the placeholder in the script with your API key:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/professor-analyzer.git
   cd professor-analyzer
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

---

## Usage

1. **Launch the Application**:
   Run the script to open the GUI.

2. **Input Details**:
   - Enter the **University Name** and **Professor Name**.
   - Specify up to three desired qualities (e.g., Clarity, Helpfulness).

3. **Analyze Reviews**:
   - Click the **Analyze Sentiment** button.
   - The app will process the reviews and display:
     - Professor rating and difficulty.
     - Summarized review insights.
     - Sentiment analysis for each review.

---

## Example Workflow

1. Launch the app.
2. Input:
   - University Name: `University of Example`
   - Professor Name: `Dr. John Doe`
   - Desired Qualities: `Clarity`, `Helpfulness`, `Engagement`
3. Click **Analyze Sentiment**.
4. View the results in the provided text box.

---

## Troubleshooting

### Common Issues
- **Professor Not Found**: Ensure the professor and university names are correct.
- **API Errors**: Verify that your Google Generative AI API key is valid.
- **Dependencies**: Double-check that all required libraries are installed.

### Debugging
If you encounter errors, try running the script in a terminal to view detailed logs.

---

## Limitations

1. **Data Availability**:
   - Limited reviews for less popular professors may affect reliability.
   
2. **Real-time Data Fetching**:
   - Network issues may slow down the review retrieval process.

---

## Future Enhancements

1. Support batch processing for multiple professors.
2. Save analysis results to a file (e.g., CSV or PDF).
3. Provide more detailed trend analysis of reviews over time.
4. Add support for alternate review platforms.

---

## Contributors

- **Hamza**: AI integration and prompt engineering.
- **Antwan**: GUI design and API integration.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
