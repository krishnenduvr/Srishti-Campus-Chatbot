import html
import textwrap

import streamlit as st
from chatbot import get_response


st.set_page_config(
    page_title="Srishti Campus",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded",
)


COURSES = [
    "Python with Data Science",
    "Digital Marketing",
    "AI and Machine Learning",
    "Data Analytics",
    "Automation Testing",
    "Robotics",
]

WEBSITE_URL = "https://www.srishticampus.in"
MAP_URL = "https://www.google.com/maps/place/Srishti+Campus/@8.5576777,76.8761087,17z"
WELCOME_MESSAGE = (
    "Hello. I am the Srishti Campus assistant. Ask me about courses, admissions, "
    "contact details, placement support, or campus information."
)


def safe_rerun() -> None:
    rerun_fn = getattr(st, "rerun", None) or getattr(st, "experimental_rerun", None)
    if rerun_fn is not None:
        rerun_fn()


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

        :root {
            --surface: rgba(255, 255, 255, 0.84);
            --border: rgba(17, 62, 110, 0.14);
            --text: #10233d;
            --muted: #5d718b;
            --navy: #0c2d57;
            --blue: #1768ac;
            --teal: #0ea5a4;
            --shadow: 0 24px 60px rgba(12, 45, 87, 0.12);
        }

        html, body, [class*="css"] {
            font-family: 'Manrope', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(79, 172, 254, 0.16), transparent 28%),
                radial-gradient(circle at top right, rgba(14, 165, 164, 0.16), transparent 24%),
                linear-gradient(180deg, #edf5fb 0%, #f7fbff 52%, #eef4f9 100%);
            color: var(--text);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0c2d57 0%, #143b6f 100%);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }

        [data-testid="stSidebar"] * {
            color: #f3f8ff !important;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1180px;
        }

        .hero-shell {
            position: relative;
            overflow: hidden;
            padding: 2.8rem;
            border-radius: 28px;
            background: linear-gradient(135deg, rgba(12, 45, 87, 0.98), rgba(22, 104, 172, 0.92));
            color: white;
            box-shadow: var(--shadow);
            margin-bottom: 1.4rem;
        }

        .hero-shell::after {
            content: "";
            position: absolute;
            inset: auto -80px -120px auto;
            width: 280px;
            height: 280px;
            background: radial-gradient(circle, rgba(255,255,255,0.24), transparent 68%);
        }

        .eyebrow {
            display: inline-block;
            padding: 0.45rem 0.9rem;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.16);
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .hero-title {
            font-size: clamp(2rem, 3vw, 3.4rem);
            line-height: 1.05;
            font-weight: 800;
            margin: 0;
            max-width: 700px;
        }

        .hero-copy {
            color: rgba(255, 255, 255, 0.84);
            font-size: 1.05rem;
            line-height: 1.8;
            max-width: 650px;
            margin-top: 1rem;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.9rem;
            margin-top: 1.6rem;
        }

        .stat-card, .info-card, .chat-shell {
            background: var(--surface);
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            backdrop-filter: blur(14px);
        }

        .stat-card {
            border-radius: 20px;
            padding: 1rem 1.1rem;
        }

        .stat-value {
            color: white;
            font-size: 1.6rem;
            font-weight: 800;
        }

        .stat-label {
            color: rgba(255, 255, 255, 0.72);
            font-size: 0.92rem;
        }

        .section-title {
            font-size: 1.25rem;
            font-weight: 800;
            margin: 0.2rem 0 0.8rem 0;
            color: var(--navy);
        }

        .info-card {
            border-radius: 22px;
            padding: 1.3rem;
            height: 100%;
        }

        .info-card h3 {
            margin: 0 0 0.7rem 0;
            color: var(--navy);
            font-size: 1.05rem;
        }

        .info-card p, .info-card li {
            color: var(--muted);
            line-height: 1.75;
            font-size: 0.97rem;
        }

        .info-card ul {
            padding-left: 1rem;
            margin-bottom: 0;
        }

        .mini-badge {
            display: inline-block;
            color: var(--blue);
            background: rgba(23, 104, 172, 0.1);
            border-radius: 999px;
            padding: 0.3rem 0.7rem;
            font-size: 0.75rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
        }

        .chat-shell {
            border-radius: 24px;
            padding: 1.2rem;
            margin-top: 0.4rem;
        }

        .chat-intro {
            padding: 1rem 1.1rem 0.4rem 1.1rem;
        }

        .chat-intro h3 {
            margin: 0;
            color: var(--navy);
        }

        .chat-intro p {
            margin: 0.55rem 0 0 0;
            color: var(--muted);
            line-height: 1.7;
        }

        .chat-history {
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
            margin: 1rem 0 1.2rem 0;
        }

        .chat-bubble {
            border-radius: 18px;
            border: 1px solid var(--border);
            background: rgba(255, 255, 255, 0.82);
            padding: 1rem 1.1rem;
            box-shadow: 0 14px 30px rgba(12, 45, 87, 0.08);
        }

        .chat-bubble.user {
            background: linear-gradient(135deg, rgba(23, 104, 172, 0.14), rgba(14, 165, 164, 0.1));
            border-color: rgba(23, 104, 172, 0.2);
        }

        .chat-bubble.assistant {
            background: rgba(255, 255, 255, 0.9);
        }

        .chat-role {
            display: inline-block;
            margin-bottom: 0.45rem;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: var(--blue);
        }

        .chat-text {
            color: var(--text);
            line-height: 1.75;
            font-size: 0.98rem;
            white-space: pre-wrap;
        }

        div[data-testid="stForm"] {
            background: rgba(255, 255, 255, 0.7);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 1rem;
            box-shadow: var(--shadow);
        }

        div[data-testid="stTextInput"] input {
            border-radius: 14px;
            border: 1px solid rgba(17, 62, 110, 0.12);
            background: rgba(255, 255, 255, 0.95);
        }

        div[data-testid="stFormSubmitButton"] button {
            width: 100%;
        }

        .contact-band {
            margin-top: 1rem;
            padding: 1.2rem 1.3rem;
            border-radius: 22px;
            background: linear-gradient(135deg, rgba(14, 165, 164, 0.12), rgba(23, 104, 172, 0.08));
            border: 1px solid rgba(23, 104, 172, 0.12);
        }

        .contact-band p {
            margin: 0.35rem 0;
            color: var(--text);
        }

        .stButton button, .stDownloadButton button {
            border-radius: 999px;
            border: none;
            background: linear-gradient(135deg, #1768ac, #0ea5a4);
            color: white;
            font-weight: 700;
            padding: 0.7rem 1.2rem;
        }

        @media (max-width: 900px) {
            .hero-shell {
                padding: 2rem 1.3rem;
            }

            .stat-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero(title: str, description: str) -> None:
    st.markdown(
        f"""
        <section class="hero-shell">
            <div class="eyebrow">Srishti Campus</div>
            <h1 class="hero-title">{title}</h1>
            <p class="hero-copy">{description}</p>
            <div class="stat-grid">
                <div class="stat-card">
                    <div class="stat-value">Career-focused</div>
                    <div class="stat-label">Training aligned with practical industry skills</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">Live guidance</div>
                    <div class="stat-label">Support for admissions, courses and placement queries</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">24/7 assistant</div>
                    <div class="stat-label">Instant answers through the campus chatbot</div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_card(title: str, body: str, badge: str = "") -> None:
    badge_html = f'<div class="mini-badge">{badge}</div>' if badge else ""
    st.markdown(
        f"""
        <section class="info-card">
            {badge_html}
            <h3>{title}</h3>
            <p>{body}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_link_card(title: str, body: str, url: str, badge: str = "") -> None:
    badge_html = f'<div class="mini-badge">{badge}</div>' if badge else ""
    st.markdown(
        f"""
        <section class="info-card">
            {badge_html}
            <h3>{title}</h3>
            <p>{body}</p>
            <p><a href="{url}" target="_blank">{url}</a></p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def fetch_bot_reply(message: str) -> str:
    try:
        return get_response(message)
    except Exception:
        return "The chatbot is unavailable right now. Please try again in a moment."


def render_chat_bubble(role: str, content: str) -> None:
    role_label = "You" if role == "user" else "Srishti Bot"
    safe_content = html.escape(content)
    st.markdown(
        f"""
        <div class="chat-bubble {role}">
            <div class="chat-role">{role_label}</div>
            <div class="chat-text">{safe_content}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_home() -> None:
    render_hero(
        "Learn faster, get guided better, and explore Srishti Campus in one place.",
        "A polished campus assistant for course discovery, admissions guidance, contact details, and instant chatbot support designed with a modern Srishti-inspired visual style.",
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        render_card(
            "Courses and skills",
            "Explore training tracks built for students, freshers, and professionals who want practical software and digital skills.",
            "Programs",
        )
    with col2:
        render_card(
            "Project-based learning",
            "Hands-on assignments, real-world exposure, and structured mentorship help learners build confidence beyond theory.",
            "Experience",
        )
    with col3:
        render_card(
            "Chatbot assistance",
            "Use the assistant to ask about admissions, learning modes, placement support, campus details, and more.",
            "Support",
        )

    st.markdown('<h2 class="section-title">What this assistant can help with</h2>', unsafe_allow_html=True)
    left, right = st.columns([1.25, 1])
    with left:
        st.markdown(
            """
            <section class="info-card">
                <h3>Campus support, organized clearly</h3>
                <ul>
                    <li>Course information and learning paths</li>
                    <li>Admission-related questions</li>
                    <li>Placement overview and career guidance</li>
                    <li>Contact details and location access</li>
                    <li>Instant responses through the integrated bot</li>
                </ul>
            </section>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            """
            <section class="info-card">
                <h3>Why the new layout feels more professional</h3>
                <p>The interface now uses a branded hero section, glass-style content cards, stronger spacing, a cleaner sidebar, and a proper chat experience that behaves more like a modern website than a basic form.</p>
            </section>
            """,
            unsafe_allow_html=True,
        )


def render_about() -> None:
    render_hero(
        "Industry-oriented training built to move students toward real careers.",
        "Srishti Campus combines practical teaching, mentorship, and placement support to help learners turn technical skills into employable confidence.",
    )
    col1, col2 = st.columns(2)
    with col1:
        render_card(
            "Who we are",
            "Srishti Campus is a software training and career development institute in Thiruvananthapuram, Kerala, operating under Srishti Innovative Computer Systems Pvt. Ltd. and focused on practical, industry-aligned learning.",
            "About",
        )
        render_card(
            "What we offer",
            "Training spans web development, mobile applications, data science, AI/ML, software testing, cloud technologies, digital marketing, internships, and academic project support.",
            "Offerings",
        )
    with col2:
        render_card(
            "Why students choose Srishti",
            "Learners benefit from experienced mentors, structured modules, live projects, workshops, and training built around current market expectations rather than only classroom theory.",
            "Value",
        )
        render_card(
            "Placement support",
            "The campus supports interview preparation, career guidance, and job-readiness so students can move from training into real opportunities with stronger confidence.",
            "Careers",
        )


def render_contact() -> None:
    render_hero(
        "Reach the campus team quickly and clearly.",
        "Everything important is grouped here so students can connect with Srishti Campus without hunting through multiple pages.",
    )
    st.markdown(
        """
        <section class="contact-band">
            <p><strong>Address:</strong> Srishti Campus, Technopark Phase 1, Kazhakkuttam, Trivandrum, 695582, Kerala, India</p>
            <p><strong>Phone:</strong> +91 9778616059</p>
            <p><strong>Email:</strong> srishticampus@gmail.com</p>
            <p><strong>Website:</strong> https://www.srishticampus.in</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        render_link_card(
            "Visit online",
            "Open the official website for additional institute information, updates, and service details.",
            WEBSITE_URL,
            "Website",
        )
    with col2:
        render_link_card(
            "Find the campus",
            "Use the map link to reach the Technopark location directly.",
            MAP_URL,
            "Location",
        )


def render_placement() -> None:
    render_hero(
        "Training that stays connected to hiring outcomes.",
        "Placement support is a core part of the student journey, with practical learning, mock interviews, and guided preparation for software roles.",
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        render_card("Placement record", "Srishti Campus highlights a strong placement track supported by career-focused programs and project exposure.", "Results")
    with col2:
        render_card("Preparation model", "Students receive support through mock interviews, resume guidance, communication practice, and job-readiness sessions.", "Preparation")
    with col3:
        render_card("Career paths", "Opportunities typically align with software development, testing, data, AI/ML, and related digital roles.", "Roles")


def render_chatbot() -> None:
    render_hero(
        "Ask a question and get an instant campus response.",
        "The chat box now submits when the user presses Enter, making the experience feel closer to a real support assistant.",
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [{"role": "assistant", "content": WELCOME_MESSAGE}]

    st.markdown(
        """
        <section class="chat-shell">
            <div class="chat-intro">
                <h3>Campus Chat</h3>
                <p>Type your message below and press Enter to send. The bot answer will appear immediately in the chat thread.</p>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="chat-history">', unsafe_allow_html=True)
    for message in st.session_state.chat_history:
        render_chat_bubble(message["role"], message["content"])
    st.markdown("</div>", unsafe_allow_html=True)

    with st.form("chat_form", clear_on_submit=True):
        prompt = st.text_input(
            "Ask about Srishti Campus",
            placeholder="Type your question and press Enter",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button("Send")

    if submitted and prompt.strip():
        st.session_state.chat_history.append({"role": "user", "content": prompt.strip()})
        bot_reply = fetch_bot_reply(prompt.strip())
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
        safe_rerun()

    if st.button("Clear conversation"):
        st.session_state.chat_history = [{"role": "assistant", "content": WELCOME_MESSAGE}]
        safe_rerun()


def render_sidebar() -> str:
    st.sidebar.markdown("## Srishti Campus")
    st.sidebar.caption("AI-powered campus guide")
    page = st.sidebar.radio(
        "Navigate",
        ["Home", "About Srishti Campus", "Contact", "Placement", "Chat Bot"],
        label_visibility="collapsed",
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Courses Offered")
    for course in COURSES:
        st.sidebar.markdown(f"- {course}")
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        textwrap.dedent(
            """
            <div style="padding:0.9rem 0.95rem;border-radius:18px;background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.12);">
                <div style="font-weight:700;margin-bottom:0.35rem;">Designed for quick support</div>
                <div style="font-size:0.92rem;line-height:1.6;">
                    Use the Chat Bot page for instant answers. Press Enter after typing your question.
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )
    return page


def main() -> None:
    inject_styles()
    page = render_sidebar()

    if page == "Home":
        render_home()
    elif page == "About Srishti Campus":
        render_about()
    elif page == "Contact":
        render_contact()
    elif page == "Placement":
        render_placement()
    else:
        render_chatbot()


if __name__ == "__main__":
    main()
