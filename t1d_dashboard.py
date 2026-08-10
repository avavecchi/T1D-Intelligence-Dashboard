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

# PAG DIRECTORY TAB
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
            "LinkedIn": "https://www.linkedin.com/company/beyond-type-1/",
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
        }

    }

    # ==========================================
    # DISPLAY ORGANIZATIONS
    # ==========================================

    pag_data = pd.read_csv("PAG_database.csv")

    # Remove Diabetes Leadership Council from the PAG Directory
    pag_data = pag_data[
        pag_data["Organization"] != "Diabetes Leadership Council"
    ]

    for index, row in pag_data.iterrows():

        organization = row["Organization"]

        # Use verified links when available.
        # Fall back to the CSV for organizations not listed above.
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

                if links["Website"]:
                    st.link_button(
                        "🌐 Website",
                        links["Website"],
                        use_container_width=True
                    )

                if links["News"]:
                    st.link_button(
                        "📰 News",
                        links["News"],
                        use_container_width=True
                    )

                if links["Instagram"]:
                    st.link_button(
                        "📸 Instagram",
                        links["Instagram"],
                        use_container_width=True
                    )

            with col2:

                if links["LinkedIn"]:
                    st.link_button(
                        "💼 LinkedIn",
                        links["LinkedIn"],
                        use_container_width=True
                    )

                if links["X"]:
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

    st.header("📅 T1D Events & Opportunities")

    st.caption(
        "Upcoming conferences, webinars, research meetings, and advocacy events "
        "relevant to the Type 1 Diabetes community."
    )

    # ==========================================
    # EVENT DATA
    # ==========================================

    events = [

        {
            "Event": "ADA Scientific Sessions",
            "Type": "Scientific Conference",
            "Icon": "🔬",
            "Timing": "Annual",
            "Focus": "Diabetes research, clinical care, technology, and innovation",
            "Organization": "American Diabetes Association",
            "Link": "https://professional.diabetes.org/scientific-sessions"
        },

        {
            "Event": "ADA Professional Webinars",
            "Type": "Webinar",
            "Icon": "💻",
            "Timing": "Ongoing",
            "Focus": "Clinical updates, diabetes management, guidelines, and education",
            "Organization": "American Diabetes Association",
            "Link": "https://professional.diabetes.org/professional-development/upcoming-professional-webinars"
        },

        {
            "Event": "Breakthrough T1D Events",
            "Type": "Advocacy & Community",
            "Icon": "🤝",
            "Timing": "Ongoing",
            "Focus": "T1D research, advocacy, fundraising, and community engagement",
            "Organization": "Breakthrough T1D",
            "Link": "https://www.breakthrought1d.org/events/"
        },

        {
            "Event": "TrialNet Events",
            "Type": "Research",
            "Icon": "🧬",
            "Timing": "Ongoing",
            "Focus": "T1D screening, prevention, clinical trials, and disease progression",
            "Organization": "TrialNet",
            "Link": "https://trialnet.org/news-events/events"
        },

        {
            "Event": "ISPAD Congress",
            "Type": "Scientific Conference",
            "Icon": "🌎",
            "Timing": "Annual",
            "Focus": "Pediatric diabetes research, treatment, technology, and care",
            "Organization": "ISPAD",
            "Link": "https://www.ispad.org/"
        },

        {
            "Event": "Children with Diabetes Friends for Life",
            "Type": "Patient & Family Conference",
            "Icon": "💙",
            "Timing": "Annual",
            "Focus": "Education, peer support, technology, and family engagement",
            "Organization": "Children with Diabetes",
            "Link": "https://childrenwithdiabetes.com/events/"
        }

    ]


    # ==========================================
    # QUICK STATS
    # ==========================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📅 Events Tracked",
            len(events)
        )

    with col2:

        st.metric(
            "🔬 Research",
            len([
                e for e in events
                if e["Type"] in [
                    "Research",
                    "Scientific Conference"
                ]
            ])
        )

    with col3:

        st.metric(
            "🤝 Advocacy & Community",
            len([
                e for e in events
                if "Advocacy" in e["Type"]
                or "Patient" in e["Type"]
            ])
        )


    st.divider()


    # ==========================================
    # EVENT FILTER
    # ==========================================

    st.markdown("### 🔎 Explore Events")

    event_types = [
        "All Events"
    ] + sorted(
        list(set(
            event["Type"]
            for event in events
        ))
    )

    selected_type = st.selectbox(
        "Filter by event type",
        event_types
    )


    if selected_type == "All Events":

        filtered_events = events

    else:

        filtered_events = [
            event for event in events
            if event["Type"] == selected_type
        ]


    st.write("")


    # ==========================================
    # EVENT CARDS
    # ==========================================

    for event in filtered_events:

        with st.container(border=True):

            # Header row
            col1, col2 = st.columns(
                [5, 1]
            )

            with col1:

                st.markdown(
                    f"### {event['Icon']} {event['Event']}"
                )

                st.caption(
                    f"{event['Organization']}  •  {event['Type']}"
                )

            with col2:

                st.markdown(
                    f"**{event['Timing']}**"
                )


            st.write("")

            # Event description
            st.write(
                event["Focus"]
            )


            # Bottom information
            col1, col2 = st.columns(
                [4, 1]
            )

            with col1:

                st.markdown(
                    f"**Focus:** {event['Focus']}"
                )

            with col2:

                st.link_button(
                    "View Event →",
                    event["Link"],
                    use_container_width=True
                )


    # ==========================================
    # FOOTER
    # ==========================================

    st.divider()

    st.markdown(
        "### 💡 Why These Events Matter"
    )

    st.info(
        "These events provide opportunities to monitor emerging T1D research, "
        "clinical practice changes, patient advocacy priorities, diabetes "
        "technology developments, and broader trends across the T1D community."
    )
