# Pavan Gadireddy — Data Engineering Portfolio

A single-page professional portfolio for a Data Engineer / ETL Developer, built
with Python and Flask. Content is sourced entirely from the resume — no
invented employers, dates, skills, or metrics.

## Overview

The site presents a resume-driven portfolio covering a professional summary,
categorized technical skills, work experience, project case studies,
education, certifications, and contact details. All page content lives in a
single Python dictionary in `app.py`, rendered through Jinja2 templates, so
the site can be updated without editing HTML.

## Features

- Single-page layout with sticky navigation and scroll-based active-link
  highlighting
- Dark navy/slate visual theme with an azure-blue accent, built for a data
  engineering audience
- Resume download endpoint (`/resume`)
- Fully responsive layout (desktop, tablet, mobile)
- No fabricated metrics, testimonials, skill-percentage bars, or stock photos
- No client-confidential details — project case studies are described at a
  business-problem level only

## Technology Stack

- **Backend:** Python 3, Flask
- **Templating:** Jinja2
- **Frontend:** HTML5, CSS3 (custom, no framework), vanilla JavaScript
- **No** React/Angular/Vue/Node.js, and **no** database — content is static
  Python data

## Folder Structure

```
portfolio/
├── app.py                     # Flask app + all resume-derived content
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   ├── images/
│   └── resume/
│       └── Pavan_Gadireddy_Resume.docx
└── templates/
    ├── base.html               # Shared layout, nav, footer
    └── index.html              # All page sections
```

## Windows Setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate it

```powershell
.venv\Scripts\Activate.ps1
```

> If PowerShell blocks script execution, run
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first, or
> activate with `.venv\Scripts\activate.bat` from `cmd.exe` instead.

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the application

```powershell
python app.py
```

The site will be available at **http://127.0.0.1:5000**.

### Optional: override the port

```powershell
$env:PORT = "8000"
python app.py
```

### Optional: enable debug mode (development only)

```powershell
$env:FLASK_DEBUG = "true"
python app.py
```

Debug mode is **off by default** — do not set `FLASK_DEBUG=true` in
production.

## Deployment Notes

The app reads `PORT` from the environment and binds to `0.0.0.0`, so it is
compatible with most Python-friendly hosts (Render, Railway, Fly.io, Azure App
Service, PythonAnywhere, Heroku-style platforms). For a production
deployment:

1. Use a production WSGI server instead of Flask's built-in dev server, e.g.
   `pip install gunicorn` and run `gunicorn app:app` (Linux-based hosts), or
   `waitress` on Windows-based hosts.
2. Leave `FLASK_DEBUG` unset (or `false`) in production.
3. Set the platform's `PORT` environment variable as required by the host.

## Customization

- **Content:** edit the `PORTFOLIO` dictionary in [`app.py`](app.py) —
  skills, experience, projects, education, and certifications are all plain
  Python lists/dicts.
- **GitHub link:** `data.github_url` is left blank because no GitHub profile
  URL was present on the source resume. Add it in `app.py` once available.
- **Resume file:** replace
  `static/resume/Pavan_Gadireddy_Resume.docx` with an updated copy (keep the
  same filename, or update `RESUME_FILENAME` in `app.py`).
- **Styling:** colors and spacing are defined as CSS custom properties at the
  top of `static/css/style.css` under `:root`.
- **Sections:** each section in `templates/index.html` is a self-contained
  `<section>` block — remove or reorder as needed, and update the nav links
  in `templates/base.html` to match.

## Privacy Notes

- Only city/state-level location is shown (no street address).
- Phone number from the source resume is intentionally omitted from the
  public site; recruiters can reach out via email or LinkedIn.
- Project case studies describe business problems and outcomes without
  disclosing client-confidential data.
