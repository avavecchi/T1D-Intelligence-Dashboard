import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="T1D Intelligence Dashboard",
    page_icon="🩺",
    layout="wide"
)


st.title("🩺 Type 1 Diabetes Intelligence Dashboard")
st.caption("Patient advocacy, research, policy, and social media hub")


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📰 News",
    "🤝 PAG Directory",
    "🔬 Research",
    "📅 Events",
    "⭐ Daily Brief"
])


# NEWS TAB
with tab1:

    st.header("📰 T1D Advocacy News")

    st.write(
        "Daily news updates from diabetes organizations will appear here."
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



# RESEARCH TAB
with tab3:

    st.header("🔬 Research Resources")

    st.link_button(
        "PubMed",
        "https://pubmed.ncbi.nlm.nih.gov/"
    )

    st.link_button(
        "ClinicalTrials.gov",
        "https://clinicaltrials.gov/"
    )

    st.link_button(
        "TrialNet",
        "https://www.trialnet.org/"
    )



# EVENTS TAB
with tab4:

    st.header("📅 T1D Events")

    st.write(
        "Upcoming diabetes conferences, webinars, and advocacy events."
    )



# DAILY BRIEF TAB
with tab5:

    st.header("⭐ Daily T1D Intelligence Brief")

    st.caption("Summary of key advocacy, research, and policy updates")


    st.subheader("🔥 Top Advocacy Updates")

    st.write("""
    • Breakthrough T1D updates and advocacy initiatives  
    • American Diabetes Association announcements  
    • Patient community and education campaigns
    """)


    st.subheader("🔬 Research Highlights")

    st.write("""
    • Early-stage T1D screening developments  
    • Beta-cell preservation research  
    • Clinical trial updates
    """)


    st.subheader("🏛 Policy & Healthcare Updates")

    st.write("""
    • Screening guideline discussions  
    • Healthcare provider education initiatives  
    • Access and reimbursement updates
    """)


    st.subheader("📅 Upcoming Events")

    st.write("""
    • ADA Scientific Sessions  
    • ISPAD Congress  
    • Diabetes advocacy webinars
    """)


    st.subheader("💡 Key Takeaway")

    st.info(
        "Today's intelligence highlights opportunities to improve early T1D detection, "
        "increase stakeholder awareness, and strengthen patient advocacy efforts."
    )
