def classify_ticket(text):
    text = text.lower()
    if any(word in text for word in ["password", "login", "mfa", "account"]):
        return "Account Access"
    if any(word in text for word in ["zoom", "teams", "crash", "audio", "microphone"]):
        return "Technical Support"
    if any(word in text for word in ["invoice", "charged", "payment", "subscription"]):
        return "Billing"
    if any(word in text for word in ["phishing", "suspicious", "password email"]):
        return "Security"
    return "General Inquiry"

if __name__ == "__main__":
    example = "I cannot login after resetting my password"
    print(classify_ticket(example))
