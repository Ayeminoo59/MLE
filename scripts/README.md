# Professional CV Builder

A beautiful, modern CV builder application with a stunning UI and full functionality.

## Features

- **Modern Design**: Beautiful gradient backgrounds, smooth animations, and professional styling
- **Complete CV Form**: Personal information, work experience, education, and skills sections
- **Dynamic Form Fields**: Add/remove multiple experiences and education entries
- **Interactive Skills Management**: Add technical skills, soft skills, and languages with tags
- **Live Preview**: Preview your CV in real-time before downloading
- **PDF Generation**: Download professional PDF resumes (requires wkhtmltopdf)
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Form Validation**: Client-side validation for required fields
- **Print Support**: Optimized printing layout

## Technology Stack

- **Frontend**: HTML5, TailwindCSS, JavaScript (Vanilla)
- **Backend**: Python Flask
- **PDF Generation**: pdfkit + wkhtmltopdf
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)

## Installation

### Prerequisites

1. Python 3.7+
2. wkhtmltopdf (for PDF generation)

### Install wkhtmltopdf

**macOS:**
```bash
brew install wkhtmltopdf
```

**Ubuntu/Debian:**
```bash
sudo apt-get install wkhtmltopdf
```

**Windows:**
Download and install from [https://wkhtmltopdf.org/](https://wkhtmltopdf.org/)

### Setup the Application

1. Clone or download the project files
2. Navigate to the scripts directory:
```bash
cd /Users/ayeminoo/Desktop/MLE/scripts
```

3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create templates directory:
```bash
mkdir templates
cp cv.html templates/
```

## Usage

### Running the Application

1. Start the Flask server:
```bash
python cv_form.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

### Using the CV Builder

1. **Fill in Personal Information**: Enter your name, contact details, and professional summary
2. **Add Work Experience**: Click "Add Experience" to add multiple job entries
3. **Add Education**: Click "Add Education" to add your academic background
4. **Manage Skills**: Add technical skills, soft skills, and languages using the tag system
5. **Preview**: Click "Preview" to see how your CV will look
6. **Generate PDF**: Click "Generate CV" to create and download your PDF resume

## Features in Detail

### Personal Information
- Full name, professional title, email, phone
- Location and portfolio/LinkedIn links
- Professional summary textarea

### Work Experience
- Dynamic addition/removal of experience entries
- Fields for job title, company, location, duration
- Description textarea for each role

### Education
- Dynamic addition/removal of education entries
- Fields for degree, institution, location, duration
- Description textarea for additional details

### Skills Management
- Three categories: Technical Skills, Soft Skills, Languages
- Tag-based interface with add/remove functionality
- Visual feedback with hover effects

### Preview System
- Real-time CV preview in modal window
- Professional formatting with clean layout
- Print and download options

## File Structure

```
scripts/
├── cv.html              # Main HTML file (move to templates/)
├── cv_script.js         # JavaScript functionality
├── cv_form.py           # Flask backend
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Customization

### Styling
The application uses TailwindCSS for styling. You can modify the colors and layout by editing the CSS classes in `cv.html`.

### PDF Layout
Modify the `create_cv_html()` function in `cv_form.py` to customize the PDF output format.

### Form Fields
Add new form fields by updating the HTML structure and corresponding JavaScript validation.

## Troubleshooting

### PDF Generation Issues
If PDF generation fails:
1. Ensure wkhtmltopdf is properly installed
2. Check that wkhtmltopdf is in your system PATH
3. Try running `wkhtmltopdf --version` to verify installation

### Port Issues
If port 5000 is already in use, modify the port in `cv_form.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Change to 8080
```

## Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the design
- Fixing bugs
- Enhancing documentation

## License

This project is open source and available under the MIT License.
