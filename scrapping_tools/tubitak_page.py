import requests
from bs4 import BeautifulSoup

def fetch_tubitak_announcements():
    url = "https://www.tubitak.gov.tr/tr/duyuru"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    if response.status_code != 200:
        return [f"TÜBİTAK sayfasına ulaşılamadı. Kod: {response.status_code}"]

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Tüm duyuru kutularını alıyoruz
    cards = soup.select(".views-row")

    results = []
    for card in cards[:5]:  # İlk 5 duyuruyu çek
        title_tag = card.select_one(".views-field-title")
        link_tag = card.find("a", href=True)

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag["href"]
            if not link.startswith("http"):
                link = "https://www.tubitak.gov.tr" + link
            results.append(f"{title} → {link}")

    return results


# Terminalden çalıştırmak için
if __name__ == "__main__":
    for a in fetch_tubitak_announcements():
        print("📢", a)
