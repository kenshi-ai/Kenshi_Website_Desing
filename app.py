from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Services page
@app.route('/services')
def services():
    return render_template('services.html')

# Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# PACS Project page
@app.route('/pacs')
def pacs():
    return render_template('pacs.html')

# Contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Compose email
        body = f"New contact form submission from Kenshi.AI website:\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg = MIMEText(body)
        msg["Subject"] = "New contact request - Kenshi.AI website"

        # Sender credentials from environment (recommended for security)
        smtp_user = os.environ.get("KENSHI_EMAIL_USER")
        smtp_password = os.environ.get("KENSHI_EMAIL_PASSWORD")
        from_addr = smtp_user
        to_addr = "kenshi.ltd@gmail.com"

        if smtp_user and smtp_password:
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(smtp_user, smtp_password)
                    server.sendmail(from_addr, [to_addr], msg.as_string())
            except Exception as e:
                # Fallback to console logging if email fails
                print("Failed to send contact email:", e)
                print(body)
        else:
            # If SMTP is not configured yet, log to console for now
            print("KENSHI_EMAIL_USER or KENSHI_EMAIL_PASSWORD not set; logging contact message instead.")
            print(body)
        
        return render_template('contact.html', success=True)
    
    return render_template('contact.html')

if __name__ == '__main__':
    # Run the Flask app
    # Set debug=True for development, debug=False for production
    app.run(debug=True, host='0.0.0.0', port=5000)
