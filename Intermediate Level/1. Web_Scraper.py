from bs4 import BeautifulSoup
import csv

webpage_dom_content = """
<div class="testimonials-container">
    <div class="testimonial-card">
        <h4>Chetan Yadav</h4>
        <p>Cyber Security</p>
    </div>
    <div class="testimonial-card">
        <h4>Anushka Nair</h4>
        <p>UI/UX Design</p>
    </div>
    <div class="testimonial-card">
        <h4>Patrick Udegor</h4>
        <p>Cyber Security</p>
    </div>
    <div class="testimonial-card">
        <h4>Prarthana R Karanth</h4>
        <p>Web Development</p>
    </div>
    <div class="testimonial-card">
        <h4>Shuban V Rao</h4>
        <p>Cyber Security</p>
    </div>
    <div class="testimonial-card">
        <h4>Rashi Sharma</h4>
        <p>Cyber Security</p>
    </div>
</div>
"""

def extract_and_export_data(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    
    cards = soup.find_all('div', class_='testimonial-card')
    
    print(f"{'Name':<25} | {'Department / Domain'}")
    print("-" * 55)
    
    extracted_records = []
    
    for card in cards:
        name = card.find('h4').text.strip() if card.find('h4') else "N/A"
        domain = card.find('p').text.strip() if card.find('p') else "N/A"
        
        print(f"{name:<25} | {domain}")
        extracted_records.append([name, domain])
        
    csv_file_path = "shadowfox_extracted_data.csv"
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Department / Domain"]) 
        writer.writerows(extracted_records)
        
    print(f"\n[Success] Collected records successfully exported to: {csv_file_path}")

extract_and_export_data(webpage_dom_content)
