# Rulebot - Simple Chatbot in Python

Rulebot is a basic chatbot implemented in Python that interacts with users and answers questions about Tata company and RGUKT college. It uses regular expressions to identify user intents and provides appropriate responses.

## Features

- Greets the user and asks about their college.
- Handles different user intents:
  - **describe_company_intent** - Provides information about Tata company.
  - **answer_why_intent** - Explains why the chatbot is asking questions.
  - **about_college** - Gives information about RGUKT.
- Recognizes exit commands like `quit`, `exit`, and `bye`.
- Asks random questions to engage with the user.
- Responds with predefined answers based on user input.

## Installation & Requirements

This chatbot requires **Python 3.x** to run. It also uses the following built-in libraries:

- `random` (for selecting random responses)
- `re` (for matching user inputs using regular expressions)

No external dependencies are needed.

## How to Run

1. Clone or download this repository.
2. Navigate to the project folder.
3. Run the chatbot using:

   ```sh
   python chatbot.py
