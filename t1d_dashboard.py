import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="T1D Intelligence Dashboard",
    page_icon="🩺",
    layout="wide"
)


st.title("🩺 Type 1 Diabetes Intelligence Dashboard")
st.caption("Patient advocacy, research, policy, and social media hub")


tab1, tab2, tab3, tab4 = st.tabs([
    "📰 News",
    "🤝 PAG Directory",
    "📅 Events",
    "⭐ Daily Brief"
])


# NEWS TAB
with tab1:

    st.header("📰 T1D Advocacy News")

    st.caption("Latest updates directly from Type 1 Diabetes organizations")


    import feedparser


    organizations = {
        "American Diabetes Association": 
            "https://diabetes.org/rss.xml",

        "Breakthrough T1D":
            "https://www.breakthrought1d.org/feed/",

        "Beyond Type 1":
            "https://beyondtype1.org/feed/",

        "Children with Diabetes":
            "https://childrenwithdiabetes.com/feed/",

        "T1D Exchange":
            "https://t1dexchange.org/feed/"
    }


    for org, feed_url in organizations.items():

        st.subheader(org)

        try:

            feed = feedparser.parse(feed_url)

            articles = feed.entries[:3]


            if articles:

                for article in articles:

                    st.markdown(
                        f"**{article.title}**"
                    )

                    st.markdown(
                        f"[🔗 Read article]({article.link})"
                    )

                    st.divider()

            else:

                st.write(
                    "No recent updates available."
                )


        except:

            st.write(
                "Unable to load updates."
            )

# PAG DIRECTORY TAB
with tab2:

    st.header("🤝 T1D Patient Advocacy Organization Hub")


    pag_data = pd.read_csv("PAG_database.csv")


    for index, row in pag_data.iterrows():

        with st.expander(row["Organization"]):

            st.write(
                f"**Category:** {row['Category']}"
            )


            if pd.notna(row["Website"]):
                st.link_button(
                    "🌐 Website",
                    row["Website"]
                )


            if pd.notna(row["News"]):
                st.link_button(
                    "📰 News",
                    row["News"]
                )


            if pd.notna(row["Instagram"]):
                st.link_button(
                    "📸 Instagram",
                    row["Instagram"]
                )


            if pd.notna(row["LinkedIn"]):
                st.link_button(
                    "💼 LinkedIn",
                    row["LinkedIn"]
                )


            if pd.notna(row["X"]):
                st.link_button(
                    "🐦 X",
                    row["X"]
                )


            if pd.notna(row["YouTube"]):
                st.link_button(
                    "▶️ YouTube",
                    row["YouTube"]
                )


# EVENTS TAB
with tab3:

    st.header("📅 T1D Events")

    st.caption(
        "Upcoming diabetes conferences, webinars, and advocacy events"
    )


    events = [

        {
            "Event": "ADA Scientific Sessions",
            "Type": "Scientific Conference",
            "Focus": "Diabetes research, clinical care, innovation",
            "Organization": "American Diabetes Association",
            "Link": "https://professional.diabetes.org/scientific-sessions"
        },

        {
            "Event": "ADA Professional Webinars",
            "Type": "Webinar Series",
            "Focus": "Clinical updates, guidelines, diabetes management",
            "Organization": "American Diabetes Association",
            "Link": "https://professional.diabetes.org/professional-development/upcoming-professional-webinars"
        },

        {
            "Event": "Breakthrough T1D Events",
            "Type": "Advocacy & Community",
            "Focus": "T1D research, advocacy, community engagement",
            "Organization": "Breakthrough T1D",
            "Link": "https://www.breakthrought1d.org/events/"
        },

        {
            "Event": "Clinical Research Updates",
            "Type": "Research",
            "Focus": "Early-stage T1D, screening, disease modification",
            "Organization": "TrialNet",
            "Link": "https://www.trialnet.org/events"
        }

    ]


    for event in events:

        st.subheader(event["Event"])

        st.write(
            f"""
            **Type:** {event["Type"]}

            **Organization:** {event["Organization"]}

            **Focus:** {event["Focus"]}
            """
        )

        st.link_button(
            "View Event",
            event["Link"]
        )

        st.divider()

# DAILY BRIEF TAB

