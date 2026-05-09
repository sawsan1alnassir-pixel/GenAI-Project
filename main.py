def generate_text(prompt):
    response = (
        "Generative AI can support RPTM and Hospitality students by helping with "
        "event planning, tourism marketing, customer service communication, budgeting, "
        "and scheduling. For example, AI can help create event promotion messages, "
        "suggest travel or recreation activities, organize planning tasks, and generate "
        "professional responses for guests or customers. However, students still need "
        "to review the AI output because it may include mistakes or information that "
        "does not fully match the real situation."
    )
    return response


def main():
    prompt = "How can Generative AI support RPTM and Hospitality?"

    print("Prompt:")
    print(prompt)
    print("\nAI Response:")
    print(generate_text(prompt))


if __name__ == "__main__":
    main()
