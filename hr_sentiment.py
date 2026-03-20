from groq import Groq
import pandas as pd
import time
import os

# ─── API SETUP ───────────────────────────────────────────
# Option 1: .env file se (recommended)
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

# Option 2: Seedha environment variable set karo
# Windows: set GROQ_API_KEY=gsk_xxxx
# Mac/Linux: export GROQ_API_KEY=gsk_xxxx

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ─── EMPLOYEE FEEDBACKS ──────────────────────────────────
feedbacks = [
    "I love working here, great team and good salary!",
    "Too much overtime, feeling burned out and stressed.",
    "Management is supportive and growth opportunities are good.",
    "Salary is very low compared to market, thinking of leaving.",
    "Work life balance is terrible, no time for family.",
    "Amazing company culture, I feel valued here.",
    "No promotion in 3 years, very disappointed.",
    "Great learning environment, happy with my job!"
]

print("Analyzing Employee Sentiments...\n")

results = []
for i, feedback in enumerate(feedbacks):
    prompt = f"""You are a sentiment analyzer. 
Analyze this employee feedback and reply with ONLY one word: Positive, Negative, or Neutral.
Do not write anything else.

Feedback: {feedback}"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5
    )
    
    sentiment = response.choices[0].message.content.strip().strip('.')
    results.append({'Feedback': feedback, 'Sentiment': sentiment})
    print(f"Feedback {i+1}: {sentiment}")
    print(f"   -> {feedback[:55]}...")
    time.sleep(1)

df = pd.DataFrame(results)
print("\nFinal Summary:")
print(df['Sentiment'].value_counts())