with tab4:

    st.header("⭐ Daily T1D Intelligence Brief")

    today = pd.Timestamp.today().strftime("%B %d, %Y")

    st.caption(
        f"Daily summary of the latest Type 1 Diabetes advocacy, research, "
        f"policy, and community developments — {today}"
    )


    # ==========================================
    # NEWS SOURCES
    # ==========================================

    import feedparser

    organizations = {

        "American Diabetes Association":
            "https://diabetes.org/rss.xml",

        "Breakthrough T1D":
            "https://www.breakthrought1d.org/feed/",

        "Beyond Type 1":
            "https://beyondtype1.org/feed/",

        "Children with Diabetes":
            "https://childrenwithdiabetes.com/feed/",

        "T1D Exchange":
            "https://t1dexchange.org/feed/"
    }


    # ==========================================
    # COLLECT NEWS
    # ==========================================

    all_articles = []

    for organization, feed_url in organizations.items():

        try:

            feed = feedparser.parse(feed_url)

            for article in feed.entries[:5]:

                title = article.get(
                    "title",
                    "Untitled"
                )

                link = article.get(
                    "link",
                    ""
                )

                summary = article.get(
                    "summary",
                    ""
                )

                all_articles.append({

                    "Organization": organization,

                    "Title": title,

                    "Link": link,

                    "Summary": summary

                })

        except Exception:

            continue


    # ==========================================
    # DASHBOARD METRICS
    # ==========================================

    st.markdown("### 📊 Today's Intelligence")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Sources Monitored",
            len(organizations)
        )

    with col2:

        st.metric(
            "Updates Found",
            len(all_articles)
        )

    with col3:

        st.metric(
            "Organizations",
            len(set(
                article["Organization"]
                for article in all_articles
            ))
        )


    st.divider()


    # ==========================================
    # TOP STORIES
    # ==========================================

    st.markdown("## 🔥 Top T1D Updates")

    if all_articles:

        # Show the first 8 updates
        top_articles = all_articles[:8]

        for article in top_articles:

            st.subheader(
                article["Title"]
            )

            st.write(
                f"**Source:** {article['Organization']}"
            )

            if article["Summary"]:

                summary = article["Summary"]

                # Remove HTML if present
                import re

                summary = re.sub(
                    "<.*?>",
                    "",
                    summary
                )

                # Keep it short
                if len(summary) > 500:

                    summary = summary[:500] + "..."

                st.write(summary)

            st.link_button(
                "🔗 Read Full Article",
                article["Link"]
            )

            st.divider()

    else:

        st.warning(
            "No current updates were found. "
            "Try refreshing the page."
        )


    # ==========================================
    # ADVOCACY
    # ==========================================

    st.markdown("## 🤝 Advocacy & Patient Community")

    advocacy_keywords = [
        "advocacy",
        "patient",
        "community",
        "awareness",
        "support",
        "fundraising",
        "access",
        "policy"
    ]

    advocacy_articles = [

        article for article in all_articles

        if any(
            keyword in article["Title"].lower()
            for keyword in advocacy_keywords
        )
    ]


    if advocacy_articles:

        for article in advocacy_articles[:5]:

            st.write(
                f"**{article['Title']}**"
            )

            st.caption(
                article["Organization"]
            )

            st.link_button(
                "Read Update",
                article["Link"]
            )

    else:

        st.info(
            "No major advocacy-specific updates were identified "
            "in the current feeds."
        )


    # ==========================================
    # RESEARCH
    # ==========================================

    st.markdown("## 🔬 Research & Scientific Developments")

    research_keywords = [
        "research",
        "study",
        "clinical trial",
        "trial",
        "therapy",
        "treatment",
        "drug",
        "immunotherapy",
        "screening",
        "beta cell",
        "c-peptide",
        "teplizumab",
        "t1d"
    ]

    research_articles = [

        article for article in all_articles

        if any(
            keyword in article["Title"].lower()
            for keyword in research_keywords
        )
    ]


    if research_articles:

        for article in research_articles[:5]:

            st.write(
                f"**{article['Title']}**"
            )

            st.caption(
                article["Organization"]
            )

            st.link_button(
                "🔬 Read Research Update",
                article["Link"]
            )

    else:

        st.info(
            "No research-specific updates were identified "
            "in the current feeds."
        )


    # ==========================================
    # POLICY / ACCESS
    # ==========================================

    st.markdown("## 🏛️ Policy, Access & Healthcare")

    policy_keywords = [
        "policy",
        "legislation",
        "insurance",
        "coverage",
        "access",
        "medicaid",
        "medicare",
        "healthcare",
        "guideline",
        "advocacy"
    ]

    policy_articles = [

        article for article in all_articles

        if any(
            keyword in article["Title"].lower()
            for keyword in policy_keywords
        )
    ]


    if policy_articles:

        for article in policy_articles[:5]:

            st.write(
                f"**{article['Title']}**"
            )

            st.caption(
                article["Organization"]
            )

            st.link_button(
                "🏛️ Read Update",
                article["Link"]
            )

    else:

        st.info(
            "No major policy or healthcare access updates "
            "were identified."
        )


    # ==========================================
    # KEY TAKEAWAY
    # ==========================================

    st.divider()

    st.markdown("## 💡 Today's Key Takeaway")

    if all_articles:

        organizations_found = list(
            set(
                article["Organization"]
                for article in all_articles
            )
        )

        st.info(
            f"Today's intelligence includes {len(all_articles)} "
            f"updates across {len(organizations_found)} T1D organizations. "
            f"Review the research, advocacy, and policy sections above "
            f"to identify the developments most relevant to T1D patients, "
            f"caregivers, healthcare professionals, and industry stakeholders."
        )

    else:

        st.info(
            "No current intelligence is available today."
        )
