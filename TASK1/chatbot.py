def chatbot():
    print("Chatbot: Namaste! I'm ChatBot. Ask me anything about India or tech. (Type 'exit' to quit)")
    
    while True:
        user_input = input("You: ").lower()

        # Greetings
        if user_input in ["hi", "hello", "hey", "namaste"]:
            print("Chatbot: Hello! How can I assist you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great! Ready to chat anytime.")
        
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot, your friendly assistant.")
        
        elif "help" in user_input:
            print("Chatbot: You can ask me about Indian facts or technology-related topics.")

        # Time and weather
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"Chatbot: The current time is {now.strftime('%H:%M:%S')}")
        
        elif "weather" in user_input:
            print("Chatbot: I can’t access live weather updates yet, but I hope it’s pleasant where you are!")

        # India-specific Questions
        elif "capital of india" in user_input:
            print("Chatbot: The capital of India is New Delhi.")
        
        elif "prime minister of india" , "pm of india" in user_input:
            print("Chatbot: As of 2025, the Prime Minister of India is Narendra Modi.")
        
        elif "national animal of india" in user_input:
            print("Chatbot: The national animal of India is the Bengal Tiger.")
        
        elif "national bird of india" in user_input:
            print("Chatbot: The national bird of India is the Indian Peacock.")
        
        elif "national flower of india" in user_input:
            print("Chatbot: The national flower of India is the Lotus.")
        
        elif "independence day of india" in user_input:
            print("Chatbot: India celebrates its Independence Day on 15th August.")
        
        elif "population of india" in user_input:
            print("Chatbot: India has a population of over 1.4 billion people as of 2025.")
        
        elif "taj mahal" in user_input:
            print("Chatbot: The Taj Mahal is a world-famous white marble mausoleum in Agra, built by Emperor Shah Jahan.")
        
        elif "currency of india" in user_input:
            print("Chatbot: The currency of India is the Indian Rupee (INR).")

        # Tech-related Questions
        elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
            print("Chatbot: Artificial Intelligence (AI) is the simulation of human intelligence by machines, especially computer systems.")

        elif "what is python" in user_input:
            print("Chatbot: Python is a popular high-level programming language known for its simplicity and readability.")

        elif "who founded google" in user_input:
            print("Chatbot: Google was founded by Larry Page and Sergey Brin in 1998.")

        elif "what is the internet" in user_input:
            print("Chatbot: The Internet is a global network that connects millions of private, public, academic, business, and government networks.")

        elif "latest tech trends" in user_input or "current technology" in user_input:
            print("Chatbot: Popular tech trends in 2025 include AI, quantum computing, 5G, edge computing, and augmented reality.")

        elif "what is machine learning" in user_input:
            print("Chatbot: Machine Learning is a subset of AI that allows systems to learn and improve from experience without being explicitly programmed.")

        elif user_input == "exit":
            print("Chatbot: Goodbye! Stay curious and keep learning!")
            break
        
        else:
            print("Chatbot: I didn't catch that. Try asking about Indian facts or technology topics.")

# Run the chatbot
chatbot()
