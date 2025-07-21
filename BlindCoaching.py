#!/usr/bin/env python3

"""
BlindCoaching.py

A simple executable program to guide a self-driven blind coaching session using the GROW model.
You will be prompted to reflect and answer open questions at each stage.
Your answers will be collected and printed as a report at the end of the session.
"""

def prompt_section(title, instructions):
    print(f"\n=== {title} ===")
    print(instructions)
    answer = input("Your answer: ")
    return (title, instructions, answer)

def main():
    print("Welcome to the Blind Coaching Session (GROW Model) with SMART Goal Setting\n")
    print("Session Goal: This session will guide you through the GROW framework to help you tackle your current objective.")
    print("At each stage, you will be prompted to reflect and answer open questions (to be provided by you).")
    print("Take your time to think and write your answers in a journal or text editor if you wish.\n")

    sections = [
        ("Goal", 
         "Define your most important current objective. What do you want to achieve?"),
        ("Reality", 
         "Describe your current situation. What is happening now? What have you tried so far?"),
        ("Options", 
         "Brainstorm possible options. What could you do? What alternatives exist?"),
        ("Will (Way Forward)", 
         "Decide on your next steps. What will you do? When will you do it? What support do you need?")
    ]

    answers = []
    for title, instructions in sections:
        result = prompt_section(title, instructions)
        answers.append(result)

    print("\nSession complete! Review your answers and commit to your next Goal.\n")
    print("=== Coaching Session Report ===")
    for title, question, answer in answers:
        print(f"\n[{title}]")
        print(f"Q: {question}")
        print(f"A: {answer}")

    # Salva il report anche su file di testo
    report_path = "coaching_session_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=== Coaching Session Report ===\n")
        for title, question, answer in answers:
            f.write(f"\n[{title}]\n")
            f.write(f"Q: {question}\n")
            f.write(f"A: {answer}\n")
    print(f"\nReport salvato in: {report_path}")

if __name__ == "__main__":
    main()