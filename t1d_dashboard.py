import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="T1D Intelligence Dashboard",
    page_icon="🩺",
    layout="wide"
)


st.title("🩺 Type 1 Diabetes Intelligence Dashboard")
st.caption("A centralized hub for patient advocacy, research, policy, and organizational updates")


tab1, tab2, tab3 = st.tabs([
    "📰 News",
    "🤝 PAG Directory",
    "📅 Events",
])


# ==========================================
# NEWS TAB
# ==========================================

with tab1:

    st.header("📰 T1D Advocacy News")

    st.caption(
        "Latest updates from leading Type 1 Diabetes organizations"
    )

    import feedparser


    # ==========================================
    # NEWS SOURCES
    # ==========================================

    news_sources = {

        "American Diabetes Association": {
            "RSS": "https://diabetes.org/rss.xml",
            "News": "https://diabetes.org/newsroom"
        },

        "Breakthrough T1D": {
            "RSS": "https://www.breakthrought1d.org/feed/",
            "News": "https://www.breakthrought1d.org/news/"
        },

        "Beyond Type 1": {
            "RSS": "https://beyondtype1.org/feed/",
            "News": "https://beyondtype1.org/resources/?filter=news"
        },

        "Children with Diabetes": {
            "RSS": "https://childrenwithdiabetes.com/feed/",
            "News": "https://childrenwithdiabetes.com/news/"
        },

        "T1D Exchange": {
            "RSS": "https://t1dexchange.org/feed/",
            "News": "https://t1dexchange.org/articles/"
        }
    }


    # ==========================================
    # DISPLAY NEWS
    # ==========================================

    for organization, source in news_sources.items():

        try:

            feed = feedparser.parse(
                source["RSS"]
            )

            articles = feed.entries[:3]


            # Only display the organization
            # if the RSS feed actually returns articles.

            if articles:

                st.subheader(
                    organization
                )

                for article in articles:

                    title = article.get(
                        "title",
                        "Untitled Article"
                    )

                    link = article.get(
                        "link",
                        ""
                    )

                    st.markdown(
                        f"**{title}**"
                    )

                    if link:

                        st.link_button(
                            "🔗 Read Article",
                            link
                        )

                    st.divider()


        except Exception:

            # If the RSS feed fails,
            # don't display an error on the dashboard.

            continue


        # ==========================================
        # NEWS PAGE BUTTON
        # ==========================================

        st.link_button(
            f"View All {organization} News →",
            source["News"]
        )

        st.divider()

# ==========================================
# PAG DIRECTORY TAB
# ==========================================

