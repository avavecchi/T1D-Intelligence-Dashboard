import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="T1D Intelligence Dashboard",
    page_icon="🩺",
    layout="wide"
)


st.title("🩺 Type 1 Diabetes Intelligence Dashboard")
st.caption("Patient advocacy, research, policy, and social media hub")


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
    from bs4 import BeautifulSoup
    from datetime import datetime
    from dateutil import parser as date_parser

    st.header("📅 T1D Events & Opportunities")

    st.caption(
        "Live event calendar aggregating events from leading Type 1 Diabetes "
        "organizations and research networks."
    )

    # ==========================================
    # EVENT SOURCE WEBSITES
    # ==========================================

    EVENT_SOURCES = {

        "American Diabetes Association": {
            "url": "https://diabetes.org/events/calendar-events",
            "type": "ADA"
        },

        "Breakthrough T1D": {
            "url": "https://www.breakthrought1d.org/discover-events/",
            "type": "BREAKTHROUGH"
        },

        "Children with Diabetes": {
            "url": "https://childrenwithdiabetes.com/events/",
            "type": "CWD"
        },

        "TrialNet": {
            "url": "https://www.trialnet.org/news-events/events",
            "type": "TRIALNET"
        },

        "T1D Exchange": {
            "url": "https://t1dexchange.org/learning-sessions",
            "type": "T1DX"
        },

        "The Diabetes Link": {
            "url": "https://www.thediabeteslink.org/events",
            "type": "DIABETES_LINK"
        },

        "Beyond Type 1": {
            "url": "https://beyondtype1.org/",
            "type": "BEYOND"
        }
    }


    # ==========================================
    # SESSION STATE
    # ==========================================

    if "calendar_month" not in st.session_state:

        st.session_state.calendar_month = pd.Timestamp.today().replace(
            day=1
        )


# ==========================================
# EVENT STORAGE
# ==========================================

all_events = []


# ==========================================
# EVENT SOURCE WEBSITES
# ==========================================

EVENT_SOURCES = {

    "American Diabetes Association": {
        "url": "https://diabetes.org/events/calendar-events",
        "type": "ADA"
    },

    "Breakthrough T1D": {
        "url": "https://www.breakthrought1d.org/discover-events/",
        "type": "BREAKTHROUGH"
    },

    "Children with Diabetes": {
        "url": "https://childrenwithdiabetes.com/events/",
        "type": "CWD"
    },

    "TrialNet": {
        "url": "https://www.trialnet.org/news-events/events",
        "type": "TRIALNET"
    },

    "T1D Exchange": {
        "url": "https://t1dexchange.org/learning-sessions",
        "type": "T1DX"
    },

    "The Diabetes Link": {
        "url": "https://www.thediabeteslink.org/events",
        "type": "DIABETES_LINK"
    },

    "Beyond Type 1": {
        "url": "https://beyondtype1.org/events/",
        "type": "BEYOND"
    },

    "ISPAD": {
        "url": "https://www.ispad.org/events.html",
        "type": "ISPAD"
    }
}


# ==========================================
# ADD EVENT
# ==========================================

def add_event(
    organization,
    title,
    start_date,
    end_date=None,
    event_type="Event",
    link="",
    location=""
):

    try:

        start_date = pd.to_datetime(
            start_date,
            errors="coerce"
        )

        if pd.isna(start_date):
            return

        if end_date:

            end_date = pd.to_datetime(
                end_date,
                errors="coerce"
            )

        else:

            end_date = start_date

        if pd.isna(end_date):

            end_date = start_date

        all_events.append({

            "Organization": organization,

            "Event": str(title).strip(),

            "Start Date": start_date,

            "End Date": end_date,

            "Type": event_type,

            "Location": location,

            "Link": link

        })

    except Exception:

        pass


# ==========================================
# HTTP REQUEST
# ==========================================

@st.cache_data(ttl=3600)
def get_page(url):

    try:

        headers = {

            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/139.0 Safari/537.36"

        }

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        return response.text

    except Exception:

        return ""


# ==========================================
# DATE PARSER
# ==========================================

def parse_date(text):

    if not text:
        return None

    patterns = [

        r"""
        (January|February|March|April|May|June|
        July|August|September|October|November|December)
        \s+\d{1,2},\s+\d{4}
        """,

        r"""
        (January|February|March|April|May|June|
        July|August|September|October|November|December)
        \s+\d{1,2}
        """,

        r"""
        \d{1,2}/\d{1,2}/\d{4}
        """

    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE |
            re.VERBOSE
        )

        if match:

            try:

                parsed = pd.to_datetime(
                    match.group(0),
                    errors="coerce"
                )

                if not pd.isna(parsed):

                    return parsed

            except Exception:

                continue

    return None


