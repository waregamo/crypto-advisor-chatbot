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

def get_crypto_data(coin):
    "Retrieve data for a specific cryptocurrency."
    if coin not in crypto_db:
        return None # Return None if coin not found     
    return crypto_db[coin]

def get_sustainable_crypto():
    "Find the most sustainable cryptocurrency."
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

def get_trending_crypto():
    """Find cryptocurrencies with rising price trends."""
    return [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]

def get_profitable_investment():
    "Find cryptocurrencies good for long-term investment."
    return [coin for coin in crypto_db 
            if crypto_db[coin]["price_trend"] == "rising" 
            and crypto_db[coin]["market_cap"] == "high"]

def respond_to_query(user_query):
    user_query = user_query.lower()
    common_cryptos = ['bitcoin', 'ethereum', 'cardano', 'dogecoin', 'pi', 'humancoin', 'ripple', 'solana', 'polkadot', 'worldcoin', 'bnb', 'tether']

    # check for unknown crypto names
    for crypto in common_cryptos:
        if crypto in user_query and crypto.title() not in crypto_db:
            return f"Sorry, {crypto.title()} is not in my database. I can only provide information about: {', '.join(crypto_db.keys())}"
        
    # check how many coins are in the database
    if "how many" in user_query or "how many coins" in user_query:
        return f"There are {len(crypto_db)} cryptocurrencies in my database: {', '.join(crypto_db.keys())}."

    # check for definition queries
    if (
        "definition" in user_query
        or "what is" in user_query
        or user_query.startswith("define ")
        or user_query.startswith("what is bitcoin")
        or user_query.startswith("what is ethereum")
        or user_query.startswith("what is cardano")
    ):
        return "Sorry, I couldn't find any definition for that."

    # Show coin details only if not a definition query
    elif any(coin.lower() in user_query for coin in crypto_db):
        for coin in crypto_db:
            if coin.lower() in user_query:
                data = get_crypto_data(coin)
                return (
                    f"🔍 Here's what I found about {coin}:\n"
                    f"- Price trend: {data['price_trend']}\n"
                    f"- Market cap: {data['market_cap']}\n"
                    f"- Energy use: {data['energy_use']}\n"
                    f"- Sustainability: {data['sustainability_score']*10}/10"
                )

    # Check for sustainability queries
    if "sustainable" in user_query or "eco" in user_query or "green" in user_query:
        coin_data = crypto_db["Cardano"]
        return (
            f"🌱 I recommend Cardano!\n"
            f"This coin is eco-friendly and has good potential for the future!"
        )

    elif "trending" in user_query or "rising" in user_query:
        # Only show Bitcoin and Cardano as trending
        response = [
            "📈 Currently trending cryptocurrencies:",
            "- Bitcoin",
            "- Cardano",
            "\nThese coins are currently showing upward price trends and may be of interest to investors looking for growth opportunities."
        ]
        return "\n".join(response)

    elif "long-term" in user_query or "investment" in user_query:
        coin = "Bitcoin"
        return (
            f"💰 For long-term growth, I recommend {coin}.\n"
            f"This coin shows good stability and growth potential."
        )

    elif "energy" in user_query or "power" in user_query:
        low_energy = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        if low_energy:
            return f"⚡ Low energy consumption coins: {', '.join(low_energy)}\nThese are more environmentally friendly options!"
        return "⚡ Currently no coins with low energy usage in our database."

   
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



