import os
import json
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Setup OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create /data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Format today's date for the file
today = datetime.now().strftime("%Y_%m_%d")
output_file = f"data/quotes_{today}.json"

# Prompt to generate 24 poetic quotes (1 for each hour)
prompt = """
You are a poetic spiritual assistant named 'el'. Generate 24 short, timeless quotes — one for each hour of the day — based on these 24 themes in this order:

Silence, Wonder, Discipline, Growth, Healing, Faith, Simplicity, Wisdom, Focus, Gratitude, Courage, Balance, Peace, Joy, Perseverance, Compassion, Presence, Clarity, Purpose, Stillness, Vision, Forgiveness, Hope, Renewal.

Each quote must be:
- 1–3 sentences long
- poetic, soulful, and inspirational
- use beautiful metaphors or natural imagery (like stars, ocean, breath, dawn)
- not repeat words or ideas across quotes
- Each key in the returned JSON must be the name of the theme

Return a JSON object where each key is the theme and value is the quote.
"""

# Generate response from OpenAI
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a poetic assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Extract and parse JSON from response
raw = response.choices[0].message.content.strip()
try:
    quotes = json.loads(raw)
except json.JSONDecodeError:
    print("❌ Error: Could not parse JSON from the response.")
    print("Raw response:", raw)
    exit(1)

# Save the JSON quotes to /data folder
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(quotes, f, indent=4, ensure_ascii=False)

print(f"✅ 24 quotes saved to {output_file}")