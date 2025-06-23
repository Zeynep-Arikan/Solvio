from bs4 import BeautifulSoup
import requests

def fetch_kosgeb_support_programs():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    targets = {
        "Girişimci Destek Programı": "https://www.kosgeb.gov.tr/site/tr/genel/destekdetay/1231/girisimci-destek-programi",
        "TEKMER Destek Programı": "https://www.kosgeb.gov.tr/site/tr/genel/destekdetay/9102/tekmer-destek-programi"
    }

    results = []

    for title, url in targets.items():
        response = requests.get(url, headers=headers)
        response.encoding = "utf-8"

        if response.status_code != 200:
            results.append(f"{title} → ❌ Erişilemedi (Kod: {response.status_code})")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # 1. Sayfa özetini çek
        content = soup.select_one(".panel-panel .panel-pane .pane-content")
        if not content:
            content = soup.select_one("article.post.hentry")  # fallback (özellikle TEKMER için)

        if content:
            text = content.get_text(strip=True)[:250] + "..."
            results.append(f"{title} → {url}\nÖzet: {text}\n")
        else:
            results.append(f"{title} → {url}\n(Detay alınamadı)\n")

        # 2. TEKMER özel başvuru formları (section ile)
        if "tekmer" in url.lower():
            form_sections = soup.select("section.accordion-inner.panel-body")
            for section in form_sections:
                if "Başvuru Formları" in section.get_text():
                    links = section.find_all("a", href=True)
                    if links:
                        results.append("📥 Başvuru Formları:")
                        for link in links:
                            name = link.get_text(strip=True)
                            href = link["href"]
                            if not href.startswith("http"):
                                href = "https://www.kosgeb.gov.tr" + href
                            results.append(f"📄 {name} → {href}")
                    break

    return results


# 🧪 Test için terminal çalıştırma bloğu
if __name__ == "__main__":
    print("📌 KOSGEB Destek Programları (Girişimci + TEKMER):\n")
    for item in fetch_kosgeb_support_programs():
        print(item)
