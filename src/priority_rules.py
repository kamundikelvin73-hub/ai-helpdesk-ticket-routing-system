def assign_priority(category, description):
    description = description.lower()
    if category == "Security":
        return "High"
    if any(word in description for word in ["cannot access", "locked out", "urgent"]):
        return "High"
    if any(word in description for word in ["crash", "freezes", "not working"]):
        return "Medium"
    return "Low"

if __name__ == "__main__":
    print(assign_priority("Account Access", "I cannot access my account"))
