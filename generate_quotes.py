import json
from datetime import datetime
import openai  # Requires 'openai' Python package

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

themes = [
    "Silence", "Wonder", "Discipline", "Growth", "Healing", "Faith", "Simplicity", "Wisdom",
    "Focus", "Gratitude", "Courage", "Balance", "Peace", "Joy", "Perseverance", "Compassion",
    "Presence", "Clarity", "Purpose", "Stillness", "Vision", "Forgiveness", "Hope", "Renewal"
]

today = datetime.today().strftime("%Y_%m_%d")
output_file = f"data/quotes_{today}.json"

hourly_quotes = []

for i, theme in enumerate(themes):
    prompt = f"""You are an oracle of timeless wisdom. Write a single, short, poetic quote themed around '{theme}', meant to uplift someone at hour {i:02d}:00 of their day. No generic advice. Each quote must be unique, rich, and soul-stirring. Format it as a raw quote, no intro or author."""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=60
    )

    quote = response['choices'][0]['message']['content'].strip().replace('"', '')
    hourly_quotes.append({
        "hour": f"{i:02d}:00",
        "theme": theme,
        "quote": quote
    })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(hourly_quotes, f, ensure_ascii=False, indent=2)

print(f"✅ Saved: {output_file}")