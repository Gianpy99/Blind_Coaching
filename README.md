# 🎯 Blind Coaching Application

A professional coaching application based on the GROW model with SMART goal setting. Create comprehensive coaching sessions with intuitive web interface and customizable questions.

## 🚀 Quick Start

### Easiest Way - Use the Menu
```bash
START_HERE.bat
```
Choose option 1 to run the application immediately.

### Direct Launch Options

#### Option 1: Standalone Application (Recommended)
```bash
python blind_coaching_standalone.py
```

#### Option 2: Web Application
```bash
python web_app.py
```

#### Option 3: Console Version
```bash
python BlindCoaching.py
```

All versions open in your browser at: **http://localhost:5000**

## 📋 Features

### Complete GROW Model Implementation
- **🎯 Goal (SMART)**: Define specific, measurable, achievable, relevant, time-bound goals
- **📊 Reality**: Assess current situation, obstacles, and resources
- **💡 Options**: Explore possible approaches and alternatives  
- **🛣️ Way Forward**: Create detailed action plans with timelines and support needs

### Professional Features
- **Goal Statement Generator**: Creates concise "I will [goal] by [timeframe]" statements
- **Progress Tracking**: Visual progress indicators through each coaching phase
- **Session Reports**: Download comprehensive coaching session summaries
- **Customizable Questions**: Edit questions in `coaching_questions.txt`
- **Professional Design**: Clean, pastell orange themed interface
- **Responsive Layout**: Works on desktop, tablet, and mobile devices

## 🛠️ Installation

### Requirements
- Python 3.6 or higher
- Flask (automatically installed)

### One-Click Setup
```bash
pip install flask
python blind_coaching_standalone.py
```

### Create Standalone Executable
```bash
python build_executable.py
```
This creates `dist/BlindCoachingApp.exe` - runs on any Windows computer without Python!

## 📁 File Structure

### Core Application Files
- `blind_coaching_standalone.py` - **Main application** (recommended)
- `web_app.py` - Alternative Flask web application
- `BlindCoaching.py` - Original console version

### Configuration
- `coaching_questions.txt` - **Customizable coaching questions**
- `START_HERE.bat` - **User-friendly launcher menu**

### Build Tools
- `build_executable.py` - Creates Windows executable
- `BlindCoachingApp.spec` - PyInstaller configuration

### Documentation
- `README.md` - This file

## ✏️ Customizing Questions

### Edit Questions File
1. Use the menu: `START_HERE.bat` → Option 2
2. Or edit directly: `notepad coaching_questions.txt`

### Question File Format
```
=== Goal (SMART) ===
What specifically do you want to achieve? [Specific]
How will you measure your success? [Measurable]

=== Reality ===
What is your current situation regarding this goal?
What obstacles are you facing?
```

Questions are automatically loaded when you restart the application.

## 🎨 User Interface

### Coaching Process Flow
1. **Welcome Screen** - Introduction and overview
2. **Goal Setting** - SMART criteria with guided questions
3. **Reality Assessment** - Current situation analysis
4. **Options Exploration** - Brainstorming alternatives
5. **Way Forward** - Action planning and next steps
6. **Session Summary** - Download comprehensive report

### Key Interface Features
- **Progress Bar** - Shows completion status
- **Section Navigation** - Easy movement between coaching phases
- **Auto-Save** - Responses automatically preserved
- **Goal Statement Display** - Generated goal prominently shown
- **Professional Styling** - Clean, coaching-focused design

## 🚀 Distribution

### For End Users
1. **Portable**: Copy `blind_coaching_standalone.py` + `coaching_questions.txt`
2. **Executable**: Use `build_executable.py` to create `.exe` file
3. **Web-based**: No installation needed, runs in any modern browser

### For Developers
- **Single File**: All HTML, CSS, JavaScript embedded in Python
- **No Dependencies**: Only requires Flask
- **Cross-Platform**: Works on Windows, macOS, Linux
- **Extensible**: Easy to modify questions and styling

## 🔧 Technical Details

### Architecture
- **Backend**: Python Flask web server
- **Frontend**: Embedded HTML5/CSS3/JavaScript
- **Data**: JSON-based session storage
- **Deployment**: Self-contained single file or executable

### Browser Compatibility
- Chrome/Edge (recommended)
- Firefox
- Safari
- Any modern browser with JavaScript enabled

### Performance
- **Startup**: Instant (under 2 seconds)
- **Memory**: ~50-100MB RAM usage
- **Storage**: Session data stored in browser
- **Network**: Runs locally, no internet required

## 🆘 Troubleshooting

### Common Issues

#### "Python not found"
- Install Python from https://python.org
- Ensure "Add Python to PATH" is checked during installation

#### "Flask not installed"
```bash
pip install flask
```

#### Port 5000 already in use
- Stop other applications using port 5000
- Or modify the port in the Python file

#### Questions not loading
- Ensure `coaching_questions.txt` exists in the same directory
- Check file encoding is UTF-8

### Getting Help
1. Check this README file
2. Review the `coaching_questions.txt` format
3. Ensure Python and Flask are properly installed
4. Try the console version if web interface has issues

## 🎯 GROW Model Guide

### What is GROW?
GROW is a proven coaching methodology:
- **G**oal - What do you want to achieve?
- **R**eality - What's your current situation?
- **O**ptions - What could you do?
- **W**ay Forward - What will you do?

### Using This Application
1. **Set SMART Goals** - Be specific, measurable, achievable, relevant, time-bound
2. **Assess Reality** - Honestly evaluate your current situation
3. **Explore Options** - Brainstorm multiple approaches
4. **Plan Forward** - Choose specific actions with deadlines

### Best Practices
- Take your time with each section
- Be honest and thorough in your responses
- Save your session reports for future reference
- Review and update your goals regularly

## 📄 License

This project is open source. Feel free to modify and distribute as needed.

---

**Ready to start coaching?** Run `START_HERE.bat` and choose option 1!
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