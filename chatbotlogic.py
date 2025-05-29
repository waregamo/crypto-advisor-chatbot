# Crypto Advisor Chatbot

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
## 2. Define chatbot logic
def get_crypto_data(coin):
    """Retrieve data for a specific cryptocurrency."""
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
def analyze_query(user_query):
    "Analyze user query and return appropriate response."
    query = user_query.lower()
    
    # Check for specific cryptocurrency queries
    for coin_name in crypto_db.keys():
        if coin_name.lower() in query:
            coin_data = get_crypto_data(coin_name)
            return f"📊 {coin_name} Info:\n- Price Trend: {coin_data['price_trend']}\n- Market Cap: {coin_data['market_cap']}\n- Energy Use: {coin_data['energy_use']}\n- Sustainability Score: {coin_data['sustainability_score']*10}/10"
    
    # Check if query contains a cryptocurrency name not in our database
    common_cryptos = ['bitcoin', 'ethereum', 'cardano', 'dogecoin','pi','humancoin','ripple', 'solana', 'polkadot', 'worldcoin', 'bnb', 'tether']
    for crypto in common_cryptos:
        if crypto in query and crypto.title() not in crypto_db:
            return f"Sorry, {crypto.title()} is not in my database. I can only provide information about: {', '.join(crypto_db.keys())}"
    
    # Check for number of cryptocurrencies in the database
    if "how many" in query:
        coin_list = ", ".join(crypto_db.keys())
        return f"📈 There are {len(crypto_db)} cryptocurrencies in the database:\n{coin_list}"
    
    # Check for sustainability related queries
    if any(word in query for word in ["sustainable", "green", "eco", "environment"]):
        coin = get_sustainable_crypto()
        coin_data = crypto_db[coin]
        return (
            f"🌱 {coin} is the most sustainable cryptocurrency!\n"
            f"- Sustainability Score: {coin_data['sustainability_score']*10}/10\n"
            f"- Energy Usage: {coin_data['energy_use']}\n"
            f"- Market Status: Price {coin_data['price_trend']}, {coin_data['market_cap']} market cap\n"
            f"💡 This coin is eco-friendly and has great long-term potential!"
        )
    
    # Check for trend related queries
    if any(word in query for word in ["trending", "trend", "rising", "up"]):
        trending = get_trending_crypto()
        if trending:
            response = ["📈 Hot Trending Cryptocurrencies:"]
            for coin in trending:
                coin_data = crypto_db[coin]
                response.extend([
                    f"- {coin}:",
                    f"  • Market Cap: {coin_data['market_cap']}",
                    f"  • Sustainability: {coin_data['sustainability_score']*10}/10"
                ])
            return "\n".join(response)
        return "📉 No coins are currently trending up. Consider checking back later or looking at long-term investment options."
    
    # Check for investment/profitability related queries
    if any(word in query for word in ["invest", "profit", "long", "term", "growth"]):
        profitable = get_profitable_investment()
        if profitable:
            return f"💰 For long-term growth, consider {', '.join(profitable)}. They have strong market presence and positive trends."
        return "Currently no coins meet our criteria for safe long-term investment."
    
    # Handle energy usage queries
    if any(word in query for word in ["energy", "power", "consumption"]):
        low_energy = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        if low_energy:
            return f"⚡ These coins have low energy usage: {', '.join(low_energy)}"
        return "No coins with low energy usage found."
    
    # If no specific query matches, provide help message
    return "❓ I can help you with:\n- Sustainability (green/eco-friendly coins)\n- Trends (rising prices)\n- Long-term investment\n- Energy consumption\n- Specific coin information (e.g., 'Tell me about Bitcoin')\nWhat would you like to know?"
## 3. Run chatbot interaction
def run_chatbot():
    "Main function to run the chatbot."
    print("🤖 Hi! I'm CryptoBuddy, your sustainable crypto investment advisor!")
    print("💡 Ask me about sustainable coins, price trends, or investment advice.")
    print("❓ Type 'exit' to end our conversation.\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nCryptoBuddy: Thanks for chatting! Remember: DYOR (Do Your Own Research) 🎓")
            print("Disclaimer: This is not financial advice. Crypto investments carry risks!")
            break
            
        if not user_input:
            print("CryptoBuddy: I didn't catch that. Could you please rephrase your question?")
            continue
            
        response = analyze_query(user_input)
        print(f"\nCryptoBuddy: {response}\n")

if __name__ == "__main__":
    run_chatbot()
    