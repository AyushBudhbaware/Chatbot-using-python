import re

def simple_chatbot():
    print("Hello! I'm your enhanced chatbot. Ask me something or type 'exit' to leave.")
    
    # Variables for KPI
    successful_responses = 0
    total_queries = 0
    
    patterns = {
        r'hello': "Hi there!",
        r'how are you': "I'm just a program, so I don't have feelings, but thanks for asking!",
        r'your name': "I'm an enhanced chatbot using pattern matching!",
        r'favorite color': "I don't have personal preferences, but blue seems popular.",
        r'joke': "Why did the programmer quit his job? He didn't get arrays!",
        r'thanks': "You're welcome!",
        r'sleep': "I don't sleep. Always up and running.",
        r'age': "I'm just a piece of code, so I don't age like humans.",
        r'birthday': "Every day is a good day for me. No birthday needed.",
        r'time': "I don't track time, but you can check your device's clock.",
        r'date': "Please check your calendar; I don't keep track.",
        r'movie': "I don't watch movies, but I can help you find one.",
        r'music': "While I don't listen to music, I know a lot about it.",
        r'help': "Of course! Ask me anything.",
        r'love': "I'm just code, so I don't feel emotions like love.",
        r'human': "No, I'm a machine learning model.",
        r'robot': "Close enough. I'm a digital chatbot.",
        r'fun': "I'm designed to be informative, but I can try to be fun!",
        r'book': "There are many great books out there. Any specific genre in mind?",
        r'food': "I don't eat, but I have information on many foods!",
        r'drink': "Digital beings like me don't drink, but I can tell you about various drinks.",
        r'country': "I have knowledge about many countries. Which one are you curious about?",
        r'city': "I know about many cities. Ask away!",
        r'sports': "Which sport are you interested in?",
        r'weather': "I can't forecast, but there are great apps for that!",
        r'news': "I don't have real-time updates, but I can share general knowledge.",
        r'language': "I can understand and generate text in multiple languages.",
        r'family': "I don't have a family; I'm a program.",
        r'hi':"hello.",
        r'friend': "All users are my friends! I'm here to help."
    }
    
    while True:
        user_input = input("You: ").lower()

        if 'exit' in user_input:
            break

        total_queries += 1  # Increment total queries
        
        responded = False
        for pattern, response in patterns.items():
            if re.search(pattern, user_input):
                print(f"Chatbot: {response}")
                responded = True
                successful_responses += 1  # Increment successful responses
                break
        
        if not responded:
            print("Chatbot: I'm not sure how to respond to that.")
            feedback = input("Please provide feedback on how I can improve: ")
            # Store the feedback (for now, we just print it)
            print(f"Feedback received: {feedback}")
            
    # Display KPI after user exits
    if total_queries > 0:
        success_rate = (successful_responses / total_queries) * 100
        print(f"Chatbot KPI: Successfully responded to {success_rate:.2f}% of queries.")
    else:
        print("Chatbot: Goodbye! Have a great day!")

# To run the chatbot:
simple_chatbot()
