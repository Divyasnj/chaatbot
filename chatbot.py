import re
import random

class Rulebot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    random_questions = (
        "Why are you here?",
        "How many students are there?",
        "Is there any fest in your college?",
        "Does your college have any head?",
        "What courses have you taken?",
        "What things happen every day?"
    )

    def __init__(self):
        self.client = {
            'describe_company_intent': r'.*\s*company.*',
            'answer_why_intent': r'why\sare.*',
            'about_college': r'.*\s*rgukt.*'
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(f"Hi {self.name}, I am Ratan Tata. Will you help me learn about your college?\n")

        if will_help.lower() in self.negative_responses:
            print("Okay, have a nice day!")
            return

        self.chat()

    def make_exit(self, reply):
        if reply in self.exit_commands:
            print("Okay, have a nice day!")
            return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_questions) + "\n").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply) + "\n").lower()

    def match_reply(self, reply):
        for intent, regex_pattern in self.client.items():
            if re.match(regex_pattern, reply):
                if intent == 'describe_company_intent':
                    return self.describe_company_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_college':
                    return self.about_college()

        return self.no_match_intent()

    def describe_company_intent(self):
        responses = [
            "My company is Tata.",
            "I am from Hyderabad, working for Tata company."
        ]
        return random.choice(responses)

    def answer_why_intent(self):
        responses = [
            "I came in search of talented people from your college.",
            "I heard RGUKT is the No.1 college!"
        ]
        return random.choice(responses)

    def about_college(self):
        responses = [
            "RGUKT is a reputed institute for engineering education.",
            "Your college offers excellent courses and has a strong academic reputation."
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responses = [
            "Please tell me more.",
            "Tell me more.",
            "Why do you say that?",
            "I see. Can you elaborate?"
        ]
        return random.choice(responses)

# Run the chatbot
tata = Rulebot()
tata.greet()
