import requests
from bs4 import BeautifulSoup

url="https://www.shadowfox.org.in/"
headers={"User-Agent": "Mozilla/5.0"}

response=requests.get(url,headers=headers)
if response.status_code == 200:
    soup=BeautifulSoup(response.text,'html.parser')
    testimonials=soup.find_all('div',class_='testimonial-card')     
    print(f"{'Name':<25} | {'Department'}")
    print("-" * 50)
    
    for item in testimonials:
        name=item.find('h4').text.strip() if item.find('h4') else "N/A"
        department=item.find('p').text.strip() if item.find('p') else "N/A"
        print(f"{name:<25} | {department}")
else:
    print(f"Failed to fetch webpage. Status code: {response.status_code}")