# ==========================================
# BREAKTHROUGH T1D
# ==========================================

def scrape_breakthrough():

    base_url = (
        "https://www.breakthrought1d.org/"
        "discover-events/"
    )

    # Current site contains hundreds of events
    # across many paginated pages.

    for page_number in range(1, 100):

        if page_number == 1:

            url = base_url

        else:

            url = (
                base_url
                + f"page/{page_number}/"
            )

        html = get_page(url)

        if not html:
            continue

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        # Event cards on the Breakthrough T1D site
        # are represented by headings and surrounding
        # text.

        headings = soup.find_all(
            ["h2", "h3"]
        )

        page_event_count = 0

        for heading in headings:

            title = heading.get_text(
                " ",
                strip=True
            )

            if not title:
                continue

            if len(title) < 4:
                continue

            # Ignore page navigation headings

            ignored = [

                "Search",
                "Location",
                "Date range",
                "Event type",
                "Find Events",
                "Open Filters"

            ]

            if title in ignored:
                continue

            container = heading.parent

            if not container:
                continue

            block = container.get_text(
                " ",
                strip=True
            )

            event_date = parse_date(
                block
            )

            if event_date is None:

                # Try a larger surrounding block

                parent = container.parent

                if parent:

                    block = parent.get_text(
                        " ",
                        strip=True
                    )

                    event_date = parse_date(
                        block
                    )

            if event_date is None:
                continue

            # Find actual event URL

            link = ""

            link_tag = heading.find(
                "a",
                href=True
            )

            if not link_tag:

                link_tag = container.find(
                    "a",
                    href=True
                )

            if link_tag:

                link = link_tag.get(
                    "href",
                    ""
                )

                if link.startswith("/"):

                    link = (
                        "https://www.breakthrought1d.org"
                        + link
                    )

            if not link:

                link = url

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
                "Run / Endurance",
                "Other Special Event"

            ]:

                if possible_type.lower() in block.lower():

                    event_type = possible_type

                    break

            add_event(

                organization=
                "Breakthrough T1D",

                title=title,

                start_date=event_date,

                event_type=event_type,

                link=link,

                location=""

            )

            page_event_count += 1

        # Stop after a reasonable number of
        # consecutive empty pages.

        if (
            page_event_count == 0
            and page_number > 10
        ):

            break


# ==========================================
# ADA
# ==========================================

def scrape_ada():

    url = (
        "https://diabetes.org/events/calendar-events"
    )

    html = get_page(url)

    if not html:
        return

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # Look for links that represent events.

    for link_tag in soup.find_all(
        "a",
        href=True
    ):

        title = link_tag.get_text(
            " ",
            strip=True
        )

        if not title:
            continue

        if len(title) < 5:
            continue

        href = link_tag.get(
            "href",
            ""
        )

        if href.startswith("/"):

            href = (
                "https://diabetes.org"
                + href
            )

        # Look at nearby containers

        container = link_tag.parent

        if not container:
            continue

        block = container.get_text(
            " ",
            strip=True
        )

        event_date = parse_date(
            block
        )

        if event_date is None:

            if container.parent:

                block = (
                    container.parent
                    .get_text(
                        " ",
                        strip=True
                    )
                )

                event_date = parse_date(
                    block
                )

        if event_date is None:
            continue

        # Don't capture generic navigation

        ignored = [

            "Register",
            "Learn More",
            "Join",
            "Sign Up",
            "View More",
            "Load More"

        ]

        if title in ignored:
            continue

        add_event(

            organization=
            "American Diabetes Association",

            title=title,

            start_date=event_date,

            event_type="ADA Event",

            link=href or url

        )


# ==========================================
# CHILDREN WITH DIABETES
# ==========================================

