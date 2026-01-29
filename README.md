# AI & Digital Innovation Hub Website

A Python Flask-based website for the AI & Digital Innovation Hub, featuring information about services, the PACS project, and contact functionality.

## 🚀 Features

- **Home Page**: Overview of the hub with hero section and stats
- **About Page**: Mission, vision, and values
- **Services Page**: Detailed information about all services offered
- **PACS Project Page**: Showcase of the AI-Powered PACS for Brain Hemorrhage Detection
- **Contact Page**: Contact form and information
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Professional dark theme with animations

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

## 🛠️ Installation

### Step 1: Download the Website Files

Save all the website files to a folder on your computer (e.g., `ai-hub-website`)

### Step 2: Open Terminal/Command Prompt

- **Windows**: Press `Win + R`, type `cmd`, and press Enter
- **Mac/Linux**: Open Terminal from Applications

### Step 3: Navigate to Your Website Folder

```bash
cd path/to/ai-hub-website
```

For example:
```bash
cd C:\Users\YourName\Documents\ai-hub-website
```

### Step 4: Install Required Packages

```bash
pip install -r requirements.txt
```

This will install Flask and other necessary packages.

## ▶️ Running the Website

### Method 1: Simple Run (Recommended for Beginners)

Just run this command in your terminal:

```bash
python app.py
```

### Method 2: With Custom Settings

You can also run it with custom host and port:

```bash
python app.py
```

The website will start and you'll see something like:
```
 * Running on http://127.0.0.1:5000
```

### Step 5: Open in Browser

Open your web browser and go to:
```
http://localhost:5000
```

Or:
```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
ai-hub-website/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── index.html             # Home page
│   ├── about.html             # About page
│   ├── services.html          # Services page
│   ├── pacs.html              # PACS project page
│   └── contact.html           # Contact page
└── static/                     # Static files
    ├── css/
    │   └── style.css          # Stylesheet
    ├── js/
    │   └── main.js            # JavaScript
    └── images/                # Place your images here
```

## 🎨 Customization

### Changing Colors

Edit `static/css/style.css` and modify the color variables at the top:

```css
:root {
    --primary: #0A84FF;      /* Main blue color */
    --secondary: #00D9FF;    /* Secondary blue */
    --accent: #FF6B35;       /* Orange accent */
    --success: #00F5A0;      /* Green for success */
}
```

### Updating Content

Edit the HTML files in the `templates/` folder:

- `index.html` - Home page content
- `about.html` - About page content
- `services.html` - Services information
- `pacs.html` - PACS project details
- `contact.html` - Contact information

### Adding Your Logo

1. Place your logo image in `static/images/`
2. Edit `templates/base.html` and replace the logo text with:

```html
<div class="logo">
    <img src="{{ url_for('static', filename='images/your-logo.png') }}" alt="AI Hub">
</div>
```

### Updating Contact Information

Edit `templates/contact.html` and `templates/base.html` (footer section) to update:
- Email address
- Phone number
- Physical address
- Working hours

## 📧 Setting Up Email Functionality

To make the contact form send actual emails:

1. Open `app.py`
2. Find the contact route function
3. Add email sending code using Gmail, SendGrid, or your preferred email service

Example with Gmail:

```python
import smtplib
from email.mime.text import MIMEText

# In the contact route:
sender_email = "your-email@gmail.com"
sender_password = "your-app-password"
receiver_email = "info@aihub.com"

msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
msg['Subject'] = 'New Contact Form Submission'
msg['From'] = sender_email
msg['To'] = receiver_email

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)
```

## 🌐 Deploying to the Internet

### Option 1: PythonAnywhere (Free & Easy)

1. Sign up at https://www.pythonanywhere.com
2. Upload your files
3. Follow their Flask deployment guide

### Option 2: Heroku (Free Tier Available)

1. Sign up at https://www.heroku.com
2. Install Heroku CLI
3. Create a `Procfile`:
   ```
   web: python app.py
   ```
4. Deploy using Git

### Option 3: Render (Modern & Free)

1. Sign up at https://render.com
2. Connect your GitHub repository
3. Deploy with one click

## 🔧 Troubleshooting

### "Python is not recognized"

Install Python from https://www.python.org/downloads/

### "pip is not recognized"

Add Python to your PATH or use:
```bash
python -m pip install -r requirements.txt
```

### Port Already in Use

Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Use 8080 instead
```

### Can't Access from Other Devices

Make sure you're using `host='0.0.0.0'` in `app.py` and access via:
```
http://YOUR-COMPUTER-IP:5000
```

## 📱 Testing on Mobile

1. Make sure your computer and phone are on the same WiFi network
2. Find your computer's IP address:
   - Windows: `ipconfig` in cmd
   - Mac/Linux: `ifconfig` in terminal
3. On your phone, browse to: `http://YOUR-IP:5000`

## 🆘 Need Help?

If you encounter any issues:

1. Make sure Python is installed: `python --version`
2. Make sure Flask is installed: `pip list | grep Flask`
3. Check that all files are in the correct folders
4. Read error messages carefully - they usually tell you what's wrong

## 📝 Notes for Non-Developers

- You don't need to understand the code to use this website
- Just follow the installation steps above
- To make changes, edit the HTML files in the `templates` folder
- Colors and styling are in `static/css/style.css`
- The website will only work when `app.py` is running
- To stop the website, press `Ctrl+C` in the terminal

## 🎓 Learning Resources

If you want to learn more about Flask:
- Official Flask Tutorial: https://flask.palletsprojects.com/tutorial/
- Flask Mega-Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## 📄 License

This website was created for AI & Digital Innovation Hub.

---

**Built with Python Flask** 🐍
