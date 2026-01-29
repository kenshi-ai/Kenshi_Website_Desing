from flask import Flask, render_template, request, redirect, url_for
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
        
        # Here you can add email sending logic later
        # For now, we'll just print to console
        print(f"New contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        
        return render_template('contact.html', success=True)
    
    return render_template('contact.html')

if __name__ == '__main__':
    # Run the Flask app
    # Set debug=True for development, debug=False for production
    app.run(debug=True, host='0.0.0.0', port=5000)
