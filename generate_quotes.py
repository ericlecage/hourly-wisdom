import json
from datetime import datetime

def generate_quotes():
    quotes = []
    themes = [
        "Silence", "Wonder", "Reflection", "Renewal", "Awakening", "Gratitude",
        "Intention", "Strength", "Courage", "Discipline", "Presence", "Balance",
        "Focus", "Patience", "Resilience", "Wisdom", "Compassion", "Surrender",
        "Peace", "Love", "Faith", "Legacy", "Mystery", "Eternity"
    ]

    for i in range(24):
        hour = f"{i:02}:00"
        theme = themes[i]
        quote = f"This is a placeholder quote for {theme} at {hour}."
        quotes.append({"hour": hour, "theme": theme, "quote": quote})

    today = datetime.today().strftime('%Y_%m_%d')
    filename = f"data/quotes_{today}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    generate_quotes()