def scrape_cwd():

    url = (
        "https://childrenwithdiabetes.com/events/"
    )

    html = get_page(url)

    if not html:
        return

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # CWD uses event/conference content
    # rather than a large traditional calendar.

    for heading in soup.find_all(
        ["h2", "h3", "h4"]
    ):

        title = heading.get_text(
            " ",
            strip=True
        )

        if not title:
            continue

        container = heading.parent

        if not container:
            continue

        block = container.get_text(
            " ",
            strip=True
        )

        event_date = parse_date(
            block
        )

        if event_date is None:

            if container.parent:

                block = (
                    container.parent
                    .get_text(
                        " ",
                        strip=True
                    )
                )

                event_date = parse_date(
                    block
                )

        if event_date is None:
            continue

        link = ""

        link_tag = heading.find(
            "a",
            href=True
        )

        if not link_tag:

            link_tag = container.find(
                "a",
                href=True
            )

        if link_tag:

            link = link_tag.get(
                "href",
                ""
            )

            if link.startswith("/"):

                link = (
                    "https://childrenwithdiabetes.com"
                    + link
                )

        add_event(

            organization=
            "Children with Diabetes",

            title=title,

            start_date=event_date,

            event_type=
            "Patient & Family Event",

            link=link or url

        )


# ==========================================
# TRIALNET
# ==========================================

def scrape_trialnet():

    url = (
        "https://www.trialnet.org/"
        "news-events/events"
    )

    html = get_page(url)

    if not html:
        return

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # TrialNet event listings

    for element in soup.find_all(
        ["article", "li", "div"]
    ):

        block = element.get_text(
            " ",
            strip=True
        )

        if not block:
            continue

        event_date = parse_date(
            block
        )

        if event_date is None:
            continue

        link_tag = element.find(
            "a",
            href=True
        )

        if not link_tag:
            continue

        title = link_tag.get_text(
            " ",
            strip=True
        )

        if not title:
            continue

        href = link_tag.get(
            "href",
            ""
        )

        if href.startswith("/"):

            href = (
                "https://www.trialnet.org"
                + href
            )

        add_event(

            organization="TrialNet",

            title=title,

            start_date=event_date,

            event_type=
            "Research / Screening",

            link=href or url,

            location=""

        )


# ==========================================
# T1D EXCHANGE
# ==========================================

def scrape_t1dx():

    url = (
        "https://t1dexchange.org/"
        "learning-sessions"
    )

    html = get_page(url)

    if not html:
        return

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # Current T1D Exchange page contains
    # the 2026 Learning Session dates:
    # November 9–11, 2026.

    page_text = soup.get_text(
        " ",
        strip=True
    )

    date_match = re.search(

        r"""
        (November)
        \s+
        (\d{1,2})
        [–-]
        (\d{1,2}),
        \s*
        (\d{4})
        """,

        page_text,

        re.IGNORECASE |
        re.VERBOSE

    )

    if date_match:

        try:

            month = date_match.group(1)

            start_day = date_match.group(2)

            end_day = date_match.group(3)

            year = date_match.group(4)

            start_date = pd.to_datetime(

                f"{month} {start_day}, {year}"

            )

            end_date = pd.to_datetime(

                f"{month} {end_day}, {year}"

            )

            add_event(

                organization=
                "T1D Exchange",

                title=
                "T1DX-QI 10th Annual Learning Session",

                start_date=start_date,

                end_date=end_date,

                event_type=
                "Research / Professional",

                link=url,

                location=
                "San Diego, CA"

            )

        except Exception:

            pass


# ==========================================
# THE DIABETES LINK
# ==========================================

def scrape_diabetes_link():

    url = (
        "https://www.thediabeteslink.org/events"
    )

    html = get_page(url)

    if not html:
        return

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    for heading in soup.find_all(
        ["h2", "h3", "h4"]
    ):

        title = heading.get_text(
            " ",
            strip=True
        )

        if not title:
            continue

        container = heading.parent

        if not container:
            continue

        block = container.get_text(
            " ",
            strip=True
        )

        event_date = parse_date(
            block
        )

        if event_date is None:

            if container.parent:

                block = (
                    container.parent
                    .get_text(
                        " ",
                        strip=True
                    )
                )

                event_date = parse_date(
                    block
                )

        if event_date is None:
            continue

        link = ""

        link_tag = heading.find(
            "a",
            href=True
        )

        if not link_tag:

            link_tag = container.find(
                "a",
                href=True
            )

        if link_tag:

            link = link_tag.get(
                "href",
                ""
            )

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

            link=link or url

        )


# ==========================================
# BEYOND TYPE 1
# ==========================================

