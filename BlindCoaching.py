#!/usr/bin/env python3

"""
BlindCoaching.py

A simple executable program to guide a self-driven blind coaching session using the GROW model.
You will be prompted to reflect and answer open questions at each stage.
Your answers will be collected and printed as a report at the end of the session.
"""

def load_questions(filename="coaching_questions.txt"):
    """Load questions from external text file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        sections = []
        current_section = None
        questions = []
        
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('=== ') and line.endswith(' ==='):
                # Save previous section if exists
                if current_section:
                    sections.append((current_section, questions))
                # Start new section
                current_section = line[4:-4]  # Remove === and ===
                questions = []
            elif line and not line.startswith('==='):
                questions.append(line)
        
        # Add the last section
        if current_section:
            sections.append((current_section, questions))
        
        return sections
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using default questions.")
        return [
            ("Goal", ["Define your most important current objective. What do you want to achieve?"]),
            ("Reality", ["Describe your current situation. What is happening now? What have you tried so far?"]),
            ("Options", ["Brainstorm possible options. What could you do? What alternatives exist?"]),
            ("Will (Way Forward)", ["Decide on your next steps. What will you do? When will you do it? What support do you need?"])
        ]

def prompt_section(title, questions):
    print(f"\n=== {title} ===")
    answers = []
    for i, question in enumerate(questions, 1):
        print(f"\n{i}. {question}")
        answer = input("Your answer: ")
        answers.append((question, answer))
    return (title, answers)

def main():
    print("Welcome to the Blind Coaching Session (GROW Model) with SMART Goal Setting\n")
    print("Session Goal: This session will guide you through the GROW framework to help you tackle your current objective.")
    print("At each stage, you will be prompted to reflect and answer open questions.")
    print("Take your time to think and write your answers in a journal or text editor if you wish.\n")

    # Load questions from external file
    sections = load_questions()

    answers = []
    for title, questions in sections:
        result = prompt_section(title, questions)
        answers.append(result)

    print("\nSession complete! Review your answers and commit to your next Goal.\n")
    print("=== Coaching Session Report ===")
    for title, qa_pairs in answers:
        print(f"\n[{title}]")
        for question, answer in qa_pairs:
            print(f"Q: {question}")
            print(f"A: {answer}")
            print()

    # Salva il report anche su file di testo
    report_path = "coaching_session_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=== Coaching Session Report ===\n")
        for title, qa_pairs in answers:
            f.write(f"\n[{title}]\n")
            for question, answer in qa_pairs:
                f.write(f"Q: {question}\n")
                f.write(f"A: {answer}\n")
                f.write("\n")
    print(f"Report salvato in: {report_path}")

if __name__ == "__main__":
    main()