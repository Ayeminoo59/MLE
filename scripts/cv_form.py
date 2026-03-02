from flask import Flask, render_template, request, jsonify, send_file
import pdfkit
import tempfile
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cv.html')

@app.route('/generate-cv', methods=['POST'])
def generate_cv():
    try:
        data = request.get_json()
        
        # Generate HTML for CV
        cv_html = create_cv_html(data)
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(cv_html)
            temp_html_path = f.name
        
        # Convert to PDF
        temp_pdf_path = temp_html_path.replace('.html', '.pdf')
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        
        pdfkit.from_file(temp_html_path, temp_pdf_path, options=options)
        
        # Clean up HTML file
        os.unlink(temp_html_path)
        
        return send_file(temp_pdf_path, as_attachment=True, download_name=f'CV_{data["personal"]["fullName"].replace(" ", "_")}_{datetime.now().strftime("%Y%m%d")}.pdf')
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        # Clean up PDF file after sending
        if 'temp_pdf_path' in locals() and os.path.exists(temp_pdf_path):
            os.unlink(temp_pdf_path)

def create_cv_html(data):
    """Generate HTML for CV from form data"""
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>CV - {data['personal']['fullName']}</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background: white;
            }}
            .header {{
                border-bottom: 3px solid #667eea;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }}
            .name {{
                font-size: 28px;
                font-weight: bold;
                margin: 0 0 5px 0;
                color: #2c3e50;
            }}
            .title {{
                font-size: 18px;
                color: #7f8c8d;
                margin: 0 0 15px 0;
            }}
            .contact-info {{
                font-size: 12px;
                color: #555;
            }}
            .section {{
                margin-bottom: 25px;
            }}
            .section-title {{
                font-size: 18px;
                font-weight: bold;
                color: #2c3e50;
                border-bottom: 2px solid #667eea;
                padding-bottom: 5px;
                margin-bottom: 15px;
            }}
            .item {{
                margin-bottom: 15px;
            }}
            .item-title {{
                font-weight: bold;
                font-size: 14px;
            }}
            .item-subtitle {{
                font-style: italic;
                color: #555;
                font-size: 13px;
            }}
            .item-date {{
                float: right;
                font-size: 12px;
                color: #666;
            }}
            .item-description {{
                font-size: 12px;
                margin-top: 5px;
            }}
            .skills-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
            }}
            .skill-category {{
                margin-bottom: 10px;
            }}
            .skill-category-title {{
                font-weight: bold;
                font-size: 13px;
                color: #2c3e50;
                margin-bottom: 5px;
            }}
            .skill-list {{
                font-size: 12px;
                color: #555;
            }}
            .summary {{
                font-size: 13px;
                line-height: 1.5;
                text-align: justify;
            }}
            @media print {{
                body {{
                    margin: 0;
                    padding: 10px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1 class="name">{data['personal']['fullName']}</h1>
            <p class="title">{data['personal'].get('title', '')}</p>
            <div class="contact-info">
                {format_contact_info(data['personal'])}
            </div>
        </div>
    """
    
    # Professional Summary
    if data['personal'].get('summary'):
        html += f"""
        <div class="section">
            <h2 class="section-title">Professional Summary</h2>
            <p class="summary">{data['personal']['summary']}</p>
        </div>
        """
    
    # Work Experience
    if data.get('experience'):
        html += """
        <div class="section">
            <h2 class="section-title">Work Experience</h2>
        """
        for exp in data['experience']:
            html += f"""
            <div class="item">
                <div class="item-title">{exp['title']}</div>
                <div class="item-subtitle">{exp['company']}</div>
                <div class="item-date">{exp.get('duration', '')}</div>
                {f'<div class="item-description">{exp["description"]}</div>' if exp.get('description') else ''}
            </div>
            """
        html += "</div>"
    
    # Education
    if data.get('education'):
        html += """
        <div class="section">
            <h2 class="section-title">Education</h2>
        """
        for edu in data['education']:
            html += f"""
            <div class="item">
                <div class="item-title">{edu['degree']}</div>
                <div class="item-subtitle">{edu['institution']}</div>
                <div class="item-date">{edu.get('duration', '')}</div>
                {f'<div class="item-description">{edu["description"]}</div>' if edu.get('description') else ''}
            </div>
            """
        html += "</div>"
    
    # Skills
    skills = data.get('skills', {})
    if any(skills.values()):
        html += """
        <div class="section">
            <h2 class="section-title">Skills</h2>
            <div class="skills-grid">
        """
        
        if skills.get('technical'):
            html += f"""
            <div class="skill-category">
                <div class="skill-category-title">Technical Skills</div>
                <div class="skill-list">{', '.join(skills['technical'])}</div>
            </div>
            """
        
        if skills.get('soft'):
            html += f"""
            <div class="skill-category">
                <div class="skill-category-title">Soft Skills</div>
                <div class="skill-list">{', '.join(skills['soft'])}</div>
            </div>
            """
        
        if skills.get('language'):
            html += f"""
            <div class="skill-category">
                <div class="skill-category-title">Languages</div>
                <div class="skill-list">{', '.join(skills['language'])}</div>
            </div>
            """
        
        html += "</div></div>"
    
    html += """
    </body>
    </html>
    """
    
    return html

def format_contact_info(personal):
    """Format contact information"""
    contact_parts = []
    
    if personal.get('email'):
        contact_parts.append(f"📧 {personal['email']}")
    if personal.get('phone'):
        contact_parts.append(f"📱 {personal['phone']}")
    if personal.get('location'):
        contact_parts.append(f"📍 {personal['location']}")
    if personal.get('portfolio'):
        contact_parts.append(f"🌐 {personal['portfolio']}")
    
    return " | ".join(contact_parts)

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)