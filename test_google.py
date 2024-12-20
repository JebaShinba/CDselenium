import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def send_email(subject, body):
    sender_email = "jebashinba2001@gmail.com"
    sender_password = "rjos mxvq elqt yugu"  # Consider using an app password for security
    recipient_email = "jeba@nidrive.in"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def run_selenium_test():
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Applicable to Windows environments
    chrome_options.add_argument("--window-size=1280x1024")  # Set a specific window size

# Initialize the Chrome WebDriver with these options
    driver = webdriver.Chrome(options=chrome_options)

    # Set up Selenium WebDriver
    
    
    try:
        # Example test: Open Google and check the title
        driver.get("https://www.googl.com")
        assert "Google" in driver.title  # Simple assertion for testing
        
        # If the test passes
        subject = "Selenium Test Passed"
        body = "The Selenium test ran successfully and the page title is correct."
        send_email(subject, body)

    except AssertionError:
        # If the test fails
        subject = "Selenium Test Failed"
        body = "The Selenium test failed. Please check the logs for details."
        send_email(subject, body)

    finally:
        driver.quit()  

if __name__ == "__main__":
    run_selenium_test()