def scrape_beyond():

    url = (
        "https://beyondtype1.org/events/"
    )

    html = get_page(url)

    if not html:
        return

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    for heading in soup.find_all(
        ["h2", "h3", "h4"]
    ):

        title = heading.get_text(
            " ",
            strip=True
        )

        if not title:
            continue

        container = heading.parent

        if not container:
            continue

        block = container.get_text(
            " ",
            strip=True
        )

        event_date = parse_date(
            block
        )

        if event_date is None:

            if container.parent:

                block = (
                    container.parent
                    .get_text(
                        " ",
                        strip=True
                    )
                )

                event_date = parse_date(
                    block
                )

        if event_date is None:
            continue

        link = ""

        link_tag = heading.find(
            "a",
            href=True
        )

        if not link_tag:

            link_tag = container.find(
                "a",
                href=True
            )

        if link_tag:

            link = link_tag.get(
                "href",
                ""
            )

            if link.startswith("/"):

                link = (
                    "https://beyondtype1.org"
                    + link
                )

        add_event(

            organization=
            "Beyond Type 1",

            title=title,

            start_date=event_date,

            event_type=
            "T1D Community Event",

            link=link or url

        )


# ==========================================
# ISPAD
# ==========================================

def scrape_ispad():

    url = (
        "https://www.ispad.org/events.html"
    )

    html = get_page(url)

    if not html:
        return

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    for heading in soup.find_all(
        ["h2", "h3", "h4"]
    ):

        title = heading.get_text(
            " ",
            strip=True
        )

        if not title:
            continue

        container = heading.parent

        if not container:
            continue

        block = container.get_text(
            " ",
            strip=True
        )

        event_date = parse_date(
            block
        )

        if event_date is None:
            continue

        link = ""

        link_tag = heading.find(
            "a",
            href=True
        )

        if link_tag:

            link = link_tag.get(
                "href",
                ""
            )

            if link.startswith("/"):

                link = (
                    "https://www.ispad.org"
                    + link
                )

        add_event(

            organization="ISPAD",

            title=title,

            start_date=event_date,

            event_type=
            "Scientific Conference",

            link=link or url

        )


# ==========================================
# RUN ALL SCRAPERS
# ==========================================

