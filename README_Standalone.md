# Blind Coaching Standalone Application

A complete, self-contained coaching application based on the GROW model that can be distributed as a standalone executable.

## 🚀 Quick Start

### Option 1: Python Script (Requires Python)
```bash
python blind_coaching_standalone.py
```

### Option 2: Standalone Executable (No Python Required)
1. Run `python build_executable.py` to create the executable
2. Distribute `dist/BlindCoachingApp.exe` - no Python installation needed!

### Option 3: Console Version
```bash
python blind_coaching_standalone.py --console
```

## 📋 Features

### Complete GROW Model Implementation
- **Goal (SMART)**: Define specific, measurable, achievable, relevant, time-bound goals
- **Reality**: Assess current situation and obstacles
- **Options**: Explore possible approaches and alternatives  
- **Way Forward**: Create action plans with timelines and support needs

### Advanced User Experience
- **Goal Statement Generator**: Creates concise goal statements with "I will [goal] by [timeframe]" format
- **Goal Reminder Banner**: Shows your goal statement throughout the session
- **Progress Tracking**: Visual progress bar and section indicators
- **Session Reports**: Downloadable text reports with all answers
- **Responsive Design**: Works on desktop, tablet, and mobile devices

### Professional Interface
- **Pastell Orange Theme**: Warm, professional color scheme
- **Smooth Animations**: Gradient backgrounds and hover effects
- **Clean Typography**: Easy-to-read fonts and spacing
- **Accessible Design**: High contrast and screen reader friendly

### Flexible Deployment
- **Web Interface**: Flask-based web application
- **Standalone Executable**: No Python installation required
- **Console Version**: Text-based fallback option
- **Customizable Questions**: External question file support

## 🛠 Installation & Setup

### Requirements
- Python 3.7+ (for script version)
- Flask (automatically installed)
- PyInstaller (for executable creation)

### Creating Standalone Executable

1. **Install dependencies:**
   ```bash
   pip install flask pyinstaller
   ```

2. **Build executable:**
   ```bash
   python build_executable.py
   ```

3. **Distribute the executable:**
   - Copy `dist/BlindCoachingApp.exe` to any Windows computer
   - Run the executable - it will open in the default browser
   - No Python installation required on target machines!

### Customizing Questions

Create or edit `coaching_questions.txt` with this format:
```
=== Section Name ===
Question 1
Question 2
Question 3

=== Another Section ===
More questions here
```

## 💼 Business Use Cases

### For Coaches and Consultants
- **Professional Tool**: Ready-to-use coaching platform for client sessions
- **Branded Experience**: Customizable questions and reports
- **Portable Solution**: Runs on any Windows computer without setup
- **Session Documentation**: Automatic report generation for records

### For Organizations
- **Employee Development**: Self-coaching tool for goal setting
- **Training Programs**: Structured approach to personal development
- **Performance Management**: Goal tracking and action planning
- **Remote Work**: Web-based accessibility for distributed teams

### For Personal Use
- **Goal Setting**: Structured approach to defining and achieving goals
- **Self-Reflection**: Guided questions for personal development
- **Progress Tracking**: Visual progress and downloadable reports
- **Decision Making**: Systematic exploration of options and next steps

## 🔧 Technical Details

### Architecture
- **Frontend**: HTML5, CSS3, JavaScript (embedded in Python)
- **Backend**: Flask web framework
- **Storage**: File-based (no database required)
- **Distribution**: PyInstaller for executable creation

### File Structure
```
blind_coaching_standalone.py    # Main application
build_executable.py            # Executable builder
coaching_questions.txt         # Question configuration (optional)
dist/BlindCoachingApp.exe     # Generated executable
```

### Security Features
- **Local Execution**: No data sent to external servers
- **File-based Storage**: All data remains on local machine
- **No Network Dependencies**: Works offline after initial download

## 📖 Usage Instructions

### Web Interface Workflow
1. **Start Application**: Run the executable or Python script
2. **Define Goal**: Answer SMART goal questions in first section
3. **Review Goal**: See generated goal statement and summary
4. **Assess Reality**: Evaluate current situation and obstacles
5. **Explore Options**: Brainstorm approaches and alternatives
6. **Plan Actions**: Define specific next steps and timelines
7. **Download Report**: Get complete session documentation

### Console Version
- Use `--console` flag for text-based interaction
- Suitable for environments without web browser access
- Same GROW model process with command-line interface

## 🔄 Updates and Maintenance

### Updating Questions
- Edit `coaching_questions.txt` to modify coaching questions
- Restart application to load new questions
- Questions are loaded dynamically at startup

### Version Control
- All configuration in external files
- Easy to version control question sets
- Portable across different environments

## 🆘 Troubleshooting

### Common Issues
- **Flask not found**: Run `pip install flask`
- **PyInstaller errors**: Ensure all dependencies installed
- **Browser not opening**: Manually navigate to http://localhost:5000
- **Questions not loading**: Check `coaching_questions.txt` format

### Support
- Check error messages in console output
- Verify Python version compatibility (3.7+)
- Ensure all required packages installed
- Test with default questions first

## 📄 License

This is a standalone application designed for coaching and personal development use. Modify and distribute according to your needs.

## 🎯 About the GROW Model

The GROW model is a proven coaching framework:
- **Goal**: What do you want to achieve?
- **Reality**: What is your current situation?
- **Options**: What could you do?
- **Will/Way Forward**: What will you do?

This application implements GROW with SMART goal setting (Specific, Measurable, Achievable, Relevant, Time-bound) for maximum effectiveness.
