import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.message import EmailMessage

def track_price(url: str, target_price: float, check_interval: int = 3600) -> None:
    """
    Track product price and send email alert when below target
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...'
    }

    while True:
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Implement site-specific price extraction
            price_str = soup.find('span', {'class': 'price'}).text
            price = float(price_str.replace('$', '').strip())
            
            if price < target_price:
                send_alert(price, url)
                break
                
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(check_interval)

def send_alert(price: float, url: str) -> None:
    msg = EmailMessage()
    msg.set_content(f"Price alert! Current price: ${price}\n{url}")
    msg['Subject'] = "Price Drop Alert"
    msg['From'] = "your_email@example.com"
    msg['To'] = "recipient@example.com"

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

if __name__ == "__main__":
    track_price("https://example.com/product", 100.0) 