with tab2:

    st.header("🤝 T1D Patient Advocacy Organization Hub")

    st.caption(
        "Explore leading Type 1 Diabetes organizations, news, and social media."
    )

    # ==========================================
    # VERIFIED ORGANIZATION LINKS
    # ==========================================

    verified_links = {

        "American Diabetes Association": {
            "Website": "https://diabetes.org/",
            "News": "https://diabetes.org/newsroom",
            "Instagram": "https://www.instagram.com/amdiabetesassn/",
            "LinkedIn": "https://www.linkedin.com/company/american-diabetes-association/",
            "X": "https://x.com/AmDiabetesAssn"
        },

        "Breakthrough T1D": {
            "Website": "https://www.breakthrought1d.org/",
            "News": "https://www.breakthrought1d.org/news/",
            "Instagram": "https://www.instagram.com/breakthrought1d/",
            "LinkedIn": "https://www.linkedin.com/company/breakthrought1d/",
            "X": "https://x.com/BreakthroughT1D"
        },

        "Beyond Type 1": {
            "Website": "https://beyondtype1.org/",
            "News": "https://beyondtype1.org/resources/?filter=news",
            "Instagram": "https://www.instagram.com/beyondtype1/",
            "LinkedIn": "https://www.linkedin.com/company/beyond-type1/",
            "X": "https://x.com/BeyondType1"
        },

        "Children with Diabetes": {
            "Website": "https://childrenwithdiabetes.com/",
            "News": "https://childrenwithdiabetes.com/news/",
            "Instagram": "https://www.instagram.com/childrenwithdiabetes/",
            "LinkedIn": "https://www.linkedin.com/company/children-with-diabetes/",
            "X": "https://x.com/cwdiabetes"
        },

        "T1D Exchange": {
            "Website": "https://t1dexchange.org/",
            "News": "https://t1dexchange.org/articles/",
            "Instagram": "https://www.instagram.com/t1dexchange/",
            "LinkedIn": "https://www.linkedin.com/company/t1d-exchange/",
            "X": "https://x.com/T1DExchange"
        },

        "The Diabetes Link": {
            "Website": "https://www.thediabeteslink.org/",
            "Events": "https://www.thediabeteslink.org/events",
            "Instagram": "https://www.instagram.com/thediabeteslink/",
            "X": "https://x.com/thediabeteslink"
        }

    }

    # ==========================================
    # LOAD PAG DATABASE
    # ==========================================

    pag_data = pd.read_csv("PAG_database.csv")

    # Remove Diabetes Leadership Council
    pag_data = pag_data[
        pag_data["Organization"] != "Diabetes Leadership Council"
    ]

    # ==========================================
    # DISPLAY ORGANIZATIONS
    # ==========================================

    for index, row in pag_data.iterrows():

        organization = row["Organization"]

        # Use verified links when available.
        # Fall back to CSV for other organizations.
        links = verified_links.get(
            organization,
            {
                "Website": row["Website"] if pd.notna(row["Website"]) else None,
                "News": row["News"] if pd.notna(row["News"]) else None,
                "Instagram": row["Instagram"] if pd.notna(row["Instagram"]) else None,
                "LinkedIn": row["LinkedIn"] if pd.notna(row["LinkedIn"]) else None,
                "X": row["X"] if pd.notna(row["X"]) else None
            }
        )

        with st.expander(
            f" {organization}",
            expanded=False
        ):

            st.write(
                f"**Category:** {row['Category']}"
            )

            st.write("")

            # ==========================================
            # LINK BUTTONS
            # ==========================================

            col1, col2 = st.columns(2)

            with col1:

                if links.get("Website"):
                    st.link_button(
                        "🌐 Website",
                        links["Website"],
                        use_container_width=True
                    )

                # The Diabetes Link uses Events instead of News
                if organization == "The Diabetes Link":

                    if links.get("Events"):
                        st.link_button(
                            "📅 Events",
                            links["Events"],
                            use_container_width=True
                        )

                else:

                    if links.get("News"):
                        st.link_button(
                            "📰 News",
                            links["News"],
                            use_container_width=True
                        )

                if links.get("Instagram"):
                    st.link_button(
                        "📸 Instagram",
                        links["Instagram"],
                        use_container_width=True
                    )

            with col2:

                # The Diabetes Link does NOT have LinkedIn
                if organization != "The Diabetes Link":

                    if links.get("LinkedIn"):
                        st.link_button(
                            "💼 LinkedIn",
                            links["LinkedIn"],
                            use_container_width=True
                        )

                if links.get("X"):
                    st.link_button(
                        "🐦 X",
                        links["X"],
                        use_container_width=True
                    )

            st.write("")
# ==========================================
# EVENTS TAB
# ==========================================

