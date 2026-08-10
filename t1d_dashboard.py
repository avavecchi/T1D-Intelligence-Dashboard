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
    from bs4 import BeautifulSoup
    from datetime import datetime
    import re

    st.header("📅 T1D Events & Opportunities")

    st.caption(
        "Upcoming conferences, webinars, research meetings, "
        "and advocacy opportunities across the Type 1 Diabetes community."
    )

    # ==========================================
    # OFFICIAL EVENT CALENDARS
    # ==========================================

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
            "https://beyondtype1.org/"
    }


    # ==========================================
    # EVENT CALENDAR LINKS
    # ==========================================

    st.markdown("### 🔗 Official Event Calendars")

    st.caption(
        "Go directly to each organization's official event calendar "
        "for the most complete and current information."
    )

    calendar_cols = st.columns(3)

    for i, (organization, url) in enumerate(
        EVENT_SOURCES.items()
    ):

        with calendar_cols[i % 3]:

            st.link_button(
                f"📅 {organization}",
                url,
                use_container_width=True
            )


    st.divider()


    # ==========================================
    # EVENT STORAGE
    # ==========================================

    all_events = []


    # ==========================================
    # HTTP REQUEST
    # ==========================================

    def get_page(url):

        try:

            headers = {
                "User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 Chrome/126 Safari/537.36"
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=20
            )

            if response.status_code == 200:

                return response.text

        except Exception:

            pass

        return ""


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

                "Event": title,

                "Start Date": start_date,

                "End Date": end_date,

                "Type": event_type,

                "Location": location,

                "Link": link

            })

        except Exception:

            pass


    # ==========================================
    # GENERIC EVENT SCRAPER
    # ==========================================

    def scrape_generic(
        organization,
        url,
        event_type="Event"
    ):

        html = get_page(url)

        if not html:

            return

        soup = BeautifulSoup(
            html,
            "html.parser"
        )


        # --------------------------------------
        # Look for structured event data first
        # --------------------------------------

        scripts = soup.find_all(
            "script",
            type="application/ld+json"
        )

        for script in scripts:

            try:

                import json

                data = json.loads(
                    script.string or ""
                )

                if isinstance(data, dict):

                    data = [data]

                if not isinstance(data, list):

                    continue

                for item in data:

                    if not isinstance(
                        item,
                        dict
                    ):

                        continue

                    item_type = item.get(
                        "@type",
                        ""
                    )

                    if item_type != "Event":

                        continue

                    title = item.get(
                        "name",
                        ""
                    )

                    start_date = item.get(
                        "startDate"
                    )

                    end_date = item.get(
                        "endDate"
                    )

                    link = item.get(
                        "url",
                        url
                    )

                    location = ""

                    location_data = item.get(
                        "location"
                    )

                    if isinstance(
                        location_data,
                        dict
                    ):

                        location = location_data.get(
                            "name",
                            ""
                        )

                    if title and start_date:

                        add_event(

                            organization=
                            organization,

                            title=title,

                            start_date=start_date,

                            end_date=end_date,

                            event_type=event_type,

                            link=link,

                            location=location

                        )

            except Exception:

                continue


        # --------------------------------------
        # Fallback: visible page events
        # --------------------------------------

        if not any(
            e["Organization"] == organization
            for e in all_events
        ):

            text = soup.get_text(
                "\n",
                strip=True
            )

            date_pattern = re.compile(
                r"\b("
                r"January|February|March|April|May|June|"
                r"July|August|September|October|November|December"
                r")\s+"
                r"(\d{1,2})"
                r"(?:,\s*(\d{4}))?",
                re.IGNORECASE
            )

            for match in date_pattern.finditer(
                text
            ):

                try:

                    month = match.group(1)
                    day = match.group(2)
                    year = match.group(3)

                    if not year:

                        year = str(
                            datetime.now().year
                        )

                    event_date = pd.to_datetime(
                        f"{month} {day}, {year}",
                        errors="coerce"
                    )

                    if pd.isna(event_date):

                        continue

                    beginning = max(
                        0,
                        match.start() - 250
                    )

                    surrounding = text[
                        beginning:
                        match.start()
                    ]

                    lines = [
                        x.strip()
                        for x in surrounding.split("\n")
                        if x.strip()
                    ]

                    if not lines:

                        continue

                    title = lines[-1]

                    # Ignore obvious navigation text

                    bad_titles = {

                        "Events",
                        "Event",
                        "Calendar",
                        "Events Calendar",
                        "Upcoming Events",
                        "View All Events",
                        "Learn More",
                        "Search",
                        "Filter",
                        "Apply"
                    }

                    if title in bad_titles:

                        continue

                    add_event(

                        organization=
                        organization,

                        title=title,

                        start_date=event_date,

                        event_type=event_type,

                        link=url

                    )

                except Exception:

                    continue


    # ==========================================
    # UPDATE EVENTS
    # ==========================================

    with st.spinner(
        "🔄 Updating upcoming events..."
    ):

        scrape_generic(
            "American Diabetes Association",
            EVENT_SOURCES[
                "American Diabetes Association"
            ],
            "Scientific / Professional"
        )

        scrape_generic(
            "Breakthrough T1D",
            EVENT_SOURCES[
                "Breakthrough T1D"
            ],
            "Advocacy / Community"
        )

        scrape_generic(
            "Children with Diabetes",
            EVENT_SOURCES[
                "Children with Diabetes"
            ],
            "Patient / Family"
        )

        scrape_generic(
            "TrialNet",
            EVENT_SOURCES[
                "TrialNet"
            ],
            "Research / Screening"
        )

        scrape_generic(
            "T1D Exchange",
            EVENT_SOURCES[
                "T1D Exchange"
            ],
            "Research / Professional"
        )

        scrape_generic(
            "The Diabetes Link",
            EVENT_SOURCES[
                "The Diabetes Link"
            ],
            "Community / Advocacy"
        )

        scrape_generic(
            "Beyond Type 1",
            EVENT_SOURCES[
                "Beyond Type 1"
            ],
            "Community / Advocacy"
        )


    # ==========================================
    # CLEAN DATA
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

        events_df = events_df.sort_values(
            "Start Date"
        )

        events = events_df.to_dict(
            "records"
        )

    else:

        events = []


    # ==========================================
    # SOURCE STATUS
    # ==========================================

    st.markdown("### 📡 Event Data Status")

    status_cols = st.columns(4)

    total_events = len(events)

    organizations_found = len(
        set(
            event["Organization"]
            for event in events
        )
    )

    with status_cols[0]:

        st.metric(
            "📅 Events Found",
            total_events
        )

    with status_cols[1]:

        st.metric(
            "🏢 Organizations",
            organizations_found
        )

    with status_cols[2]:

        st.metric(
            "🔗 Official Calendars",
            len(EVENT_SOURCES)
        )

    with status_cols[3]:

        st.metric(
            "🔄 Data Driven",
            "Yes"
        )


    st.divider()


    # ==========================================
    # ORGANIZATION FILTER
    # ==========================================

    st.markdown("### 🔎 Upcoming Events")


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
        "Filter by organization",
        organization_options
    )


    # ==========================================
    # UPCOMING EVENTS
    # ==========================================

    today = pd.Timestamp.today().normalize()


    upcoming_events = [

        event
        for event in events

        if event["End Date"] >= today

    ]


    if (
        selected_organization
        != "All Organizations"
    ):

        upcoming_events = [

            event
            for event in upcoming_events

            if event["Organization"]
            == selected_organization

        ]


    upcoming_events = sorted(
        upcoming_events,
        key=lambda x: x["Start Date"]
    )


    if upcoming_events:

        for event in upcoming_events:

            with st.container(
                border=True
            ):

                col1, col2 = st.columns(
                    [5, 1]
                )


                with col1:

                    st.markdown(
                        f"### 📌 {event['Event']}"
                    )

                    st.caption(
                        f"**{event['Organization']}** "
                        f"• {event['Type']}"
                    )

                    if event["Location"]:

                        st.write(
                            f"📍 {event['Location']}"
                        )


                with col2:

                    if (
                        event["Start Date"]
                        == event["End Date"]
                    ):

                        date_text = (
                            event[
                                "Start Date"
                            ].strftime(
                                "%b %d, %Y"
                            )
                        )

                    else:

                        date_text = (

                            event[
                                "Start Date"
                            ].strftime(
                                "%b %d"
                            )

                            + " – "

                            + event[
                                "End Date"
                            ].strftime(
                                "%b %d, %Y"
                            )

                        )


                    st.markdown(
                        f"📅 **{date_text}**"
                    )


                    if event["Link"]:

                        st.link_button(
                            "View Event →",
                            event["Link"],
                            use_container_width=True
                        )


    else:

        st.info(
            "No upcoming events were found "
            "from the available event pages."
        )


    # ==========================================
    # FOOTER
    # ==========================================

    st.divider()

    st.caption(
        "Event information is pulled from public organization "
        "event pages when the dashboard loads. Use the official "
        "calendar links above for the most complete and current "
        "event information."
    )
