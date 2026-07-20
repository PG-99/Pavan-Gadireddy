Pavan Gadireddy — Data Engineering Portfolio

A professional single-page portfolio website developed using Python, Flask, Jinja2, HTML, CSS, and JavaScript. I built this project to showcase my experience as a Data Engineer and ETL Developer in a structured, interactive, and recruiter-friendly format.

Claude Code was used as an AI-assisted development tool to help generate the initial project structure, review code, improve the user interface, troubleshoot issues, and refine the documentation. I reviewed, customized, tested, and managed the complete project using my Python, Flask, Git, and GitHub skills.

Overview
The portfolio presents my professional background, technical skills, work experience, project case studies, education, certifications, and contact information.

All portfolio content is stored in a Python dictionary inside app.py and rendered dynamically through Jinja2 templates. This makes the website easy to maintain and update without editing multiple HTML sections.

My Contributions
Defined the portfolio requirements and website structure
Organized resume content into structured Python data
Built and configured the Flask application
Customized the Jinja2 templates
Reviewed and updated the HTML, CSS, and JavaScript
Added professional experience, skills, projects, education, and certifications
Configured resume download functionality
Added LinkedIn, GitHub, email, and location details
Tested the application locally
Troubleshot Python virtual environment and Flask issues
Managed the project using Git and GitHub
Prepared the application for production deployment
Used Claude Code to accelerate development, debugging, and code refinement

Features
Professional single-page portfolio layout
Sticky navigation bar
Scroll-based active navigation highlighting
Fully responsive design for desktop, tablet, and mobile
Dark navy and slate theme with Azure-blue accents
Resume download functionality
Dynamic content rendering using Flask and Jinja2
Categorized technical skills
Professional experience timeline
Project case studies based on real experience
Education and certification sections
Clickable email, LinkedIn, and GitHub links
Clean and accessible user interface
No fabricated employers, dates, achievements, or technical metrics
No database or unnecessary frontend framework dependencies

Technology Stack
Programming Language: Python 3
Backend Framework: Flask
Templating Engine: Jinja2
Frontend: HTML5, CSS3, Vanilla JavaScript
Version Control: Git and GitHub
Development Environment: Visual Studio Code
AI-Assisted Development: Claude Code
Production Server: Gunicorn

Folder Structure
portfolio/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── images/
│   └── resume/
│       └── Pavan_Gadireddy_Resume.docx
└── templates/
    ├── base.html
    └── index.html

File Responsibilities
app.py — Flask application, routes, configuration, and portfolio content
templates/base.html — Shared page layout, navigation, metadata, and footer
templates/index.html — Main portfolio sections
static/css/style.css — Layout, typography, colors, and responsive styling
static/js/main.js — Navigation behavior and frontend interactions
static/images/ — Profile image and other website assets
static/resume/ — Downloadable resume
requirements.txt — Required Python packages
.gitignore — Files and folders excluded from Git tracking
README.md — Project documentation and setup instructions

Local Setup

1. Clone the repository
git clone https://github.com/PG-99/Pavan_Gadireddy_Portfolio.git

2. Open the project folder
cd Pavan_Gadireddy_Portfolio

3. Create a virtual environment
python -m venv .venv

4. Activate the virtual environment
.\.venv\Scripts\Activate.ps1
If PowerShell blocks script execution, run:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Then activate the environment again:
.\.venv\Scripts\Activate.ps1

5. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

6. Run the application
python app.py
Open the website in a browser:
http://127.0.0.1:5000
To stop the application, press:
Ctrl + C

Environment Configuration
Change the port
$env:PORT = "8000"
python app.py
The website will then be available at:
http://127.0.0.1:8000

Enable debug mode
Use debug mode only during local development:
$env:FLASK_DEBUG = "true"
python app.py
Debug mode is disabled by default and should remain disabled in production.

Deployment
The application reads the PORT environment variable and binds to 0.0.0.0, making it compatible with Python-supporting platforms such as Render, Railway, Azure App Service, PythonAnywhere, Fly.io, and other Flask-compatible hosting services.
For Linux-based deployment, use Gunicorn:
gunicorn app:app
Typical deployment settings:
Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app

Customization

Update portfolio content
Edit the PORTFOLIO dictionary inside:
app.py
The dictionary contains:
Name
Professional title
Summary
Skills
Work experience
Projects
Education
Certifications
Email
LinkedIn
GitHub
Location

Update the GitHub link
In app.py, update:
"github_url": "https://github.com/PG-99"

Update the resume
Replace the resume file inside:
static/resume/
If the filename changes, update:
RESUME_FILENAME = "Pavan_Gadireddy_Resume.docx"
A PDF version is recommended for better browser compatibility.

Update the profile picture
Place the profile image inside:
static/images/
Reference it using:
{{ url_for('static', filename='images/pavan-profile.jpg') }}

Update the design
Modify:
static/css/style.css
The primary colors, spacing, typography, and component styles are defined under the :root section.

Git Workflow
After making changes:
git status
git add .
git commit -m "Update portfolio content and design"
git push

Privacy and Content Standards
Only city and state-level location information is displayed
Full residential address is excluded
Immigration and identification information is not published
Employer-confidential information is omitted
Project descriptions remain at the business and technical-solution level
No unsupported employers, dates, achievements, or metrics are included
Sensitive files and environment variables are excluded through .gitignore

Development Approach
This project demonstrates my ability to combine Python web development with modern AI-assisted development workflows.
Claude Code supported the project by helping with:
Initial project scaffolding
Python and Flask code suggestions
HTML and CSS improvements
Responsive design refinement
Troubleshooting and debugging
Documentation
Deployment preparation

I remained responsible for defining the requirements, reviewing the implementation, validating the content, modifying the source code, testing the application, managing version control, and publishing the project.
Future Enhancements
Deploy the application with a public production URL
Replace the resume with a PDF version
Add additional independent data engineering projects
Add links to individual project repositories
Add automated Flask route tests
Add CI/CD using GitHub Actions
Improve SEO and social-sharing metadata
Add a custom domain
Add privacy-friendly analytics

Author
Pavan Gadireddy
Data Engineer | ETL Developer | Master Data Management | Data Quality and Integration
GitHub: https://github.com/PG-99
LinkedIn: https://www.linkedin.com/in/pavan-gadireddy/

Acknowledgment
This portfolio was developed using Python, Flask, Jinja2, HTML, CSS, JavaScript, Git, and GitHub. Claude Code was used as an AI-assisted coding tool to support development, debugging, documentation, and code refinement.