with tab3:

    import requests
    import re
    import json
    from bs4 import BeautifulSoup
    from datetime import datetime

    st.header("📅 T1D Events & Opportunities")

    st.caption(
        "Upcoming events, conferences, webinars, research meetings, "
        "and advocacy opportunities from leading T1D organizations."
    )

    # ==========================================
    # EVENT CALENDAR LINKS
    # ==========================================

    st.markdown("### 🔗 Event Calendars")

    EVENT_SOURCES = {

        "American Diabetes Association":
            "https://diabetes.org/events/calendar-events",

        "Breakthrough T1D":
            "https://www.breakthrought1d.org/discover-events/",

        "Children with Diabetes":
            "https://childrenwithdiabetes.com/events/",

        "TrialNet":
            "https://www.trialnet.org/news-events/events",

        "T1D Exchange":
            "https://t1dexchange.org/learning-sessions",

        "The Diabetes Link":
            "https://www.thediabeteslink.org/events",

        "Beyond Type 1":
            "https://beyondtype1.org/resources/#28"
    }

    source_cols = st.columns(3)

    for i, (organization, url) in enumerate(
        EVENT_SOURCES.items()
    ):

        with source_cols[i % 3]:

            st.link_button(
                f"📅 {organization}",
                url,
                use_container_width=True
            )

    st.divider()


    # ==========================================
    # REQUEST HELPER
    # ==========================================

    HEADERS = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    }


    def get_html(url):

        try:

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=25
            )

            if response.status_code == 200:

                return response.text

        except Exception:

            pass

        return ""


    # ==========================================
    # EVENT STORAGE
    # ==========================================

    all_events = []


    def add_event(
        organization,
        title,
        start_date,
        end_date=None,
        event_type="Event",
        link="",
        location=""
    ):

        if not title:
            return

        title = str(title).strip()

        if len(title) < 4:
            return

        # Remove obvious navigation/button text

        invalid_titles = {

            "Events",
            "Event",
            "Search",
            "Register",
            "Register Now",
            "Learn More",
            "View Details",
            "View Event",
            "Read More",
            "Apply Filters",
            "Clear Filters",
            "Find Events",
            "Upcoming Events",
            "Event Calendar",
            "Calendar",
            "More",
            "Next",
            "Previous"

        }

        if title in invalid_titles:
            return


        try:

            start = pd.to_datetime(
                start_date,
                errors="coerce"
            )

            if pd.isna(start):
                return


            if end_date:

                end = pd.to_datetime(
                    end_date,
                    errors="coerce"
                )

            else:

                end = start


            if pd.isna(end):

                end = start


            all_events.append({

                "Organization":
                    organization,

                "Event":
                    title,

                "Start Date":
                    start,

                "End Date":
                    end,

                "Type":
                    event_type,

                "Location":
                    location,

                "Link":
                    link

            })

        except Exception:

            pass


    # ==========================================
    # JSON-LD EVENT SCRAPER
    # ==========================================

    def scrape_json_ld(
        html,
        organization,
        default_type="Event"
    ):

        if not html:
            return

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        scripts = soup.find_all(
            "script",
            type="application/ld+json"
        )

        for script in scripts:

            try:

                raw = script.string

                if not raw:
                    continue

                data = json.loads(raw)

                if isinstance(data, dict):

                    data = [data]

                if not isinstance(data, list):
                    continue


                for item in data:

                    if not isinstance(item, dict):
                        continue


                    # Handle @graph

                    if "@graph" in item:

                        graph = item["@graph"]

                        if isinstance(graph, list):

                            for graph_item in graph:

                                if isinstance(
                                    graph_item,
                                    dict
                                ):

                                    data.append(
                                        graph_item
                                    )

                        continue


                    item_type = item.get(
                        "@type",
                        ""
                    )

                    if isinstance(
                        item_type,
                        list
                    ):

                        is_event = (
                            "Event"
                            in item_type
                        )

                    else:

                        is_event = (
                            item_type
                            == "Event"
                        )


                    if not is_event:
                        continue


                    title = item.get(
                        "name",
                        ""
                    )

                    start = item.get(
                        "startDate"
                    )

                    end = item.get(
                        "endDate"
                    )

                    link = item.get(
                        "url",
                        ""
                    )


                    location = ""

                    location_data = item.get(
                        "location"
                    )


                    if isinstance(
                        location_data,
                        dict
                    ):

                        location = (
                            location_data.get(
                                "name",
                                ""
                            )
                        )

                    elif isinstance(
                        location_data,
                        str
                    ):

                        location = (
                            location_data
                        )


                    add_event(

                        organization=
                        organization,

                        title=title,

                        start_date=start,

                        end_date=end,

                        event_type=
                        default_type,

                        link=link,

                        location=location

                    )


            except Exception:

                continue


    # ==========================================
    # ADA
    # ==========================================

    def scrape_ada():

        url = (
            "https://diabetes.org/events/"
            "calendar-events"
        )

        html = get_html(url)

        if not html:
            return


        # First try structured event data

        before_count = len(
            all_events
        )

        scrape_json_ld(
            html,
            "American Diabetes Association",
            "ADA Event"
        )


        # If structured data worked,
        # keep those results.

        if len(all_events) > before_count:
            return


        soup = BeautifulSoup(
            html,
            "html.parser"
        )


        # ADA event cards

        possible_cards = soup.select(
            "article, "
            "[class*='event'], "
            "[class*='card']"
        )


        for card in possible_cards:

            title_tag = card.find(
                [
                    "h2",
                    "h3",
                    "h4"
                ]
            )


            if not title_tag:
                continue


            title = title_tag.get_text(
                " ",
                strip=True
            )


            card_text = card.get_text(
                " ",
                strip=True
            )


            date_match = re.search(

                r"(January|February|March|April|May|June|"
                r"July|August|September|October|November|December)"
                r"\s+\d{1,2},?\s+\d{4}",

                card_text,

                re.IGNORECASE

            )


            if not date_match:
                continue


            event_date = pd.to_datetime(
                date_match.group(0),
                errors="coerce"
            )


            link_tag = card.find(
                "a",
                href=True
            )


            link = url


            if link_tag:

                link = link_tag["href"]

                if link.startswith("/"):

                    link = (
                        "https://diabetes.org"
                        + link
                    )


            add_event(

                organization=
                "American Diabetes Association",

                title=title,

                start_date=event_date,

                event_type="ADA Event",

                link=link

            )


    # ==========================================
    # BREAKTHROUGH T1D
    # ==========================================

    def scrape_breakthrough():

        base_url = (
            "https://www.breakthrought1d.org/"
            "discover-events/"
        )


        # Breakthrough currently uses
        # many paginated event pages.

        for page in range(1, 93):

            if page == 1:

                url = base_url

            else:

                url = (
                    base_url
                    + f"page/{page}/"
                )


            html = get_html(url)

            if not html:
                break


            soup = BeautifulSoup(
                html,
                "html.parser"
            )


            # Find event links/cards

            cards = soup.select(
                "article, "
                ".event, "
                "[class*='event-card'], "
                "[class*='event-item']"
            )


            found_on_page = 0


            for card in cards:

                title_tag = card.find(
                    [
                        "h2",
                        "h3",
                        "h4"
                    ]
                )


                if not title_tag:
                    continue


                title = title_tag.get_text(
                    " ",
                    strip=True
                )


                card_text = card.get_text(
                    " ",
                    strip=True
                )


                date_match = re.search(

                    r"(January|February|March|April|May|June|"
                    r"July|August|September|October|November|December)"
                    r"\s+\d{1,2},\s+\d{4}",

                    card_text,

                    re.IGNORECASE

                )


                if not date_match:
                    continue


                event_date = pd.to_datetime(
                    date_match.group(0),
                    errors="coerce"
                )


                # Event type

                event_type = (
                    "Breakthrough T1D Event"
                )


                for possible_type in [

                    "Community",
                    "Walk",
                    "T1D Support",
                    "Research",
                    "Gala",
                    "Ride",
                    "Golf",
                    "Run / Endurance"

                ]:

                    if possible_type.lower() in (
                        card_text.lower()
                    ):

                        event_type = (
                            possible_type
                        )

                        break


                # Location

                location = ""

                lines = [
                    x.strip()
                    for x in card.stripped_strings
                ]


                for line in lines:

                    if (
                        line != title
                        and
                        "Community" not in line
                        and
                        "Support" not in line
                        and
                        line
                        != date_match.group(0)
                    ):

                        if len(line) > 5:

                            location = line
                            break


                link_tag = card.find(
                    "a",
                    href=True
                )


                link = base_url


                if link_tag:

                    link = link_tag["href"]

                    if link.startswith("/"):

                        link = (
                            "https://www.breakthrought1d.org"
                            + link
                        )


                add_event(

                    organization=
                    "Breakthrough T1D",

                    title=title,

                    start_date=event_date,

                    event_type=event_type,

                    link=link,

                    location=location

                )

                found_on_page += 1


            # Fallback for pages where the
            # event cards aren't exposed as
            # normal HTML cards.

            if found_on_page == 0:

                text = soup.get_text(
                    "\n",
                    strip=True
                )


                date_matches = list(
                    re.finditer(

                        r"(January|February|March|April|May|June|"
                        r"July|August|September|October|November|December)"
                        r"\s+\d{1,2},\s+\d{4}",

                        text,

                        re.IGNORECASE

                    )
                )


                for i, match in enumerate(
                    date_matches
                ):

                    try:

                        event_date = pd.to_datetime(
                            match.group(0)
                        )


                        start = match.end()


                        if (
                            i + 1
                            < len(date_matches)
                        ):

                            end = (
                                date_matches[
                                    i + 1
                                ].start()
                            )

                        else:

                            end = (
                                start + 400
                            )


                        block = text[
                            start:end
                        ]


                        lines = [

                            x.strip()

                            for x in
                            block.split("\n")

                            if x.strip()

                        ]


                        if not lines:
                            continue


                        # Pick the first plausible
                        # title, not navigation.

                        title = None


                        for candidate in lines[:8]:

                            if candidate in [
                                "Community",
                                "Walk",
                                "Research",
                                "T1D Support",
                                "Search",
                                "Location",
                                "Event type"
                            ]:

                                continue


                            if len(candidate) >= 5:

                                title = candidate
                                break


                        if not title:
                            continue


                        add_event(

                            organization=
                            "Breakthrough T1D",

                            title=title,

                            start_date=event_date,

                            event_type=
                            "Breakthrough T1D Event",

                            link=base_url

                        )

                    except Exception:

                        continue


    # ==========================================
    # CHILDREN WITH DIABETES
    # ==========================================

    def scrape_cwd():

        url = (
            "https://childrenwithdiabetes.com/events/"
        )

        html = get_html(url)

        if not html:
            return


        before_count = len(
            all_events
        )


        scrape_json_ld(
            html,
            "Children with Diabetes",
            "Patient & Family Event"
        )


        soup = BeautifulSoup(
            html,
            "html.parser"
        )


        # CWD has conference/event headings.

        headings = soup.find_all(
            [
                "h2",
                "h3",
                "h4"
            ]
        )


        for heading in headings:

            title = heading.get_text(
                " ",
                strip=True
            )


            if not title:
                continue


            parent = heading.parent


            if not parent:
                continue


            text = parent.get_text(
                " ",
                strip=True
            )


            date_match = re.search(

                r"(January|February|March|April|May|June|"
                r"July|August|September|October|November|December)"
                r"\s+\d{1,2}"
                r"(?:[-–]\d{1,2})?"
                r",?\s+\d{4}",

                text,

                re.IGNORECASE

            )


            if not date_match:
                continue


            date_text = (
                date_match.group(0)
            )


            start_text = re.sub(
                r"[-–]\d{1,2}",
                "",
                date_text
            )


            start_date = pd.to_datetime(
                start_text,
                errors="coerce"
            )


            if pd.isna(start_date):
                continue


            add_event(

                organization=
                "Children with Diabetes",

                title=title,

                start_date=start_date,

                event_type=
                "Patient & Family Event",

                link=url

            )


    # ==========================================
    # TRIALNET
    # ==========================================

    def scrape_trialnet():

        url = (
            "https://www.trialnet.org/"
            "news-events/events"
        )

        html = get_html(url)

        if not html:
            return


        scrape_json_ld(
            html,
            "TrialNet",
            "Research / Screening"
        )


        soup = BeautifulSoup(
            html,
            "html.parser"
        )


        # TrialNet event listings

        cards = soup.select(
            "article, "
            "[class*='event'], "
            "[class*='views-row']"
        )


        for card in cards:

            title_tag = card.find(
                [
                    "h2",
                    "h3",
                    "h4"
                ]
            )


            if not title_tag:
                continue


            title = title_tag.get_text(
                " ",
                strip=True
            )


            text = card.get_text(
                " ",
                strip=True
            )


            date_match = re.search(

                r"(January|February|March|April|May|June|"
                r"July|August|September|October|November|December)"
                r"\s+\d{1,2}"
                r"(?:,\s+\d{4})?",

                text,

                re.IGNORECASE

            )


            if not date_match:
                continue


            date_text = (
                date_match.group(0)
            )


            if "," not in date_text:

                date_text += (
                    f", {datetime.now().year}"
                )


            event_date = pd.to_datetime(
                date_text,
                errors="coerce"
            )


            if pd.isna(event_date):
                continue


            add_event(

                organization="TrialNet",

                title=title,

                start_date=event_date,

                event_type=
                "Research / Screening",

                link=url

            )


    # ==========================================
    # T1D EXCHANGE
    # ==========================================

    def scrape_t1dx():

        url = (
            "https://t1dexchange.org/"
            "learning-sessions"
        )

        html = get_html(url)

        if not html:
            return


        # This page has a clear named
        # Learning Session and date.

        soup = BeautifulSoup(
            html,
            "html.parser"
        )


        headings = soup.find_all(
            [
                "h1",
                "h2",
                "h3",
                "h4"
            ]
        )


        for heading in headings:

            title = heading.get_text(
                " ",
                strip=True
            )


            if not title:
                continue


            if (
                "Learning Session"
                not in title
            ):

                continue


            parent = heading.parent


            if not parent:
                continue


            text = parent.get_text(
                " ",
                strip=True
            )


            date_match = re.search(

                r"(January|February|March|April|May|June|"
                r"July|August|September|October|November|December)"
                r"\s+\d{1,2}"
                r"(?:[-–]\d{1,2})?"
                r",\s+\d{4}",

                text,

                re.IGNORECASE

            )


            if not date_match:
                continue


            date_text = (
                date_match.group(0)
            )


            start_text = re.sub(
                r"[-–]\d{1,2}",
                "",
                date_text
            )


            start_date = pd.to_datetime(
                start_text,
                errors="coerce"
            )


            if pd.isna(start_date):
                continue


            add_event(

                organization="T1D Exchange",

                title=title,

                start_date=start_date,

                event_type=
                "Research / Professional",

                link=url,

                location=
                "San Diego, CA"

            )


    # ==========================================
    # THE DIABETES LINK
    # ==========================================

    def scrape_diabetes_link():

        url = (
            "https://www.thediabeteslink.org/"
            "events"
        )

        html = get_html(url)

        if not html:
            return


        scrape_json_ld(
            html,
            "The Diabetes Link",
            "Community / Advocacy"
        )


        soup = BeautifulSoup(
            html,
            "html.parser"
        )


        cards = soup.select(
            "article, "
            "[class*='event'], "
            "[class*='card']"
        )


        for card in cards:

            title_tag = card.find(
                [
                    "h2",
                    "h3",
                    "h4"
                ]
            )


            if not title_tag:
                continue


            title = title_tag.get_text(
                " ",
                strip=True
            )


            text = card.get_text(
                " ",
                strip=True
            )


            date_match = re.search(

                r"(January|February|March|April|May|June|"
                r"July|August|September|October|November|December)"
                r"\s+\d{1,2}"
                r"(?:,\s+\d{4})?",

                text,

                re.IGNORECASE

            )


            if not date_match:
                continue


            date_text = (
                date_match.group(0)
            )


            if "," not in date_text:

                date_text += (
                    f", {datetime.now().year}"
                )


            event_date = pd.to_datetime(
                date_text,
                errors="coerce"
            )


            if pd.isna(event_date):
                continue


            link_tag = card.find(
                "a",
                href=True
            )


            link = url


            if link_tag:

                link = link_tag["href"]

                if link.startswith("/"):

                    link = (
                        "https://www.thediabeteslink.org"
                        + link
                    )


            add_event(

                organization=
                "The Diabetes Link",

                title=title,

                start_date=event_date,

                event_type=
                "Community / Advocacy",

                link=link

            )


    # ==========================================
    # BEYOND TYPE 1
    # ==========================================

    def scrape_beyond():

        # Beyond Type 1 currently does not expose
        # a conventional public event calendar like
        # Breakthrough T1D or ADA.
        #
        # Keep the source link available rather than
        # inventing event records.

        return


    # ==========================================
    # RUN ALL SCRAPERS
    # ==========================================

    with st.spinner(
        "🔄 Pulling current event data..."
    ):

        scrape_ada()

        scrape_breakthrough()

        scrape_cwd()

        scrape_trialnet()

        scrape_t1dx()

        scrape_diabetes_link()

        scrape_beyond()


    # ==========================================
    # CLEAN DATA
    # ==========================================

    if all_events:

        events_df = pd.DataFrame(
            all_events
        )


        # Remove duplicate records

        events_df = events_df.drop_duplicates(
            subset=[
                "Organization",
                "Event",
                "Start Date"
            ]
        )


        # Remove obviously bad titles

        bad_words = [

            "search",
            "register",
            "learn more",
            "view details",
            "apply filters",
            "clear filters",
            "event calendar",
            "upcoming events"

        ]


        events_df = events_df[
            ~events_df["Event"].str.lower().isin(
                bad_words
            )
        ]


        # Keep current/future events

        today = pd.Timestamp.today().normalize()


        events_df = events_df[
            events_df["End Date"] >= today
        ]


        events_df = events_df.sort_values(
            "Start Date"
        )


        events = events_df.to_dict(
            "records"
        )

    else:

        events = []


    # ==========================================
    # FILTER
    # ==========================================

    col1, col2 = st.columns(2)


    with col1:

        organizations = [
            "All Organizations"
        ] + sorted(
            list(
                set(
                    e["Organization"]
                    for e in events
                )
            )
        )


        selected_org = st.selectbox(
            "🏢 Organization",
            organizations
        )


    with col2:

        event_types = [
            "All Event Types"
        ] + sorted(
            list(
                set(
                    e["Type"]
                    for e in events
                )
            )
        )


        selected_type = st.selectbox(
            "🏷️ Event Type",
            event_types
        )


    filtered_events = events


    if selected_org != "All Organizations":

        filtered_events = [

            e for e in filtered_events

            if e["Organization"]
            == selected_org

        ]


    if selected_type != "All Event Types":

        filtered_events = [

            e for e in filtered_events

            if e["Type"]
            == selected_type

        ]


    # ==========================================
    # UPCOMING EVENTS
    # ==========================================

    st.markdown(
        "## 📌 Upcoming Events"
    )


    if filtered_events:

        for event in filtered_events[:50]:

            with st.container(
                border=True
            ):

                # ==================================
                # REAL EVENT NAME
                # ==================================

                st.markdown(
                    f"## {event['Event']}"
                )


                # ==================================
                # ORGANIZATION
                # ==================================

                st.markdown(
                    f"**{event['Organization']}**"
                )


                st.caption(
                    event["Type"]
                )


                # ==================================
                # DATE
                # ==================================

                if (
                    event["Start Date"]
                    == event["End Date"]
                ):

                    date_text = (
                        event["Start Date"]
                        .strftime(
                            "%B %d, %Y"
                        )
                    )

                else:

                    date_text = (

                        event["Start Date"]
                        .strftime(
                            "%B %d, %Y"
                        )

                        + " – "

                        + event["End Date"]
                        .strftime(
                            "%B %d, %Y"
                        )

                    )


                st.markdown(
                    f"📅 **{date_text}**"
                )


                # ==================================
                # LOCATION
                # ==================================

                if event["Location"]:

                    st.markdown(
                        f"📍 {event['Location']}"
                    )


                st.write("")


                # ==================================
                # EVENT LINK
                # ==================================

                if event["Link"]:

                    st.link_button(
                        "View Event →",
                        event["Link"]
                    )


                st.write("")


    else:

        st.info(
            "No upcoming events were found "
            "from the available public event pages."
        )


    # ==========================================
    # FOOTER
    # ==========================================

    st.divider()

    st.caption(
        "Event information is retrieved from the "
        "organizations' public event pages when "
        "the dashboard loads. Because each organization "
        "uses a different calendar platform, availability "
        "and update timing may vary by source."
    )