with st.spinner(
    "🔄 Updating live event calendars..."
):

    scrape_ada()

    scrape_breakthrough()

    scrape_cwd()

    scrape_trialnet()

    scrape_t1dx()

    scrape_diabetes_link()

    scrape_beyond()

    scrape_ispad()
    
    # ==========================================
    # REMOVE DUPLICATES
    # ==========================================

    if all_events:

        events_df = pd.DataFrame(
            all_events
        )


        events_df = events_df.drop_duplicates(
            subset=[
                "Organization",
                "Event",
                "Start Date"
            ]
        )


        events = events_df.to_dict(
            "records"
        )

    else:

        events = []


    # ==========================================
    # EVENT SOURCE STATUS
    # ==========================================

    st.markdown(
        "### 📡 Live Event Sources"
    )


    status_cols = st.columns(
        6
    )


    source_names = [

        "ADA",

        "Breakthrough T1D",

        "Children with Diabetes",

        "TrialNet",

        "T1D Exchange",

        "The Diabetes Link"

    ]


    for i, source_name in enumerate(
        source_names
    ):

        with status_cols[
            i
        ]:

            st.metric(
                source_name,
                len([
                    e for e in events
                    if (
                        source_name
                        in e["Organization"]
                    )
                ])
            )


    st.divider()


    # ==========================================
    # MONTH NAVIGATION
    # ==========================================

    col1, col2, col3 = st.columns(
        [1, 3, 1]
    )


    with col1:

        if st.button(
            "← Previous",
            use_container_width=True
        ):

            st.session_state.calendar_month = (

                st.session_state.calendar_month
                - pd.DateOffset(
                    months=1
                )

            )

            st.rerun()


    with col2:

        st.markdown(

            f"""
            <h2 style="
                text-align:center;
                margin-bottom:0;
            ">
                {st.session_state.calendar_month.strftime('%B %Y')}
            </h2>
            """,

            unsafe_allow_html=True

        )


    with col3:

        if st.button(
            "Next →",
            use_container_width=True
        ):

            st.session_state.calendar_month = (

                st.session_state.calendar_month
                + pd.DateOffset(
                    months=1
                )

            )

            st.rerun()


    if st.button(
        "📍 Jump to Today"
    ):

        st.session_state.calendar_month = (
            pd.Timestamp.today().replace(
                day=1
            )
        )

        st.rerun()


    st.divider()


    # ==========================================
    # ORGANIZATION FILTER
    # ==========================================

    organization_options = [
        "All Organizations"
    ] + sorted(
        list(
            set(
                event["Organization"]
                for event in events
            )
        )
    )


    selected_organization = st.selectbox(

        "🏢 Filter by organization",

        organization_options

    )


    if (
        selected_organization
        == "All Organizations"
    ):

        calendar_events = events

    else:

        calendar_events = [

            event
            for event in events

            if event["Organization"]
            == selected_organization

        ]


    # ==========================================
    # CALENDAR
    # ==========================================

    calendar_month = (
        st.session_state.calendar_month
    )


    month_start = calendar_month

    month_end = (
        calendar_month
        + pd.offsets.MonthEnd(1)
    )


    first_weekday = (
        month_start.weekday()
    )


    days_in_month = (
        month_end.day
    )


    weekdays = [

        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"

    ]


    header_cols = st.columns(7)


    for i, weekday in enumerate(
        weekdays
    ):

        with header_cols[i]:

            st.markdown(

                f"""
                <div style="
                    text-align:center;
                    font-weight:700;
                    padding:8px;
                ">
                    {weekday}
                </div>
                """,

                unsafe_allow_html=True

            )


    # ==========================================
    # CALENDAR CELLS
    # ==========================================

    total_cells = (
        first_weekday
        + days_in_month
    )


    number_of_weeks = (
        (total_cells + 6) // 7
    )


    day_number = 1


    for week in range(
        number_of_weeks
    ):

        cols = st.columns(7)


        for weekday in range(7):

            cell_number = (
                week * 7
                + weekday
            )


            with cols[weekday]:

                if cell_number < first_weekday:

                    st.markdown(
                        "<div style='height:120px;'></div>",
                        unsafe_allow_html=True
                    )

                    continue


                if (
                    day_number
                    > days_in_month
                ):

                    st.markdown(
                        "<div style='height:120px;'></div>",
                        unsafe_allow_html=True
                    )

                    continue


                current_date = pd.Timestamp(

                    year=calendar_month.year,

                    month=calendar_month.month,

                    day=day_number

                )


                day_events = [

                    event
                    for event in calendar_events

                    if (

                        event["Start Date"]
                        <= current_date
                        <= event["End Date"]

                    )

                ]


                with st.container(
                    border=True
                ):

                    if (
                        current_date.date()
                        == pd.Timestamp.today().date()
                    ):

                        st.markdown(
                            f"### 📍 {day_number}"
                        )

                    else:

                        st.markdown(
                            f"### {day_number}"
                        )


                    for event in day_events[:5]:

                        st.markdown(

                            f"**📌 "
                            f"{event['Event']}**"

                        )

                        st.caption(

                            f"{event['Organization']} "
                            f"• "
                            f"{event['Type']}"

                        )


                        if event["Link"]:

                            st.link_button(

                                "View",

                                event["Link"],

                                use_container_width=True

                            )


                    if len(day_events) > 5:

                        st.caption(

                            f"+ {len(day_events) - 5} "
                            f"more events"

                        )


                day_number += 1


    # ==========================================
    # UPCOMING EVENTS
    # ==========================================

    st.divider()

    st.markdown(
        "## 📌 Upcoming Events"
    )


    today = pd.Timestamp.today()


    upcoming_events = sorted(

        [

            event
            for event in events

            if event["End Date"]
            >= today

        ],

        key=lambda x:
        x["Start Date"]

    )


    if upcoming_events:

        for event in upcoming_events[:20]:

            with st.container(
                border=True
            ):

                col1, col2 = st.columns(
                    [4, 1]
                )


                with col1:

                    st.markdown(

                        f"### 📌 "
                        f"{event['Event']}"

                    )

                    st.caption(

                        f"{event['Organization']} "
                        f"• "
                        f"{event['Type']}"

                    )


                    if event["Location"]:

                        st.write(
                            f"📍 {event['Location']}"
                        )


                with col2:

                    st.write(

                        event[
                            "Start Date"
                        ].strftime(
                            "%b %d, %Y"
                        )

                    )


                    if event["Link"]:

                        st.link_button(

                            "View Event →",

                            event["Link"],

                            use_container_width=True

                        )


    else:

        st.info(
            "No upcoming events were found."
        )


    # ==========================================
    # SOURCE LINKS
    # ==========================================

    st.divider()

    st.markdown(
        "### 🔗 Event Calendars"
    )


    source_cols = st.columns(3)


    for i, (
        organization,
        source
    ) in enumerate(
        EVENT_SOURCES.items()
    ):

        with source_cols[
            i % 3
        ]:

            st.link_button(

                f"View {organization} Calendar →",

                source["url"],

                use_container_width=True

            )


    st.caption(
        "Event data is retrieved from the organizations' "
        "public event pages when the dashboard loads. "
        "Because each organization uses a different calendar "
        "system, individual sources may update at different times."
    )
