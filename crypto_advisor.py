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

    if "sustainable" in user_query or "eco" in user_query or "green" in user_query:
        recommend = max(crypto_db, key=lambda coin: crypto_db[coin]["sustainability_score"])
        coin_data = crypto_db[recommend]
        return (
            f"🌱 I recommend {recommend}!\n"
            f"- Sustainability Score: {coin_data['sustainability_score']*10}/10\n"
            f"- Energy Usage: {coin_data['energy_use']}\n"
            f"- Current Status: Price {coin_data['price_trend']}, {coin_data['market_cap']} market cap\n"
            f"This coin is eco-friendly and has good potential for the future!"
        )

    elif "trending" in user_query or "rising" in user_query:
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if trending_coins:
            response = ["📈 Currently trending cryptocurrencies:"]
            for coin in trending_coins:
                data = crypto_db[coin]
                response.append(
                    f"- {coin}:\n"
                    f"  • Market Cap: {data['market_cap']}\n"
                    f"  • Sustainability: {data['sustainability_score']*10}/10"
                )
            return "\n".join(response)
        return "📉 No coins are trending up at the moment. Consider looking at long-term investment options."

    elif "long-term" in user_query or "investment" in user_query:
        best_choices = [
            coin for coin in crypto_db
            if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"
        ]
        if best_choices:
            coin = best_choices[0]
            data = crypto_db[coin]
            return (
                f"💰 For long-term growth, I recommend {coin}:\n"
                f"- Strong market cap: {data['market_cap']}\n"
                f"- Price trend: {data['price_trend']}\n"
                f"- Sustainability: {data['sustainability_score']*10}/10\n"
                f"This coin shows good stability and growth potential."
            )
        return "⚠️ Currently no coins meet our criteria for safe long-term investment."

    elif "energy" in user_query or "power" in user_query:
        low_energy = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        if low_energy:
            return f"⚡ Low energy consumption coins: {', '.join(low_energy)}\nThese are more environmentally friendly options!"
        return "⚡ Currently no coins with low energy usage in our database."

    elif "available coins" in user_query or "list all coins" in user_query:
        available_coins = ", ".join(crypto_db.keys())
        return f"💰 Available coins: {available_coins}. You can ask about their trends, sustainability, or long-term growth potential. 📊"

    elif "definition" in user_query or "what is" in user_query:
        return "❓ Sorry, I couldn't find a definition for that. Please ask about sustainability, trends, or long-term growth. 🤖"

    else:
        return (
            "❓ I can help you with:\n"
            "- Sustainability (eco-friendly coins)\n"
            "- Current trends (rising prices)\n"
            "- Long-term investment recommendations\n"
            "- Energy consumption information\n"
            "What would you like to know?"
        )

# 3. Run chatbot interaction
print("👋 Hi, I’m CryptoBuddy, your crypto advisor! 🤖")
print("You can ask me things like: 'Which crypto is trending up?' or 'What’s the most sustainable coin?'\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("CryptoBuddy: Goodbye! Remember to always research before you invest.")
        break
    response = respond_to_query(user_input)
    print("CryptoBuddy:", response)



