#!/usr/bin/env python3
"""
Blind Coaching Standalone Application
A complete self-contained coaching application based on the GROW model
"""

import os
import sys
import webbrowser
import threading
import time
from datetime import datetime
import json

# Check if Flask is available, if not provide installation instructions
try:
    from flask import Flask, render_template_string, request, jsonify, Response
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

# Embedded HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blind Coaching Session - GROW Model</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #ffd4c4 0%, #ffb399 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .section:hover {
            transform: translateY(-5px);
        }

        .section-title {
            font-size: 1.8rem;
            color: #d97742;
            margin-bottom: 20px;
            border-bottom: 3px solid #d97742;
            padding-bottom: 10px;
        }

        .question {
            margin-bottom: 20px;
        }

        .question-text {
            font-weight: 600;
            color: #555;
            margin-bottom: 8px;
            font-size: 1.1rem;
        }

        .answer-input {
            width: 100%;
            min-height: 100px;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1rem;
            resize: vertical;
            transition: border-color 0.3s ease;
            font-family: inherit;
        }

        .answer-input:focus {
            outline: none;
            border-color: #d97742;
            box-shadow: 0 0 0 3px rgba(217, 119, 66, 0.15);
        }

        .navigation {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 30px 0;
        }

        .btn {
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary {
            background: linear-gradient(135deg, #ffc299 0%, #d97742 100%);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(217, 119, 66, 0.3);
        }

        .btn-secondary {
            background: #f8f9fa;
            color: #d97742;
            border: 2px solid #d97742;
        }

        .btn-secondary:hover {
            background: #d97742;
            color: white;
        }

        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: rgba(255,255,255,0.3);
            border-radius: 4px;
            margin: 20px 0;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: white;
            border-radius: 4px;
            transition: width 0.3s ease;
        }

        .hidden {
            display: none;
        }

        .completion-screen {
            text-align: center;
            background: white;
            border-radius: 15px;
            padding: 50px 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .completion-screen h2 {
            color: #d97742;
            font-size: 2rem;
            margin-bottom: 20px;
        }

        .completion-screen p {
            font-size: 1.1rem;
            margin-bottom: 30px;
            color: #666;
        }

        .recap-item {
            margin-bottom: 15px;
            padding: 15px;
            background: white;
            border-left: 4px solid #d97742;
            border-radius: 5px;
        }

        .recap-item strong {
            color: #d97742;
        }

        #goalSummaryContent {
            max-height: 400px;
            overflow-y: auto;
        }

        .goal-reminder {
            background: linear-gradient(135deg, #ffc299 0%, #d97742 100%);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(217, 119, 66, 0.2);
            animation: slideIn 0.5s ease-out;
        }

        .goal-reminder-content {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .goal-reminder-label {
            font-weight: 600;
            font-size: 1rem;
            white-space: nowrap;
        }

        #goalReminderText {
            flex: 1;
            font-size: 1rem;
            line-height: 1.4;
            min-width: 200px;
        }

        .goal-reminder-edit {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: background 0.3s ease;
        }

        .goal-reminder-edit:hover {
            background: rgba(255, 255, 255, 0.3);
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .navigation {
                flex-direction: column;
                gap: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Blind Coaching Session</h1>
            <p>GROW Model with SMART Goal Setting</p>
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill"></div>
            </div>
        </div>

        <div id="coachingForm">
            <!-- Goal Reminder Banner -->
            <div id="goalReminder" class="goal-reminder hidden">
                <div class="goal-reminder-content">
                    <span class="goal-reminder-label">🎯 Your Goal:</span>
                    <span id="goalReminderText">Your goal statement will appear here</span>
                    <button class="goal-reminder-edit" onclick="editGoalStatement()">✏️</button>
                </div>
            </div>

            {% for section in sections %}
            <div class="section {% if loop.index0 > 0 %}hidden{% endif %}" id="section-{{ loop.index0 }}">
                <h2 class="section-title">{{ section.title }}</h2>
                {% set outer_loop = loop %}
                {% for question in section.questions %}
                <div class="question">
                    <div class="question-text">{{ loop.index }}. {{ question }}</div>
                    <textarea 
                        class="answer-input" 
                        id="answer-{{ outer_loop.index0 }}-{{ loop.index0 }}"
                        placeholder="Take your time to reflect and write your answer here..."
                        data-section="{{ outer_loop.index0 }}"
                        data-question="{{ loop.index0 }}"
                    ></textarea>
                </div>
                {% endfor %}
            </div>
            {% endfor %}
        </div>

        <!-- Goal Recap Section -->
        <div id="goalRecap" class="section hidden">
            <h2 class="section-title">🎯 Your Goal Summary</h2>
            <p style="margin-bottom: 20px; color: #666; font-size: 1.1rem;">
                Before proceeding to assess your current reality, let's review the goal you've defined. 
                This is your opportunity to refine or clarify your objective.
            </p>
            
            <div id="goalSummaryContent" style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <!-- Goal summary will be populated by JavaScript -->
            </div>
            
            <!-- Goal Statement Section -->
            <div style="background: linear-gradient(135deg, #ffc299 0%, #d97742 100%); padding: 20px; border-radius: 10px; margin-bottom: 20px; color: white;">
                <h3 style="margin-bottom: 15px; color: white;">📝 Your Goal Statement</h3>
                <p style="margin-bottom: 10px; opacity: 0.9;">Summarize your goal using this format: <strong>"I will [Specific Goal] by [Timeframe]"</strong></p>
                <textarea 
                    id="goalStatement" 
                    placeholder="Format: I will [your specific goal] by [your timeframe].&#10;&#10;Example: I will increase my monthly revenue by 25% by the end of the next 6 months."
                    style="width: 100%; min-height: 80px; padding: 15px; border: none; border-radius: 8px; font-size: 1rem; resize: vertical; font-family: inherit; line-height: 1.5;"
                ></textarea>
                <p style="margin-top: 10px; font-size: 0.9rem; opacity: 0.8;">💡 This statement will appear at the top of each section as a reminder of your goal.</p>
            </div>
            
            <div style="margin-top: 25px;">
                <button class="btn btn-secondary" onclick="editGoal()" style="margin-right: 15px;">
                    ✏️ Edit Goal
                </button>
                <p style="margin-top: 15px; color: #666; font-style: italic;">
                    💡 Take a moment to reflect: Is this goal specific, measurable, achievable, relevant, and time-bound?
                </p>
            </div>
        </div>

        <div class="navigation">
            <button class="btn btn-secondary" id="prevBtn" onclick="changeSection(-1)" disabled>
                ← Previous
            </button>
            <span id="sectionIndicator">Section 1 of {{ sections|length }}</span>
            <button class="btn btn-primary" id="nextBtn" onclick="changeSection(1)">
                Next →
            </button>
        </div>

        <div id="completionScreen" class="completion-screen hidden">
            <h2>🎉 Session Complete!</h2>
            <p>Congratulations! You've completed your coaching session using the GROW model.</p>
            <p>Review your answers and commit to your next steps.</p>
            <div style="margin-top: 30px;">
                <button class="btn btn-primary" onclick="downloadReport()">
                    📄 Download Report
                </button>
                <button class="btn btn-secondary" onclick="startNewSession()" style="margin-left: 15px;">
                    🔄 Start New Session
                </button>
            </div>
        </div>
    </div>

    <script>
        const sections = {{ sections | tojson }};
        let currentSection = 0;
        const totalSections = sections.length;

        function updateProgress() {
            const progress = ((currentSection + 1) / totalSections) * 100;
            document.getElementById('progressFill').style.width = progress + '%';
        }

        function updateNavigationForRecap() {
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            const indicator = document.getElementById('sectionIndicator');

            prevBtn.disabled = false;
            nextBtn.textContent = 'Continue to Reality →';
            indicator.textContent = 'Goal Summary & Review';
            
            const progress = ((1.5) / totalSections) * 100;
            document.getElementById('progressFill').style.width = progress + '%';
        }

        function updateGoalRecap() {
            const goalSection = sections[0];
            let goalSummary = '';
            let combinedAnswers = '';
            
            goalSection.questions.forEach((question, questionIndex) => {
                const textarea = document.getElementById(`answer-0-${questionIndex}`);
                const answer = textarea ? textarea.value.trim() : '';
                if (answer) {
                    goalSummary += `<div class="recap-item">
                        <strong>Q:</strong> ${question}<br>
                        <strong>A:</strong> ${answer}
                    </div>`;
                    combinedAnswers += answer + ' ';
                }
            });

            if (!goalSummary) {
                goalSummary = '<p><em>No goals defined yet. Please go back and complete the Goal section.</em></p>';
            }

            document.getElementById('goalSummaryContent').innerHTML = goalSummary;
            
            const goalStatementField = document.getElementById('goalStatement');
            if (!goalStatementField.value.trim() && combinedAnswers.trim()) {
                const suggestion = generateGoalSuggestion(combinedAnswers.trim());
                goalStatementField.value = suggestion;
            }
        }

        function generateGoalSuggestion(combinedAnswers) {
            const goalSection = sections[0];
            let specific = '';
            let timeframe = '';
            
            goalSection.questions.forEach((question, questionIndex) => {
                const textarea = document.getElementById(`answer-0-${questionIndex}`);
                const answer = textarea ? textarea.value.trim() : '';
                
                if (answer) {
                    if (question.toLowerCase().includes('specifically') || question.toLowerCase().includes('what') && questionIndex === 0) {
                        specific = answer;
                    }
                    else if (question.toLowerCase().includes('when') || question.toLowerCase().includes('timeframe') || question.toLowerCase().includes('by when')) {
                        timeframe = answer;
                    }
                }
            });
            
            specific = specific.replace(/^(I want to|I will|I would like to|I plan to|My goal is to)\s*/i, '').trim();
            timeframe = timeframe.replace(/^(by|within|in|before)\s*/i, '').trim();
            
            let goalStatement = '';
            
            if (specific && timeframe) {
                goalStatement = `I will ${specific} by ${timeframe}`;
            } else if (specific) {
                goalStatement = `I will ${specific}`;
            } else {
                goalStatement = combinedAnswers.replace(/\s+/g, ' ').trim();
                if (!goalStatement.toLowerCase().startsWith('i will')) {
                    goalStatement = 'I will ' + goalStatement.charAt(0).toLowerCase() + goalStatement.slice(1);
                }
            }
            
            goalStatement = goalStatement.charAt(0).toUpperCase() + goalStatement.slice(1);
            if (!goalStatement.endsWith('.')) {
                goalStatement += '.';
            }
            
            return goalStatement;
        }

        function updateGoalReminder() {
            const goalStatement = document.getElementById('goalStatement');
            const goalReminderText = document.getElementById('goalReminderText');
            const goalReminder = document.getElementById('goalReminder');
            
            if (goalStatement && goalStatement.value.trim()) {
                goalReminderText.textContent = goalStatement.value.trim();
                if (currentSection >= 1 && currentSection < totalSections) {
                    goalReminder.classList.remove('hidden');
                } else {
                    goalReminder.classList.add('hidden');
                }
            } else {
                goalReminder.classList.add('hidden');
            }
        }

        function editGoalStatement() {
            currentSection = 0.5;
            showSection(currentSection);
            updateNavigationForRecap();
            
            setTimeout(() => {
                document.getElementById('goalStatement').focus();
            }, 100);
        }

        function editGoal() {
            currentSection = 0;
            showSection(currentSection);
            updateNavigation();
        }

        function updateNavigation() {
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            const indicator = document.getElementById('sectionIndicator');

            prevBtn.disabled = currentSection === 0;
            
            if (currentSection === totalSections - 1) {
                nextBtn.textContent = 'Complete Session →';
            } else {
                nextBtn.textContent = 'Next →';
            }

            indicator.textContent = `Section ${currentSection + 1} of ${totalSections}`;
            updateProgress();
        }

        function showSection(index) {
            for (let i = 0; i < totalSections; i++) {
                document.getElementById(`section-${i}`).classList.add('hidden');
            }
            document.getElementById('goalRecap').classList.add('hidden');
            
            if (index === 0.5) {
                document.getElementById('goalRecap').classList.remove('hidden');
                document.getElementById('coachingForm').classList.remove('hidden');
                document.getElementById('completionScreen').classList.add('hidden');
                updateGoalRecap();
            } else if (index < totalSections) {
                document.getElementById(`section-${index}`).classList.remove('hidden');
                document.getElementById('coachingForm').classList.remove('hidden');
                document.getElementById('completionScreen').classList.add('hidden');
            } else {
                document.getElementById('coachingForm').classList.add('hidden');
                document.getElementById('completionScreen').classList.remove('hidden');
            }
            
            updateGoalReminder();
        }

        function changeSection(direction) {
            if (direction === 1) {
                if (currentSection === 0) {
                    currentSection = 0.5;
                    showSection(currentSection);
                    updateNavigationForRecap();
                    return;
                } else if (currentSection === 0.5) {
                    currentSection = 1;
                    showSection(currentSection);
                    updateNavigation();
                    return;
                } else if (currentSection === totalSections - 1) {
                    currentSection = totalSections;
                    showSection(currentSection);
                    document.querySelector('.navigation').style.display = 'none';
                    return;
                }
            } else if (direction === -1) {
                if (currentSection === 0.5) {
                    currentSection = 0;
                    showSection(currentSection);
                    updateNavigation();
                    return;
                } else if (currentSection === 1) {
                    currentSection = 0.5;
                    showSection(currentSection);
                    updateNavigationForRecap();
                    return;
                }
            }

            const newSection = currentSection + direction;
            if (newSection >= 0 && newSection < totalSections) {
                currentSection = newSection;
                showSection(currentSection);
                updateNavigation();
            }
        }

        function collectAnswers() {
            const sessionData = {
                goalStatement: '',
                sections: []
            };

            const goalStatementField = document.getElementById('goalStatement');
            if (goalStatementField) {
                sessionData.goalStatement = goalStatementField.value.trim();
            }

            sections.forEach((section, sectionIndex) => {
                const sectionData = {
                    title: section.title,
                    answers: []
                };

                section.questions.forEach((question, questionIndex) => {
                    const textarea = document.getElementById(`answer-${sectionIndex}-${questionIndex}`);
                    if (textarea) {
                        sectionData.answers.push({
                            question: question,
                            answer: textarea.value || ''
                        });
                    } else {
                        sectionData.answers.push({
                            question: question,
                            answer: ''
                        });
                    }
                });

                sessionData.sections.push(sectionData);
            });

            return sessionData;
        }

        function downloadReport() {
            const sessionData = collectAnswers();
            
            const hasAnswers = sessionData.sections.some(section => 
                section.answers.some(qa => qa.answer.trim() !== '')
            );
            
            if (!hasAnswers) {
                alert('Please answer at least one question before downloading the report.');
                return;
            }
            
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/download_direct';
            form.style.display = 'none';
            
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'session_data';
            input.value = JSON.stringify(sessionData);
            
            form.appendChild(input);
            document.body.appendChild(form);
            form.submit();
            document.body.removeChild(form);
        }

        function startNewSession() {
            document.querySelectorAll('.answer-input').forEach(textarea => {
                textarea.value = '';
            });
            
            currentSection = 0;
            showSection(currentSection);
            updateNavigation();
            document.querySelector('.navigation').style.display = 'flex';
            
            document.getElementById('goalSummaryContent').innerHTML = '';
        }

        updateNavigation();
        updateProgress();
        
        document.addEventListener('DOMContentLoaded', function() {
            const goalStatement = document.getElementById('goalStatement');
            if (goalStatement) {
                goalStatement.addEventListener('input', updateGoalReminder);
                goalStatement.addEventListener('blur', updateGoalReminder);
            }
        });
    </script>
</body>
</html>"""

# Default questions
DEFAULT_QUESTIONS = [
    {
        "title": "Goal (SMART)",
        "questions": [
            "What specifically do you want to achieve? [Specific]",
            "How will you measure your success? [Measurable]",
            "Is this goal realistic with your current resources? [Achievable]",
            "Why is this goal important to you right now? [Relevant]",
            "By when do you want to accomplish this? [Time-bound]"
        ]
    },
    {
        "title": "Reality",
        "questions": [
            "What is your current situation regarding this goal?",
            "What have you already tried?",
            "What obstacles are you facing?",
            "What resources do you currently have?"
        ]
    },
    {
        "title": "Options",
        "questions": [
            "What are all the possible ways you could approach this?",
            "What would you do if you had unlimited resources?",
            "Who could help you with this goal?",
            "What alternatives exist if your first choice doesn't work?"
        ]
    },
    {
        "title": "Way Forward",
        "questions": [
            "What specific actions will you take?",
            "When will you start each action?",
            "What support do you need?",
            "How will you track your progress?"
        ]
    }
]

def load_questions_from_file():
    """Load questions from coaching_questions.txt if it exists."""
    try:
        if os.path.exists('coaching_questions.txt'):
            with open('coaching_questions.txt', 'r', encoding='utf-8') as f:
                content = f.read()
            
            sections = []
            current_section = None
            questions = []
            
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('=== ') and line.endswith(' ==='):
                    if current_section:
                        sections.append({"title": current_section, "questions": questions})
                    current_section = line[4:-4]
                    questions = []
                elif line and not line.startswith('==='):
                    questions.append(line)
            
            if current_section:
                sections.append({"title": current_section, "questions": questions})
            
            return sections if sections else DEFAULT_QUESTIONS
    except Exception:
        pass
    
    return DEFAULT_QUESTIONS

def create_questions_file():
    """Create a sample coaching_questions.txt file."""
    content = """=== Goal (SMART) ===
What specifically do you want to achieve? [Specific]
How will you measure your success? [Measurable]
Is this goal realistic with your current resources? [Achievable]
Why is this goal important to you right now? [Relevant]
By when do you want to accomplish this? [Time-bound]

=== Reality ===
What is your current situation regarding this goal?
What have you already tried?
What obstacles are you facing?
What resources do you currently have?

=== Options ===
What are all the possible ways you could approach this?
What would you do if you had unlimited resources?
Who could help you with this goal?
What alternatives exist if your first choice doesn't work?

=== Way Forward ===
What specific actions will you take?
When will you start each action?
What support do you need?
How will you track your progress?"""

    try:
        with open('coaching_questions.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Created coaching_questions.txt with default questions")
    except Exception as e:
        print(f"⚠️  Could not create coaching_questions.txt: {e}")

def run_flask_app():
    """Run the Flask application."""
    if not FLASK_AVAILABLE:
        print("❌ Flask is not installed!")
        print("\nTo install Flask, run:")
        print("   pip install flask")
        print("\nOr run this application with the --console flag for text-based coaching.")
        return False

    app = Flask(__name__)
    
    @app.route('/')
    def index():
        sections = load_questions_from_file()
        return render_template_string(HTML_TEMPLATE, sections=sections)
    
    @app.route('/download_direct', methods=['POST'])
    def download_direct():
        try:
            session_data_str = request.form.get('session_data')
            if not session_data_str:
                return "No session data provided", 400
            
            data = json.loads(session_data_str)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"coaching_session_report_{timestamp}.txt"
            
            report_content = "=== Blind Coaching Session Report ===\n"
            report_content += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            
            if 'goalStatement' in data and data['goalStatement'].strip():
                report_content += "🎯 GOAL STATEMENT\n"
                report_content += f"{data['goalStatement']}\n"
                report_content += "=" * 50 + "\n\n"
            
            for section in data['sections']:
                report_content += f"[{section['title']}]\n"
                for qa in section['answers']:
                    report_content += f"Q: {qa['question']}\n"
                    report_content += f"A: {qa['answer']}\n"
                    report_content += "\n"
                report_content += "\n"
            
            return Response(
                report_content,
                mimetype='text/plain',
                headers={
                    'Content-Disposition': f'attachment; filename={filename}'
                }
            )
            
        except Exception as e:
            return f"Error generating report: {str(e)}", 500
    
    # Open browser automatically
    def open_browser():
        time.sleep(1.5)
        webbrowser.open('http://localhost:5000')
    
    thread = threading.Thread(target=open_browser)
    thread.daemon = True
    thread.start()
    
    print("🎯 Starting Blind Coaching Application...")
    print("🌐 Opening browser at: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the application")
    
    try:
        app.run(host='localhost', port=5000, debug=False)
        return True
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        return False

def run_console_version():
    """Run a simplified console version of the coaching session."""
    print("🎯 Blind Coaching Session - Console Version")
    print("=" * 50)
    print("GROW Model with SMART Goal Setting\n")
    
    sections = load_questions_from_file()
    answers = []
    
    for section in sections:
        print(f"\n=== {section['title']} ===")
        section_answers = []
        
        for i, question in enumerate(section['questions'], 1):
            print(f"\n{i}. {question}")
            answer = input("Your answer: ").strip()
            section_answers.append((question, answer))
        
        answers.append((section['title'], section_answers))
    
    # Generate report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"coaching_session_report_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=== Blind Coaching Session Report ===\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for title, qa_pairs in answers:
                f.write(f"[{title}]\n")
                for question, answer in qa_pairs:
                    f.write(f"Q: {question}\n")
                    f.write(f"A: {answer}\n")
                    f.write("\n")
                f.write("\n")
        
        print(f"\n✅ Session complete! Report saved as: {filename}")
        
    except Exception as e:
        print(f"❌ Error saving report: {e}")

def main():
    """Main application entry point."""
    print("🎯 Blind Coaching Application")
    print("=" * 40)
    
    # Create questions file if it doesn't exist
    if not os.path.exists('coaching_questions.txt'):
        create_questions_file()
    
    # Check command line arguments
    if len(sys.argv) > 1 and '--console' in sys.argv:
        run_console_version()
        return
    
    # Try to run Flask version first
    if not run_flask_app():
        print("\n" + "=" * 40)
        print("Falling back to console version...")
        print("=" * 40)
        run_console_version()

if __name__ == "__main__":
    main()
