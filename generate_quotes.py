import json
from datetime import datetime

themes_and_quotes = [
    ("Silence", "Silence is not empty; it is full of answers."),
    ("Wonder", "Let wonder be the lens through which you see the ordinary."),
    ("Discipline", "Discipline is the bridge between your longing and becoming."),
    ("Growth", "Growth often disguises itself in discomfort."),
    ("Healing", "Some wounds teach, others remind — but all heal with time."),
    ("Faith", "Faith isn’t the absence of doubt, but the courage to walk with it."),
    ("Simplicity", "In simplicity, we return to what truly matters."),
    ("Wisdom", "Wisdom is the echo of truth heard in quiet surrender."),
    ("Focus", "The sun doesn’t burn until brought to a single point."),
    ("Gratitude", "Gratitude rewrites even broken days into sacred text."),
    ("Courage", "Courage doesn’t roar — it whispers, 'try again tomorrow.'"),
    ("Balance", "Balance is not perfection; it’s the rhythm of realignment."),
    ("Peace", "Peace is when your spirit exhales."),
    ("Joy", "Joy is not in things; it is in the overflow of being."),
    ("Perseverance", "Even the tide returns — so will you."),
    ("Compassion", "Compassion is strength wrapped in softness."),
    ("Presence", "The present moment is the only place life breathes."),
    ("Clarity", "When the heart clears, the path does too."),
    ("Purpose", "Purpose is a whisper louder than fear."),
    ("Stillness", "Stillness is not inactivity — it’s alignment."),
    ("Vision", "Vision sees not what is, but what can be."),
    ("Forgiveness", "Forgiveness is the gift you give yourself first."),
    ("Hope", "Hope is rebellion against despair."),
    ("Renewal", "Renewal is not a return — it is a resurrection."),
]

today = datetime.now().strftime("%Y_%m_%d")
output_file = f"data/quotes_{today}.json"

# Assemble quotes
quotes = []
for i, (theme, quote) in enumerate(themes_and_quotes):
    hour = f"{i:02d}:00"
    quotes.append({
        "hour": hour,
        "theme": theme,
        "quote": quote
    })

# Write to JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)

print(f"✅ Saved 24 poetic quotes to {output_file}")