#!/usr/bin/env python3

"""
Web-based Blind Coaching Application using Flask
A web interface for the GROW model coaching session
"""

from flask import Flask, render_template, request, jsonify, send_file, Response
import json
import os
from datetime import datetime

app = Flask(__name__)

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
                    sections.append({"title": current_section, "questions": questions})
                # Start new section
                current_section = line[4:-4]  # Remove === and ===
                questions = []
            elif line and not line.startswith('==='):
                questions.append(line)
        
        # Add the last section
        if current_section:
            sections.append({"title": current_section, "questions": questions})
        
        return sections
    except FileNotFoundError:
        return [
            {"title": "Goal", "questions": ["Define your most important current objective. What do you want to achieve?"]},
            {"title": "Reality", "questions": ["Describe your current situation. What is happening now? What have you tried so far?"]},
            {"title": "Options", "questions": ["Brainstorm possible options. What could you do? What alternatives exist?"]},
            {"title": "Way Forward", "questions": ["Decide on your next steps. What will you do? When will you do it? What support do you need?"]}
        ]

@app.route('/')
def index():
    """Main coaching session page"""
    sections = load_questions()
    return render_template('coaching.html', sections=sections)

@app.route('/save_session', methods=['POST'])
def save_session():
    """Save the coaching session report"""
    try:
        data = request.json
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"coaching_session_report_{timestamp}.txt"
        filepath = os.path.join(os.getcwd(), filename)
        
        # Debug logging
        app.logger.info(f"Saving report to: {filepath}")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("=== Coaching Session Report ===\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for section in data['sections']:
                f.write(f"[{section['title']}]\n")
                for qa in section['answers']:
                    f.write(f"Q: {qa['question']}\n")
                    f.write(f"A: {qa['answer']}\n")
                    f.write("\n")
                f.write("\n")
        
        app.logger.info(f"Report saved successfully: {filename}")
        return jsonify({"success": True, "filename": filename})
    except Exception as e:
        app.logger.error(f"Error saving report: {str(e)}")
        return jsonify({"success": False, "error": str(e)})

@app.route('/download_direct', methods=['POST'])
def download_direct():
    """Direct download of coaching session report"""
    try:
        # Parse the session data from form
        session_data_str = request.form.get('session_data')
        if not session_data_str:
            return "No session data provided", 400
        
        data = json.loads(session_data_str)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"coaching_session_report_{timestamp}.txt"
        
        # Create report content
        report_content = "=== Coaching Session Report ===\n"
        report_content += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Add goal statement if present
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
        
        # Create response with file download
        return Response(
            report_content,
            mimetype='text/plain',
            headers={
                'Content-Disposition': f'attachment; filename={filename}'
            }
        )
        
    except Exception as e:
        app.logger.error(f"Error in direct download: {str(e)}")
        return f"Error generating report: {str(e)}", 500

@app.route('/test_download')
def test_download():
    """Test endpoint to verify download functionality"""
    try:
        test_content = "Test report content\nGenerated at: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        filename = "test_report.txt"
        filepath = os.path.join(os.getcwd(), filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(test_content)
        
        return send_file(
            filepath, 
            as_attachment=True, 
            download_name=filename,
            mimetype='text/plain'
        )
    except Exception as e:
        return f"Test download error: {e}", 500

@app.route('/download/<filename>')
def download_report(filename):
    """Download the coaching session report"""
    try:
        # Security check - only allow downloading report files
        if not filename.startswith('coaching_session_report_') or not filename.endswith('.txt'):
            return "Invalid filename", 400
        
        filepath = os.path.join(os.getcwd(), filename)
        app.logger.info(f"Attempting to download: {filepath}")
        
        if not os.path.exists(filepath):
            app.logger.error(f"File not found: {filepath}")
            return f"File not found: {filename}", 404
        
        return send_file(
            filepath, 
            as_attachment=True, 
            download_name=filename,
            mimetype='text/plain'
        )
    except Exception as e:
        app.logger.error(f"Error downloading file: {str(e)}")
        return f"Error downloading file: {e}", 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    print("Starting Blind Coaching Web Application...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='localhost', port=5000)
