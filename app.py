import streamlit as st
import base64
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)
set_bg("image.jpg")
st.sidebar.title("⚙️ Settings")
page = st.sidebar.radio("", ["🏠 Home","🏫 About Srishti Campus", "📞 Contact","💼 Placement","🤖 Chat Bot"])
st.title("🎓 Srishti Campus")
st.markdown(
    """
    <style>
    /* 🎨 Change all main text color */
    html, body, [class*="st-"] {
        color: #1F2D3D !important;  /* Replace this with any color you like */
    }

    /* 🚫 But keep sidebar (settings) text color unchanged */
    section[data-testid="stSidebar"] * {
        color: inherit !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
if page=="🏠 Home":
    st.write("""
    ###  Hello!  
    Welcome to the official AI-powered assistant of **Srishti Campus**.

    This chatbot helps you with:
    - 📘 Course details  
    - 📝 Admission procedures  
    - 🕒Mode of learning  
    - 📞 Contact information  
    - 🏫 Campus information  

    Start chatting anytime — your virtual guide is here **24×7**!
    """)
elif page == "🏫 About Srishti Campus":
            st.header("About Srishti Campus")
            st.write("""
                 Srishti Campus is growing as one of the Universal skills development Corporation,
                 in building skilled engineers to meet the Universal IT market needs.
                 Srishti Campus is an ISO 9001 : 2008 certified corporate training wing of Srishti Innovative Computer Systems Pvt. Ltd. Located in Technopark.

                ### 🚀 Who We Are
                Established with a mission to bridge the gap between academic learning and industry demands,  
                Srishti Campus provides practical, project-focused training that equips learners with the skills 
                required to succeed in today’s competitive IT environment.

                ### 🎓 What We Offer
                - Training in Web Development (PHP, .NET), Mobile App Development (Android & iOS), and other modern technologies.
                - End‑to‑end programs covering technology learning, design, development, delivery, and assessment.
                - Hands‑on labs, instructor‑led courseware, libraries, free seminars, and practical workshops.
                - Special packages introduced during the 10th year celebrations to support freshers in building a better future.

                ### 🧑‍🏫 Why Choose Srishti Campus?
                - Proven track record: 70+ companies have hired trained professionals from Srishti Campus.
                - 100% placement achievement since 2016, with continuous focus on securing student futures.
                - Experienced mentors and industry masters guiding students with clear‑cut curriculum.
                - Training team dedicated to delivering knowledge in the latest IT software industry trends.
                - Programs designed for working professionals, freshers, and career switchers.

                ### 💼 Placement Support
                With a strong industry network, Srishti Campus maintains an excellent placement record,  
                helping students secure positions in top companies across Kerala, Bengaluru, and other major cities.  
                The dedicated placement team provides interview preparation, career guidance, and continuous support.

                ### 🌐 Our Vision
                - To empower students with the skills and confidence to build successful IT careers.
                - To act as a bridge between academic learning and industry demand.
                - To ensure every student who joins Srishti Campus follows a path toward an exponential career.
                - To create professionals who meet industry demand, equipped with best practices, SDLC knowledge,and awareness of technological advancements.
                    """)

elif page == "📞 Contact":
    st.header("Contact Srishti Campus")
    st.write("""
    📍 **Address:** Srishti Campus,Technopark Phase 1, Kazhakkuttam, Trivandrum ,695582, Kerala, india  
    📞 **Phone:** +91-9744010829  
    ✉️ **Email:** srishticampus@gmail.com  
    🌐 **Website:** [www.srishticampus.in](https://www.srishticampus.in)  
    📌 **Location:** [View on Google Maps](https://www.google.com/maps/place/Srishti+Campus/@8.5601677,76.8733984,15.82z/data=!4m6!3m5!1s0x3b05b95e87b42537:0x5d73d1ce107e6a53!8m2!3d8.5576777!4d76.8761087!16s%2Fg%2F119x3z4h_)
    """)
elif page == "💼 Placement":
    st.header("💼 Placement Summary")

    st.write("""
    Become a part of our placement journey with Srishti Campus.
    More than just placement assistance — we prepare you to enter the IT industry with confidence.
    Opportunities to learn add‑on skills: aptitude, attitude, resume building, and more.

    ### ⭐ Placement Highlights
    - Personalized guidance: we understand your skills and goals to tailor our services.
    - Strong industry network and matching tools to connect you with the right opportunities.
    - End‑to‑end support: application process, interview preparation, job placement, and transition into your new role.
    - Your success is our priority.

    ### 🎯 Why Our Students Get Placed
    - Continuous skill development beyond technical training (aptitude, attitude, communication).
    - Resume building workshops and interview coaching.
    - 100% placement focus with proven track record.
    - Real success stories: watch videos of successfully placed candidates sharing their journeys.
    """)

elif page == "🤖 Chat Bot":
    st.write("💬 Welcome! Ask me anything about Srishti Campus.")
    from chatbot import get_bot_response
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    user_message = st.text_input("Type your message:")
    if st.button("Ask Bot"):
        if user_message.strip() != "":
            st.session_state.chat_history.append(("You", user_message))
            bot_reply = get_bot_response(user_message)
            st.session_state.chat_history.append(("Bot", bot_reply))
    st.subheader("💬 Chat with Bot:")
    for sender, message in st.session_state.chat_history:
        if sender == "You":
            st.markdown(
                f"<div style='background-color:#e6f3ff;padding:8px;border-radius:10px;margin-bottom:5px;'><b>🧑‍💻 You:</b> {message}</div>",
                unsafe_allow_html=True)
        else:
            st.markdown(
                f"<div style='background-color:#f0fff0;padding:8px;border-radius:10px;margin-bottom:5px;'><b>🤖 Bot:</b> {message}</div>",
                unsafe_allow_html=True)


st.sidebar.markdown("### 🎓 Courses Offered")
st.sidebar.markdown("""
- 📘 Python   
- 📗 Java 
- 📓 Digital Marketing 
- 📙 Software Testing  
- 📕 Web Designing 
- 📒 Mean Stack  
- 📔 MySQL
- 📘 Android Full Stack
- 📗 Datascience Using Python
""")