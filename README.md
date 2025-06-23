# Solvio – AI-Powered Startup Advisor 💡🤖

Solvio, yapay zekâ destekli açık kaynaklı bir danışmanlık platformudur.  
Kullanıcılara şirket kurma süreçleri, devlet destekleri (KOSGEB, TÜBİTAK), teknopark avantajları ve daha fazlası hakkında akıllı öneriler sunar.

## 🚀 Özellikler

- 🧠 LLM destekli danışman ajanlar (LangChain + Gemini 1.5 Flash)
- 🏢 Şirket kurma rehberi (Anonim, Limited, Start-up vs.)
- 💸 Teşvik eşleştirme (KOSGEB, TÜBİTAK, Ar-Ge)
- 🔍 Web scraping ile güncel desteklerin listelenmesi
- 🧭 Doğru ajanla doğru bilgiye yönlendirme
- 🌐 Gradio tabanlı kullanıcı arayüzü (yakında)

## 🔧 Kullanılan Teknolojiler

- `Python`
- `LangChain`
- `Google Gemini 1.5 Flash`
- `Gradio`
- `dotenv`
- `BeautifulSoup` + `Requests` (scraping için)
- `Open Source principles`

## 🛠️ Kurulum

```bash
git clone https://github.com/Zeynep-Arikan/Solvio.git
cd Solvio
python -m venv venv
venv\Scripts\activate  # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
