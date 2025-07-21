# Blind Coaching Application

A self-guided coaching application based on the GROW model with SMART goal setting.

## Available Versions

### 1. Console Version (`BlindCoaching.py`)
Traditional command-line interface for coaching sessions.

### 2. Web Version (`web_app.py`) - **Recommended**
Modern web-based interface with better user experience.

## Quick Start - Web Version

1. **Install Requirements**
   ```bash
   pip install flask
   ```

2. **Start the Web Application**
   ```bash
   python web_app.py
   ```

3. **Open Your Browser**
   Navigate to: `http://localhost:5000`

4. **Follow the Enhanced GROW Process**
   - **Goal (SMART)**: Define specific, measurable, achievable, relevant, time-bound objectives
   - **Goal Recap & Statement**: Review your goals and create a clear, actionable goal statement
   - **Reality**: Assess your current situation (with goal reminder)
   - **Options**: Explore possible approaches (with goal reminder)
   - **Will**: Create your action plan (with goal reminder)

## Features

- ✅ **Interactive Web Interface**: Modern, responsive design with gradient animations
- ✅ **Enhanced GROW Process**: 5-step process with goal recap and statement creation
- ✅ **Goal Statement & Reminder**: Create a clear goal statement that appears throughout the session
- ✅ **Progress Tracking**: Visual progress bar through sessions
- ✅ **Customizable Questions**: Edit `coaching_questions.txt` to personalize
- ✅ **Report Generation**: Automatic session reports with timestamps and goal statement
- ✅ **Download Reports**: Save your coaching sessions as text files
- ✅ **SMART Goal Focus**: Structured approach to goal setting with reflection phase
- ✅ **Goal Review System**: Edit and refine your goals before proceeding
- ✅ **Debug Tools**: Built-in debugging for troubleshooting

## Workflow & User Experience

### Enhanced 5-Step Process

1. **Goal Definition (SMART)**: Answer structured questions to define your objectives
2. **Goal Recap & Statement**: Review your answers and create a one-sentence goal statement
3. **Reality Assessment**: Evaluate your current situation with your goal always visible
4. **Options Exploration**: Brainstorm approaches with goal reminder at the top
5. **Action Planning**: Define concrete next steps with goal context

### Key User Experience Features

- **Auto-Generated Goal Statement**: The app intelligently combines your SMART answers into a coherent goal statement
- **Editable Goal Statement**: Refine and customize your goal statement before proceeding
- **Persistent Goal Reminder**: Your goal statement appears at the top of each subsequent section
- **Seamless Navigation**: Move between sections with clear progress indicators
- **Instant Goal Editing**: Quick access to modify your goal statement from any section

## Customization

Edit `coaching_questions.txt` to customize the coaching questions:

```
=== Goal (SMART) ===
What specifically do you want to achieve?
How will you measure your success?
...

=== Reality ===
What is your current situation?
...
```

## File Structure

```
Blind_Coaching/
├── web_app.py              # Web application (Flask)
├── BlindCoaching.py         # Console version
├── coaching_questions.txt   # Customizable questions
├── templates/
│   └── coaching.html       # Web interface template
└── coaching_session_report_*.txt  # Generated reports
```

## Usage Tips

1. **Take Your Time**: There's no rush - reflect deeply on each question
2. **Be Honest**: The more honest you are, the more effective the coaching
3. **Perfect Your Goal Statement**: Use the recap phase to create a clear, actionable goal
4. **Use the Goal Reminder**: Let your goal statement guide you through Reality, Options, and Will
5. **Review Reports**: Keep your reports to track progress over time
6. **Customize Questions**: Adapt the questions to your specific needs
7. **Regular Sessions**: Consider weekly or monthly coaching sessions
8. **Edit as Needed**: Use the quick edit button to refine your goal during the session

## Sample Report Format

```
=== Coaching Session Report ===
Date: 2025-07-21 20:30:15

🎯 GOAL STATEMENT
I will increase my monthly revenue by 25% within the next 6 months by implementing a new marketing strategy and improving customer retention.
==================================================

[Goal (SMART)]
Q: What specifically do you want to achieve?
A: Increase monthly revenue by 25%

Q: How will you measure your success?
A: Monthly revenue reports and customer metrics
...

[Reality]
Q: What is your current situation regarding this goal?
A: Currently at $10,000 monthly revenue...
...
```

## Technical Notes

- **Port**: Web app runs on `localhost:5000`
- **File Encoding**: UTF-8 for international character support
- **Browser Compatibility**: Works with all modern browsers
- **Offline Capable**: No internet connection required after setup
- **Auto-Save**: Goal statements and answers are preserved during navigation
- **Debug Mode**: Built-in debugging tools for troubleshooting
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Troubleshooting

### Download Issues
- Use the "🧪 Test Download" button to verify download functionality
- Check browser download settings and permissions
- Use the "🔍 Debug" button to inspect form data

### Goal Reminder Not Showing
- Ensure you've completed the Goal section
- Create a goal statement in the recap phase
- The reminder only appears in Reality, Options, and Will sections

### Questions Not Loading
- Check that `coaching_questions.txt` exists in the project directory
- Verify the file format matches the expected structure
- The app will fall back to default questions if the file is missing