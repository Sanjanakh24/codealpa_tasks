def chatbot_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm doing great! How can I help you?"

    elif "services" in user_input:
        return "We provide cloud computing, AI solutions, and software development services."

    elif "cloud computing" in user_input:
        return "Cloud computing is the delivery of computing services over the internet like storage, servers, and databases."

    elif "internship" in user_input:
        return "Yes, we offer internships in cloud computing, AI, and web development."

    elif "certificate" in user_input:
        return "Yes, a completion certificate is provided after successful task submission."

    elif "contact" in user_input or "email" in user_input:
        return "You can contact us at services@codealpha.tech"

    elif "bye" in user_input:
        return "Thank you for chatting with us. Have a great day!"

    else:
        return "Sorry, I didn’t understand that. Please try asking something else."
