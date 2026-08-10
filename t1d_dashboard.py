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
        "Track upcoming conferences, webinars, research meetings, "
        "and advocacy opportunities across the Type 1 Diabetes community."
    )


    # ==========================================
    # EVENT DATA
    # ==========================================

    events = [

        {
            "Event": "ADA Scientific Sessions",
            "Type": "Scientific Conference",
            "Icon": "🔬",
            "Start Date": "2027-06-05",
            "End Date": "2027-06-08",
            "Focus": "Diabetes research, clinical care, technology, and innovation",
            "Organization": "American Diabetes Association",
            "Link": "https://professional.diabetes.org/scientific-sessions"
        },

        {
            "Event": "ADA Professional Webinars",
            "Type": "Webinar",
            "Icon": "💻",
            "Start Date": "2026-08-20",
            "End Date": "2026-08-20",
            "Focus": "Clinical updates, diabetes management, guidelines, and education",
            "Organization": "American Diabetes Association",
            "Link": "https://professional.diabetes.org/professional-development/upcoming-professional-webinars"
        },

        {
            "Event": "Breakthrough T1D Events",
            "Type": "Advocacy & Community",
            "Icon": "🤝",
            "Start Date": "2026-09-01",
            "End Date": "2026-09-01",
            "Focus": "T1D research, advocacy, fundraising, and community engagement",
            "Organization": "Breakthrough T1D",
            "Link": "https://www.breakthrought1d.org/events/"
        },

        {
            "Event": "TrialNet Events",
            "Type": "Research",
            "Icon": "🧬",
            "Start Date": "2026-09-15",
            "End Date": "2026-09-15",
            "Focus": "T1D screening, prevention, clinical trials, and disease progression",
            "Organization": "TrialNet",
            "Link": "https://trialnet.org/news-events/events"
        },

        {
            "Event": "ISPAD Congress",
            "Type": "Scientific Conference",
            "Icon": "🌎",
            "Start Date": "2026-10-01",
            "End Date": "2026-10-04",
            "Focus": "Pediatric diabetes research, treatment, technology, and care",
            "Organization": "ISPAD",
            "Link": "https://www.ispad.org/"
        },

        {
            "Event": "Children with Diabetes Friends for Life",
            "Type": "Patient & Family Conference",
            "Icon": "💙",
            "Start Date": "2026-07-14",
            "End Date": "2026-07-18",
            "Focus": "Education, peer support, technology, and family engagement",
            "Organization": "Children with Diabetes",
            "Link": "https://childrenwithdiabetes.com/events/"
        }

    ]


    # ==========================================
    # CONVERT DATES
    # ==========================================

    for event in events:

        event["Start Date"] = pd.to_datetime(
            event["Start Date"]
        )

        event["End Date"] = pd.to_datetime(
            event["End Date"]
        )


    # ==========================================
    # MONTH NAVIGATION
    # ==========================================

    if "calendar_month" not in st.session_state:

        st.session_state.calendar_month = pd.Timestamp.today().replace(
            day=1
        )


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
                - pd.DateOffset(months=1)
            )

            st.rerun()


    with col2:

        st.markdown(
            f"<h2 style='text-align:center;'>"
            f"{st.session_state.calendar_month.strftime('%B %Y')}"
            f"</h2>",
            unsafe_allow_html=True
        )


    with col3:

        if st.button(
            "Next →",
            use_container_width=True
        ):

            st.session_state.calendar_month = (
                st.session_state.calendar_month
                + pd.DateOffset(months=1)
            )

            st.rerun()


    # ==========================================
    # TODAY BUTTON
    # ==========================================

    if st.button(
        "📍 Jump to Today"
    ):

        st.session_state.calendar_month = pd.Timestamp.today().replace(
            day=1
        )

        st.rerun()


    st.divider()


    # ==========================================
    # CALENDAR
    # ==========================================

    calendar_month = st.session_state.calendar_month

    month_start = calendar_month

    month_end = (
        calendar_month
        + pd.offsets.MonthEnd(1)
    )


    # Monday = 0
    first_weekday = month_start.weekday()

    days_in_month = month_end.day


    # Calendar weekday headers

    weekday_names = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]


    header_cols = st.columns(7)

    for i, day_name in enumerate(
        weekday_names
    ):

        with header_cols[i]:

            st.markdown(
                f"<div style='text-align:center; "
                f"font-weight:bold; "
                f"padding:8px;'>"
                f"{day_name}"
                f"</div>",
                unsafe_allow_html=True
            )


    # ==========================================
    # CALENDAR DAYS
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

                # Empty cells before month begins

                if cell_number < first_weekday:

                    st.markdown(
                        "<div style='"
                        "height:115px;"
                        "'></div>",
                        unsafe_allow_html=True
                    )

                    continue


                # Empty cells after month ends

                if day_number > days_in_month:

                    st.markdown(
                        "<div style='"
                        "height:115px;"
                        "'></div>",
                        unsafe_allow_html=True
                    )

                    continue


                current_date = pd.Timestamp(
                    year=calendar_month.year,
                    month=calendar_month.month,
                    day=day_number
                )


                # ==================================
                # EVENTS ON THIS DAY
                # ==================================

                day_events = []


                for event in events:

                    if (
                        event["Start Date"]
                        <= current_date
                        <= event["End Date"]
                    ):

                        day_events.append(
                            event
                        )


                # ==================================
                # DAY CONTAINER
                # ==================================

                with st.container(
                    border=True
                ):

                    # Highlight today

                    if (
                        current_date.date()
                        == pd.Timestamp.today().date()
                    ):

                        st.markdown(
                            f"**📍 {day_number}**"
                        )

                    else:

                        st.markdown(
                            f"**{day_number}**"
                        )


                    # Show events

                    for event in day_events:

                        st.markdown(
                            f"{event['Icon']} "
                            f"**{event['Event']}**"
                        )


                        st.caption(
                            event["Type"]
                        )


                    # Empty space keeps calendar consistent

                    if not day_events:

                        st.write("")


                day_number += 1


    # ==========================================
    # EVENT LEGEND
    # ==========================================

    st.divider()

    st.markdown(
        "### 🗂️ Event Categories"
    )


    legend_col1, legend_col2, legend_col3, legend_col4 = st.columns(4)


    with legend_col1:

        st.markdown(
            "🔬 **Research / Scientific**"
        )


    with legend_col2:

        st.markdown(
            "🤝 **Advocacy & Community**"
        )


    with legend_col3:

        st.markdown(
            "💻 **Webinars**"
        )


    with legend_col4:

        st.markdown(
            "💙 **Patient & Family**"
        )


    # ==========================================
    # UPCOMING EVENTS
    # ==========================================

    st.divider()

    st.markdown(
        "### 📌 Upcoming Events"
    )


    today = pd.Timestamp.today()


    upcoming_events = sorted(
        [
            event
            for event in events
            if event["End Date"] >= today
        ],
        key=lambda x: x["Start Date"]
    )


    for event in upcoming_events[:5]:

        with st.container(
            border=True
        ):

            col1, col2 = st.columns(
                [4, 1]
            )


            with col1:

                st.markdown(
                    f"### {event['Icon']} "
                    f"{event['Event']}"
                )

                st.caption(
                    f"{event['Organization']} • "
                    f"{event['Type']}"
                )

                st.write(
                    event["Focus"]
                )


            with col2:

                if (
                    event["Start Date"]
                    == event["End Date"]
                ):

                    date_text = event[
                        "Start Date"
                    ].strftime(
                        "%b %d, %Y"
                    )

                else:

                    date_text = (
                        event["Start Date"].strftime(
                            "%b %d"
                        )
                        + " – "
                        + event["End Date"].strftime(
                            "%b %d, %Y"
                        )
                    )


                st.markdown(
                    f"📅 **{date_text}**"
                )


                st.link_button(
                    "View Event →",
                    event["Link"],
                    use_container_width=True
                )


    # ==========================================
    # FOOTER
    # ==========================================

    st.divider()

    st.info(
        "Use the calendar to monitor upcoming T1D scientific meetings, "
        "research activities, advocacy opportunities, webinars, and "
        "patient-focused events."
    )
