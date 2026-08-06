import requests
from bs4 import BeautifulSoup
from datetime import datetime


organizations = [
    "American Diabetes Association",
    "Breakthrough T1D",
    "Beyond Type 1",
    "Children with Diabetes",
    "T1D Exchange",
    "The Diabetes Link",
    "Diabetes Patient Advocacy Coalition",
    "Diabetes Leadership Council"
]


topics = [
    "Type 1 diabetes screening",
    "Teplizumab Tzield",
    "beta cell preservation",
    "clinical trials type 1 diabetes",
    "FDA type 1 diabetes"
]


def get_google_news(query):
    url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "xml")

    articles = []

    for item in soup.find_all("item")[:5]:
        title = item.title.text
        link = item.link.text
        date = item.pubDate.text

        articles.append({
            "title": title,
            "link": link,
            "date": date
        })

    return articles


def generate_report():

    today = datetime.now().strftime("%B %d, %Y")

    report = []

    report.append(
        f"""
🩺 T1D INTELLIGENCE DAILY REPORT
Date: {today}

================================
"""
    )


    report.append("\n📰 ADVOCACY ORGANIZATION UPDATES\n")


    for org in organizations:

        report.append(f"\n--- {org} ---")

        articles = get_google_news(org + " diabetes")

        if articles:
            for article in articles:
                report.append(
                    f"""
• {article['title']}
  {article['link']}
"""
                )

        else:
            report.append("No updates found.")



    report.append("\n\n🔬 RESEARCH & SCIENCE UPDATES\n")


    for topic in topics:

        report.append(f"\n--- {topic} ---")

        articles = get_google_news(topic)

        for article in articles:
            report.append(
                f"""
• {article['title']}
  {article['link']}
"""
            )


    filename = "T1D_Daily_Report.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(report))


    print(
        f"""
✅ T1D Daily Report Created!

File:
{filename}
"""
    )


generate_report()
