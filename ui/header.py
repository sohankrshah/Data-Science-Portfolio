import streamlit as st

def create_sidebar():
    """Create a fixed left sidebar navigation"""

    # Inject custom CSS for sidebar layout
    st.markdown("""
    <style>
    /* Sidebar container */
    .sidebar-container {
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        width: 220px;
        background-color: rgb(14, 17, 23);
        padding: 20px 15px;
        box-shadow: 2px 0 10px rgba(0,0,0,0.1);
        z-index: 999;
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    /* Logo section */
    .logo-section {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .company-name {
        color: white;
        font-size: 24px;
        font-weight: bold;
        margin: 0;
    }

    /* Navigation menu */
    .nav-menu {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .nav-item, .home-icon {
        color: white;
        text-decoration: none;
        font-weight: 500;
        font-size: 16px;
        padding: 10px 15px;
        border-radius: 8px;
        transition: all 0.3s ease;
        cursor: pointer;
        border: none;
        background: transparent;
        text-align: left;
    }

    .nav-item:hover, .home-icon:hover {
        background-color: rgba(255,255,255,0.1);
        transform: translateX(4px);
    }

    .nav-item.active, .home-icon.active {
        background-color: rgba(255,255,255,0.2);
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'
    current_page = st.session_state.current_page

    # Render sidebar HTML
    st.markdown(f"""
    <div class="sidebar-container">
        <div class="logo-section">
            <div class="company-name">KARTSBAZAR</div>
        </div>
        <nav class="nav-menu">
            <button class="home-icon {'active' if current_page == 'Home' else ''}" onclick="setPage('Home')">🏠 Home</button>
            <button class="nav-item {'active' if current_page == 'Overview' else ''}" onclick="setPage('Overview')">Overview</button>
            <button class="nav-item {'active' if current_page == 'Portfolio' else ''}" onclick="setPage('Portfolio')">Portfolio</button>
            <button class="nav-item {'active' if current_page == 'Contact' else ''}" onclick="setPage('Contact')">Contact Us</button>
        </nav>
    </div>
    """, unsafe_allow_html=True)

def get_current_page():
    """Return the current active page"""
    return st.session_state.get('current_page', 'Home')
