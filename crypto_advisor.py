# 1. Predefined crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 0.3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 0.6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.8
    }
}

# 2. Define chatbot logic
def respond_to_query(user_query):
    user_query = user_query.lower()

    # Sustainability & Energy Use questions
    if any(kw in user_query for kw in ["sustainable", "least energy", "environmentally friendly", "greenest", "eco"]):
        recommend = max(crypto_db, key=lambda coin: crypto_db[coin]["sustainability_score"])
        energy_use_low = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        response_parts = []
        if "least energy" in user_query or "energy" in user_query:
            if energy_use_low:
                response_parts.append(f"The coin(s) using the least energy: {', '.join(energy_use_low)}.")
            else:
                response_parts.append("No coins with low energy use found.")
        if any(kw in user_query for kw in ["sustainable", "environmentally friendly", "greenest", "eco"]):
            response_parts.append(f"I recommend {recommend}. It is eco-friendly and has good potential for the future.")
        return " ".join(response_parts)

    # Trending & Profitability questions
    elif any(kw in user_query for kw in ["trending up", "rising in price", "trending", "rising"]):
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if trending_coins:
            return f"The coins that are currently trending up are: {', '.join(trending_coins)}."
        else:
            return "There are no coins trending up at the moment."

    elif any(kw in user_query for kw in ["good coin for making profit", "high market cap and is trending", "good for profit"]):
        best_choices = [
            coin for coin in crypto_db
            if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"
        ]
        if best_choices:
            return f"For profit, consider {best_choices[0]}. It is trending and has a high market cap."
        else:
            return "I couldn't find a good coin for profit based on the data."

    # Long-Term Investment questions
    elif any(kw in user_query for kw in ["long-term growth", "long-term profits", "strong future potential", "invest in for long-term"]):
        best_choices = [
            coin for coin in crypto_db
            if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"
        ]
        if best_choices:
            return f"For long-term growth, consider {best_choices[0]}. It has strong market support and good profit potential."
        else:
            return "I couldn't find a good option for long-term investment based on the data."

    else:
        return "Sorry, I didn't understand your question. Please ask about sustainability, trends, profitability, or long-term growth."

# 3. Run chatbot interaction
print("👋 Hi, I’m CryptoBuddy, your crypto advisor!")
print("You can ask me things like: 'Which crypto is trending up?' or 'What’s the most sustainable coin?'\n")

while True:
    user_input = input("💬 You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("CryptoBuddy: Goodbye! Remember to always research before you invest.")
        break
    response = respond_to_query(user_input)
    print("🤖 CryptoBuddy:", response)
 


