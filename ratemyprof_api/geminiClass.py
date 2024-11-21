import google.generativeai as genai
import os
import ratemyprof_api

genai.configure(api_key="AIzaSyAhScXimIELR9bq7evzWGUlNZzmRhOsWXc") 

model = genai.GenerativeModel("gemini-1.5-flash")


Prompt = '''I am a student at the University of Cincinnati. I am looking for a professor who is knowledgeable,
 engaging, and approachable. I want to take a class with a professor who is passionate about their subject and cares about 
 their students. I came across this professor, give me the sentiment about this professor, here are the rate my prfessor 
 reviews:''' + 

response = model.generate_content(Prompt)
print(response.text)