# ============================================================
# STYLES DAN KONFIGURASI CSS - SISTEM KLASIFIKASI BSM
# ============================================================

import streamlit as st
import plotly.graph_objects as go

def load_custom_css():
    """Memuat custom CSS untuk aplikasi Streamlit."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Bungee&family=IBM+Plex+Mono:wght@400;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    /* ===== GLOBAL VARIABLES ===== */
    :root {
        --blue: #2146FF;
        --yellow: #FFE500;
        --black: #000000;
        --white: #FFFFFF;
        --gray: #F2F2F2;
        --cyan: #00F5FF;
        --red: #FF2D2D;
        --lime: #B6FF00;
        --purple: #9B00FF;
        --border: 3px solid #000;
        --border-thick: 5px solid #000;
        --shadow: 6px 6px 0px #000;
        --shadow-sm: 4px 4px 0px #000;
        --shadow-lg: 8px 8px 0px #000;
        --shadow-hover: 2px 2px 0px #000;
    }
    
    html, body {
        font-family: 'Space Grotesk', sans-serif;
        background: #F2F2F2;
    }
    
    /* dot grid background */
    .main {
        background-image: radial-gradient(circle, #00000018 1px, transparent 1px);
        background-size: 22px 22px;
        background-color: #F2F2F2;
    }
    
    .main .block-container {
        padding: 1.2rem 2rem 3rem;
        max-width: 1440px;
    }
    
    /* ===== STICKY HEADER ===== */
    .sticky-header {
        position: fixed;
        top: 3.8rem;
        left: 18rem;
        right: 1rem;
        z-index: 999999;
        background: var(--yellow);
        border: var(--border-thick);
        box-shadow: var(--shadow);
        padding: 0.85rem 1.4rem;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .sticky-header-spacer { height: 100px; }
    .sticky-header-icon {
        width: 40px;
        height: 40px;
        min-width: 40px;
        background: var(--blue);
        border: var(--border);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        color: white;
    }
    .sticky-header-title {
        font-family: 'Archivo Black', sans-serif;
        font-size: 1.3rem;
        font-weight: 900;
        color: var(--black);
        text-transform: uppercase;
        letter-spacing: 0.02em;
        white-space: nowrap;
    }
    @media (max-width: 768px) {
        .sticky-header { left: 1rem; right: 1rem; top: 4rem; }
    }
    
    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] > div:first-child {
        background: var(--blue) !important;
        border-right: 5px solid var(--black) !important;
    }
    [data-testid="stSidebar"] * {
        color: var(--white) !important;
    }
    [data-testid="stSidebar"] label {
        color: var(--yellow) !important;
        font-family: 'Archivo Black', sans-serif !important;
        font-weight: 900 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        font-size: 0.7rem !important;
    }
    [data-testid="stSidebar"] .stRadio > div {
        gap: 4px;
        flex-direction: column;
    }
    [data-testid="stSidebar"] .stRadio label {
        background: rgba(0,0,0,0.25) !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        padding: 10px 14px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        color: var(--white) !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
        cursor: pointer;
        transition: all 0.15s;
        border-radius: 0 !important;
    }
    [data-testid="stSidebar"] .stRadio label:hover {
        background: var(--yellow) !important;
        border-color: var(--black) !important;
        color: var(--black) !important;
        box-shadow: 3px 3px 0 rgba(0,0,0,0.5) !important;
        transform: translate(-2px, -2px);
    }
    [data-testid="stSidebar"] .stRadio label[data-selected="true"],
    [data-testid="stSidebar"] .stRadio label[aria-checked="true"] {
        background: var(--yellow) !important;
        border-color: var(--black) !important;
        color: var(--black) !important;
        font-weight: 700 !important;
    }
    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.3) !important;
        border-width: 2px !important;
    }
    [data-testid="stSidebar"] .stSlider * {
        color: var(--white) !important;
    }
    [data-testid="stSidebar"] .stButton > button {
        background: var(--yellow) !important;
        color: var(--black) !important;
        border: 3px solid var(--black) !important;
        box-shadow: 4px 4px 0 var(--black) !important;
        font-family: 'Archivo Black', sans-serif !important;
        font-weight: 900 !important;
        border-radius: 0 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        transform: translate(3px, 3px) !important;
        box-shadow: 1px 1px 0 var(--black) !important;
        background: var(--white) !important;
    }
    
    /* ===== HERO SECTION ===== */
    .hero-home {
        background: var(--blue);
        border: var(--border-thick);
        box-shadow: var(--shadow-lg);
        padding: 3rem 3rem 2.5rem;
        position: relative;
        overflow: hidden;
        margin-bottom: 2rem;
    }
    .hero-home::before {
        content: '';
        position: absolute;
        top: -40px; right: -40px;
        width: 200px; height: 200px;
        background: var(--yellow);
        border: 4px solid var(--black);
        transform: rotate(15deg);
        pointer-events: none;
        opacity: 0.35;
    }
    .hero-home::after {
        content: '';
        position: absolute;
        bottom: -30px; right: 120px;
        width: 120px; height: 120px;
        background: var(--cyan);
        border: 4px solid var(--black);
        border-radius: 50%;
        pointer-events: none;
        opacity: 0.3;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: var(--yellow);
        color: var(--black);
        border: 3px solid var(--black);
        box-shadow: 3px 3px 0 var(--black);
        padding: 5px 16px;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 1.4rem;
    }
    .hero-title {
        font-family: 'Archivo Black', sans-serif !important;
        font-size: 3rem !important;
        font-weight: 900 !important;
        color: var(--white) !important;
        line-height: 1.05 !important;
        margin: 0 0 1rem !important;
        text-transform: uppercase !important;
        letter-spacing: -0.5px !important;
    }
    .hero-sub {
        font-size: 1rem;
        color: rgba(255,255,255,0.88);
        max-width: 680px;
        line-height: 1.6;
        margin-bottom: 2rem;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* ===== CARDS (BRUTALIST) ===== */
    .modern-card {
        background: var(--white);
        border: var(--border-thick);
        box-shadow: var(--shadow);
        padding: 1.6rem;
        transition: transform 0.12s, box-shadow 0.12s;
        height: 100%;
        position: relative;
    }
    .modern-card::before {
        content: '';
        position: absolute;
        top: 6px; left: 6px;
        right: -6px; bottom: -6px;
        background: var(--yellow);
        z-index: -1;
        border: 2px solid var(--black);
    }
    .modern-card:hover {
        transform: translate(-3px, -3px);
        box-shadow: var(--shadow-lg);
    }
    .metric-icon {
        font-size: 1.9rem;
        margin-bottom: 0.6rem;
    }
    .metric-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        font-weight: 700;
        color: #555;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 4px;
    }
    .metric-value {
        font-family: 'Archivo Black', sans-serif;
        font-size: 2.4rem;
        font-weight: 900;
        color: var(--blue);
        line-height: 1;
    }
    .metric-desc {
        font-size: 0.78rem;
        color: #555;
        margin-top: 5px;
        font-family: 'IBM Plex Mono', monospace;
    }
    
    /* ===== PREDICTION CARD ===== */
    .prediction-card {
        background: var(--white);
        border: var(--border-thick);
        box-shadow: var(--shadow);
        padding: 2rem;
        text-align: center;
    }
    .prediction-card.success {
        border-color: var(--black);
        background: #D1FAE5;
        color: #065F46;
    }
    .prediction-card.danger {
        border-color: var(--black);
        background: #FEE2E2;
        color: #991B1B;
    }
    .prediction-icon { 
        font-size: 3.5rem; 
        margin-bottom: 1rem; 
    }
    .prediction-result {
        font-family: 'Archivo Black', sans-serif;
        font-size: 2rem;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .prediction-prob { 
        font-size: 1rem; 
        color: #333; 
        margin-top: 1rem; 
    }
    .prediction-prob .prob-value {
        color: var(--black);
    }
    .badge-penerima {
        background: #D1FAE5;
        color: #065F46;
        border: 3px solid #065F46;
        box-shadow: 3px 3px 0 #065F46;
        padding: 5px 18px;
        font-family: 'Archivo Black', sans-serif;
        font-weight: 900;
        font-size: 0.85rem;
        text-transform: uppercase;
        display: inline-block;
    }
    .badge-tidak {
        background: #FEE2E2;
        color: #991B1B;
        border: 3px solid #991B1B;
        box-shadow: 3px 3px 0 #991B1B;
        padding: 5px 18px;
        font-family: 'Archivo Black', sans-serif;
        font-weight: 900;
        font-size: 0.85rem;
        text-transform: uppercase;
        display: inline-block;
    }
    
    /* ===== FORM & INPUT — NEO BRUTALISM WARM PALETTE ===== */
    .stTextInput input,
    .stNumberInput input,
    .stSelectbox > div > div,
    textarea {
        background: #FFF8D6 !important;
        color: #111111 !important;
        border: 3px solid #000 !important;
        border-radius: 0 !important;
        box-shadow: 3px 3px 0 #000 !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        transition: all 0.12s ease !important;
    }
    .stTextInput input:hover,
    .stNumberInput input:hover,
    .stSelectbox > div > div:hover,
    textarea:hover {
        background: #FFFBE6 !important;
        box-shadow: 4px 4px 0 #000 !important;
    }
    .stTextInput input:focus,
    .stNumberInput input:focus,
    .stSelectbox > div > div:focus-within,
    textarea:focus {
        background: #FFE500 !important;
        border-color: #2146FF !important;
        box-shadow: 6px 6px 0 #000 !important;
        transform: translate(-2px, -2px) !important;
        outline: none !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        background: transparent !important;
    }
    .stSelectbox span {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    .stTextInput input::placeholder,
    .stNumberInput input::placeholder,
    textarea::placeholder {
        color: #666666 !important;
        font-weight: 500 !important;
    }
    .stNumberInput [data-testid="stNumberInputStepUp"],
    .stNumberInput [data-testid="stNumberInputStepDown"] {
        background: #FFF8D6 !important;
        border: 2px solid #000 !important;
        border-radius: 0 !important;
        color: #111111 !important;
        transition: all 0.1s ease !important;
    }
    .stNumberInput [data-testid="stNumberInputStepUp"]:hover,
    .stNumberInput [data-testid="stNumberInputStepDown"]:hover {
        background: #FFE500 !important;
    }
    .stFileUploader > div {
        border: 3px dashed var(--black) !important;
        border-radius: 0 !important;
        background: #F8F5E9 !important;
        box-shadow: 4px 4px 0 var(--black) !important;
        transition: all 0.12s ease !important;
    }
    .stFileUploader > div:hover {
        background: #FFF8D6 !important;
        box-shadow: 6px 6px 0 var(--black) !important;
    }
    .stTextInput label,
    .stNumberInput label,
    .stSelectbox label {
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.7rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        color: #333333 !important;
    }
    
    /* ===== ALERTS ===== */
    .alert-success {
        background: #D1FAE5;
        border: 3px solid #065F46;
        box-shadow: 4px 4px 0 #065F46;
        padding: 12px 18px;
        color: #065F46;
        font-size: 0.9rem;
        font-weight: 600;
    }
    .alert-info {
        background: #DBEAFE;
        border: 3px solid #1E40AF;
        box-shadow: 4px 4px 0 #1E40AF;
        padding: 12px 18px;
        color: #1E40AF;
        font-size: 0.9rem;
        font-weight: 600;
    }
    .alert-warning {
        background: #FEF3C7;
        border: 3px solid #92400E;
        box-shadow: 4px 4px 0 #92400E;
        padding: 12px 18px;
        color: #92400E;
        font-size: 0.9rem;
        font-weight: 600;
    }
    .alert-error {
        background: #FEE2E2;
        border: 3px solid #991B1B;
        box-shadow: 4px 4px 0 #991B1B;
        padding: 12px 18px;
        color: #991B1B;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    /* ===== BUTTONS (GLOBAL) ===== */
    .stButton > button {
        background: var(--blue) !important;
        color: var(--white) !important;
        border: 3px solid var(--black) !important;
        border-radius: 0 !important;
        box-shadow: 5px 5px 0 var(--black) !important;
        font-family: 'Archivo Black', sans-serif !important;
        font-weight: 900 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
        padding: 11px 22px !important;
        transition: transform 0.1s, box-shadow 0.1s !important;
    }
    .stButton > button:hover {
        transform: translate(4px, 4px) !important;
        box-shadow: 1px 1px 0 var(--black) !important;
        background: var(--yellow) !important;
        color: var(--black) !important;
    }
    .stButton > button:active {
        transform: translate(5px, 5px) !important;
        box-shadow: 0px 0px 0 var(--black) !important;
    }
    .stDownloadButton > button {
        background: var(--yellow) !important;
        color: var(--black) !important;
        border: 3px solid var(--black) !important;
        border-radius: 0 !important;
        box-shadow: 5px 5px 0 var(--black) !important;
        font-family: 'Archivo Black', sans-serif !important;
        font-weight: 900 !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
        transition: transform 0.1s, box-shadow 0.1s !important;
    }
    .stDownloadButton > button:hover {
        transform: translate(4px, 4px) !important;
        box-shadow: 1px 1px 0 var(--black) !important;
    }
    
    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: var(--black);
        padding: 4px;
        border: 3px solid var(--black);
        box-shadow: 5px 5px 0 var(--black);
        border-radius: 0 !important;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 0 !important;
        padding: 8px 16px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.82rem !important;
        color: rgba(255,255,255,0.7) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        border: 2px solid transparent !important;
    }
    .stTabs [aria-selected="true"] {
        background: var(--yellow) !important;
        color: var(--black) !important;
        border: 2px solid var(--black) !important;
        font-weight: 900 !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255,255,255,0.15) !important;
        color: var(--white) !important;
    }
    
    /* ===== PROGRESS ===== */
    .stProgress > div > div > div {
        background: var(--blue) !important;
        border-radius: 0 !important;
        border: 1px solid var(--black) !important;
    }
    .stProgress > div > div {
        background: var(--gray) !important;
        border: 2px solid var(--black) !important;
        border-radius: 0 !important;
        box-shadow: 3px 3px 0 var(--black) !important;
    }
    
    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        background: var(--blue) !important;
        border: 3px solid var(--black) !important;
        border-radius: 0 !important;
        box-shadow: 4px 4px 0 var(--black) !important;
        color: var(--white) !important;
        font-family: 'Archivo Black', sans-serif !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
    }
    .streamlit-expanderContent {
        border: 3px solid var(--black) !important;
        border-top: none !important;
        border-radius: 0 !important;
        background: var(--white) !important;
    }
    
    /* ===== DATAFRAME ===== */
    .stDataFrame {
        border: 3px solid var(--black) !important;
        box-shadow: 5px 5px 0 var(--black) !important;
    }
    [data-testid="stDataFrame"] th {
        background: var(--blue) !important;
        color: var(--white) !important;
        font-family: 'Archivo Black', sans-serif !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        border: 2px solid var(--black) !important;
    }
    [data-testid="stDataFrame"] td {
        border: 1px solid #ddd !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.82rem !important;
        color: var(--black) !important;
    }
    [data-testid="stDataFrame"] tr:nth-child(even) td {
        background: rgba(33, 70, 255, 0.05) !important;
    }
    [data-testid="stDataFrame"] tr:hover td {
        background: rgba(255, 229, 0, 0.3) !important;
    }
    
    /* ===== METRIC WIDGET ===== */
    [data-testid="metric-container"] {
        background: var(--white);
        border: 3px solid var(--black);
        box-shadow: var(--shadow);
        padding: 16px !important;
    }
    [data-testid="metric-container"] label {
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.7rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        color: #555 !important;
    }
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        font-family: 'Archivo Black', sans-serif !important;
        color: var(--blue) !important;
        font-weight: 900 !important;
    }
    
    /* ===== FOOTER ===== */
    .footer {
        background: var(--black);
        color: var(--white);
        border: var(--border-thick);
        box-shadow: var(--shadow-lg);
        padding: 2rem;
        text-align: center;
        margin-top: 3rem;
        position: relative;
        overflow: hidden;
    }
    .footer::before {
        content: '//BSM//';
        position: absolute;
        top: 50%; left: -10px;
        transform: translateY(-50%);
        font-family: 'Bungee', sans-serif;
        font-size: 5rem;
        color: rgba(255,229,0,0.08);
        white-space: nowrap;
        pointer-events: none;
        letter-spacing: 0.2em;
    }
    .footer-brand {
        font-family: 'Archivo Black', sans-serif;
        color: var(--yellow);
        font-weight: 900;
        font-size: 1.2rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    .footer-divider {
        width: 60px;
        height: 4px;
        background: var(--yellow);
        margin: 12px auto;
    }
    
    /* ===== INFO/WARNING/ERROR NATIVE ===== */
    .stAlert {
        border: 3px solid var(--black) !important;
        border-radius: 0 !important;
        box-shadow: 4px 4px 0 var(--black) !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
    }
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: var(--gray); border: 2px solid var(--black); }
    ::-webkit-scrollbar-thumb { background: var(--blue); border: 2px solid var(--black); }
    ::-webkit-scrollbar-thumb:hover { background: var(--yellow); border: 2px solid var(--black); }
    
    /* ===== HEADINGS IN MAIN ===== */
    .main h1, .main h2, .main h3 {
        font-family: 'Archivo Black', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 0.02em !important;
    }
    .main h3 {
        border-left: 5px solid var(--blue);
        padding-left: 10px;
        margin-top: 1.5rem;
    }
    
    /* ===== SPINNER ===== */
    .stSpinner > div {
        border-top-color: var(--blue) !important;
    }
    
    /* ===== HIDE STREAMLIT BRANDING ===== */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stDeployButton { display: none; }
    
    /* ===== ANIMATIONS ===== */
    @keyframes floatY {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .modern-card { animation: fadeInUp 0.3s ease both; }
    .hero-home { animation: fadeInUp 0.4s ease both; }


    /* =========================================================
       CONTRAST FIX + ACADEMIC CLEAN THEME
       Dipasang terakhir supaya menimpa gaya brutalist yang terlalu teriak.
       ========================================================= */
    :root {
        --blue: #1D4ED8;
        --yellow: #F8D84A;
        --black: #0F172A;
        --white: #FFFFFF;
        --gray: #F8FAFC;
        --cyan: #38BDF8;
        --red: #EF4444;
        --lime: #84CC16;
        --purple: #7C3AED;
        --border: 1px solid #D7DEE8;
        --border-thick: 1px solid #D7DEE8;
        --shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        --shadow-sm: 0 4px 12px rgba(15, 23, 42, 0.07);
        --shadow-lg: 0 14px 35px rgba(15, 23, 42, 0.12);
        --shadow-hover: 0 10px 28px rgba(15, 23, 42, 0.12);
    }

    html, body, .stApp, .main {
        background: #F8FAFC !important;
        color: #0F172A !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }

    .main {
        background-image: radial-gradient(circle, rgba(15,23,42,0.08) 1px, transparent 1px) !important;
        background-size: 26px 26px !important;
    }

    .main .block-container {
        padding: 1.4rem 2rem 3rem !important;
        max-width: 1280px !important;
    }

    .main h1, .main h2, .main h3, .main h4,
    .main p, .main span, .main label, .main div {
        color: #0F172A;
    }

    .main h3 {
        color: #0F172A !important;
        border-left: 5px solid #1D4ED8 !important;
        background: #FFFFFF !important;
        padding: 0.75rem 1rem !important;
        border-radius: 12px !important;
        box-shadow: 0 6px 18px rgba(15,23,42,0.06) !important;
        text-shadow: none !important;
    }

    /* Sidebar lebih kalem, bukan biru nyala kayak papan iklan diskon. */
    [data-testid="stSidebar"] > div:first-child {
        background: #0F172A !important;
        border-right: 1px solid #263244 !important;
    }
    [data-testid="stSidebar"] * {
        color: #E5E7EB !important;
    }
    [data-testid="stSidebar"] label {
        color: #BFDBFE !important;
        font-family: 'IBM Plex Mono', monospace !important;
        letter-spacing: 0.06em !important;
    }
    [data-testid="stSidebar"] .stRadio label {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 10px !important;
        box-shadow: none !important;
        color: #E5E7EB !important;
        padding: 10px 12px !important;
        transform: none !important;
    }
    [data-testid="stSidebar"] .stRadio label:hover,
    [data-testid="stSidebar"] .stRadio label[data-selected="true"],
    [data-testid="stSidebar"] .stRadio label[aria-checked="true"] {
        background: #1D4ED8 !important;
        border-color: #60A5FA !important;
        color: #FFFFFF !important;
        box-shadow: none !important;
        transform: none !important;
    }

    /* Hero: tetap kuat, tapi tidak bikin mata minta cuti. */
    .hero-home {
        background: linear-gradient(135deg, #1E3A8A 0%, #1D4ED8 55%, #2563EB 100%) !important;
        border: 1px solid #1E40AF !important;
        border-radius: 24px !important;
        box-shadow: 0 20px 50px rgba(29,78,216,0.22) !important;
        padding: 3rem 3rem 2.5rem !important;
        overflow: hidden !important;
    }
    .hero-home::before {
        background: rgba(255,255,255,0.12) !important;
        border: 1px solid rgba(255,255,255,0.22) !important;
        box-shadow: none !important;
    }
    .hero-home::after {
        background: rgba(56,189,248,0.22) !important;
        border: 1px solid rgba(255,255,255,0.26) !important;
    }
    .hero-title {
        color: #FFFFFF !important;
        text-shadow: 0 3px 12px rgba(0,0,0,0.20) !important;
        letter-spacing: -0.03em !important;
    }
    .hero-sub {
        color: #DBEAFE !important;
    }
    .hero-badge {
        background: rgba(255,255,255,0.14) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255,255,255,0.28) !important;
        border-radius: 999px !important;
        box-shadow: none !important;
    }

    /* Override kotak statistik inline di hero. */
    .hero-home div[style*="background:#FFE500"],
    .hero-home div[style*="background:#00F5FF"],
    .hero-home div[style*="background:#B6FF00"],
    .hero-home div[style*="background:#fff"] {
        background: rgba(255,255,255,0.95) !important;
        color: #0F172A !important;
        border: 1px solid rgba(255,255,255,0.55) !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 22px rgba(15,23,42,0.14) !important;
    }

    /* Card utama: hilangkan kuning ekstrem, perbaiki text clipping. */
    .modern-card {
        background: #FFFFFF !important;
        border: 1px solid #D7DEE8 !important;
        border-radius: 20px !important;
        box-shadow: 0 10px 28px rgba(15,23,42,0.08) !important;
        padding: 1.5rem !important;
        overflow: hidden !important;
        min-height: 210px !important;
    }
    .modern-card::before {
        display: none !important;
    }
    .modern-card:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 18px 36px rgba(15,23,42,0.12) !important;
    }
    .metric-icon {
        width: 44px !important;
        height: 44px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        background: #EFF6FF !important;
        border-radius: 12px !important;
        font-size: 1.5rem !important;
        margin-bottom: 1rem !important;
    }
    .metric-label {
        color: #475569 !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.08em !important;
    }
    .metric-value {
        color: #1D4ED8 !important;
        font-size: clamp(1.75rem, 3.3vw, 2.35rem) !important;
        line-height: 0.95 !important;
        overflow-wrap: anywhere !important;
        word-break: normal !important;
    }
    .metric-desc {
        color: #334155 !important;
        font-size: 0.82rem !important;
        line-height: 1.55 !important;
    }

    /* Expander yang tadi putih di atas abu-abu. Manusia memang suka menyiksa readability. */
    [data-testid="stExpander"] {
        background: #FFFFFF !important;
        border: 1px solid #D7DEE8 !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 24px rgba(15,23,42,0.06) !important;
        overflow: hidden !important;
    }
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary p,
    [data-testid="stExpander"] summary span,
    .streamlit-expanderHeader {
        background: #FFFFFF !important;
        color: #0F172A !important;
        border: none !important;
        box-shadow: none !important;
        text-transform: none !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
    }
    [data-testid="stExpander"] div,
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] span,
    [data-testid="stExpander"] li {
        color: #0F172A !important;
    }

    /* Step list inline di landing. */
    .main div[style*="background:#fff; border:3px solid #000"] {
        background: #FFFFFF !important;
        border: 1px solid #D7DEE8 !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 22px rgba(15,23,42,0.07) !important;
    }
    .main div[style*="background:#FFE500; border:2px solid #000"] {
        background: #EFF6FF !important;
        border: 1px solid #BFDBFE !important;
        border-radius: 12px !important;
        box-shadow: none !important;
    }

    /* Form, button, tabs: konsisten, bukan carnival mode. */
    .stTextInput input,
    .stNumberInput input,
    .stSelectbox > div > div,
    textarea {
        background: #FFFFFF !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 12px !important;
        box-shadow: none !important;
        font-weight: 600 !important;
    }
    .stTextInput input:focus,
    .stNumberInput input:focus,
    .stSelectbox > div > div:focus-within,
    textarea:focus {
        background: #FFFFFF !important;
        border-color: #1D4ED8 !important;
        box-shadow: 0 0 0 3px rgba(29,78,216,0.14) !important;
        transform: none !important;
    }
    .stSelectbox span {
        color: #0F172A !important;
    }
    .stButton > button,
    .stDownloadButton > button {
        background: #1D4ED8 !important;
        color: #FFFFFF !important;
        border: 1px solid #1E40AF !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 18px rgba(29,78,216,0.18) !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: #1E40AF !important;
        color: #FFFFFF !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 12px 22px rgba(29,78,216,0.22) !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        background: #E2E8F0 !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 14px !important;
        box-shadow: none !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #334155 !important;
        border-radius: 10px !important;
        border: none !important;
    }
    .stTabs [aria-selected="true"] {
        background: #FFFFFF !important;
        color: #1D4ED8 !important;
        border: none !important;
        box-shadow: 0 3px 10px rgba(15,23,42,0.08) !important;
    }

    [data-testid="stDataFrame"] th {
        background: #1E3A8A !important;
        color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
    }
    [data-testid="stDataFrame"] td {
        color: #0F172A !important;
        border: 1px solid #E2E8F0 !important;
    }

    .footer {
        background: #0F172A !important;
        border: 1px solid #1E293B !important;
        border-radius: 24px !important;
        box-shadow: 0 16px 40px rgba(15,23,42,0.18) !important;
        color: #E5E7EB !important;
    }
    .footer-brand { color: #BFDBFE !important; }
    .footer-divider { background: #3B82F6 !important; }



    /* ============================================================
       DARK BACKGROUND OVERRIDE - BLACK MODE YANG MASIH KEBACA
       ============================================================ */
    :root {
        --bg-black: #050505;
        --panel-black: #0B0F19;
        --panel-soft: #111827;
        --panel-line: #263244;
        --text-main: #F8FAFC;
        --text-muted: #CBD5E1;
        --text-soft: #94A3B8;
        --accent-blue: #3B82F6;
        --accent-yellow: #FACC15;
    }

    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    .main,
    .block-container {
        background: var(--bg-black) !important;
        color: var(--text-main) !important;
    }

    .main {
        background-image: radial-gradient(circle, rgba(255,255,255,0.08) 1px, transparent 1px) !important;
        background-size: 24px 24px !important;
        background-color: var(--bg-black) !important;
    }

    [data-testid="stHeader"] {
        background: rgba(5, 5, 5, 0.88) !important;
        backdrop-filter: blur(10px) !important;
    }

    h1, h2, h3, h4, h5, h6,
    p, li, label, span, div {
        color: inherit;
    }

    h1, h2, h3, h4, h5, h6,
    .section-title,
    .sticky-header-title {
        color: var(--text-main) !important;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] span {
        color: var(--text-muted) !important;
    }

    /* Sidebar tetap biru, tapi tidak norak */
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #07111F 0%, #0B1E3A 55%, #08111F 100%) !important;
        border-right: 1px solid #1E3A5F !important;
    }
    [data-testid="stSidebar"] * {
        color: #E5E7EB !important;
    }
    [data-testid="stSidebar"] label {
        color: #BFDBFE !important;
    }
    [data-testid="stSidebar"] .stRadio label {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(148,163,184,0.22) !important;
        color: #E5E7EB !important;
        border-radius: 12px !important;
        box-shadow: none !important;
    }
    [data-testid="stSidebar"] .stRadio label:hover,
    [data-testid="stSidebar"] .stRadio label[data-selected="true"],
    [data-testid="stSidebar"] .stRadio label[aria-checked="true"] {
        background: rgba(59,130,246,0.18) !important;
        color: #FFFFFF !important;
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 3px rgba(59,130,246,0.14) !important;
        transform: none !important;
    }

    /* Hero */
    .hero-home {
        background: linear-gradient(135deg, #0B1220 0%, #102B63 55%, #2146FF 100%) !important;
        border: 1px solid #31518A !important;
        border-radius: 28px !important;
        box-shadow: 0 24px 70px rgba(0,0,0,0.52) !important;
    }
    .hero-home::before,
    .hero-home::after {
        opacity: 0.18 !important;
        border-color: rgba(255,255,255,0.25) !important;
    }
    .hero-title { color: #FFFFFF !important; }
    .hero-sub { color: #D7E3F8 !important; }
    .hero-badge {
        background: rgba(250,204,21,0.14) !important;
        color: #FDE68A !important;
        border: 1px solid rgba(250,204,21,0.45) !important;
        box-shadow: none !important;
        border-radius: 999px !important;
    }

    /* Card gelap, bukan kuning silau */
    .modern-card,
    .prediction-card {
        background: linear-gradient(180deg, #111827 0%, #0B0F19 100%) !important;
        border: 1px solid #263244 !important;
        border-radius: 24px !important;
        box-shadow: 0 18px 45px rgba(0,0,0,0.42) !important;
        color: var(--text-main) !important;
    }
    .modern-card::before { display: none !important; }
    .modern-card:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 24px 60px rgba(0,0,0,0.52) !important;
        border-color: #3B82F6 !important;
    }
    .metric-label { color: #94A3B8 !important; }
    .metric-value { color: #60A5FA !important; }
    .metric-desc { color: #CBD5E1 !important; }

    /* Sticky header */
    .sticky-header {
        background: rgba(17,24,39,0.94) !important;
        border: 1px solid #263244 !important;
        border-radius: 18px !important;
        box-shadow: 0 18px 45px rgba(0,0,0,0.45) !important;
        backdrop-filter: blur(12px) !important;
    }
    .sticky-header-icon {
        background: #1D4ED8 !important;
        border: 1px solid #60A5FA !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
    }

    /* Form */
    .stTextInput input,
    .stNumberInput input,
    .stSelectbox > div > div,
    textarea {
        background: #0B1220 !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        box-shadow: none !important;
    }
    .stTextInput input:hover,
    .stNumberInput input:hover,
    .stSelectbox > div > div:hover,
    textarea:hover {
        background: #101827 !important;
        border-color: #475569 !important;
        box-shadow: none !important;
    }
    .stTextInput input:focus,
    .stNumberInput input:focus,
    .stSelectbox > div > div:focus-within,
    textarea:focus {
        background: #111827 !important;
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 3px rgba(59,130,246,0.22) !important;
        transform: none !important;
        outline: none !important;
    }
    .stTextInput label,
    .stNumberInput label,
    .stSelectbox label {
        color: #CBD5E1 !important;
    }
    .stSelectbox span {
        color: #F8FAFC !important;
    }

    /* Buttons */
    .stButton > button,
    .stDownloadButton > button {
        background: #2563EB !important;
        color: #FFFFFF !important;
        border: 1px solid #60A5FA !important;
        border-radius: 12px !important;
        box-shadow: 0 10px 26px rgba(37,99,235,0.25) !important;
    }
    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: #1D4ED8 !important;
        color: #FFFFFF !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 14px 32px rgba(37,99,235,0.32) !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: #0B1220 !important;
        border: 1px solid #263244 !important;
        border-radius: 14px !important;
        box-shadow: none !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #CBD5E1 !important;
        border-radius: 10px !important;
    }
    .stTabs [aria-selected="true"] {
        background: #1E3A8A !important;
        color: #FFFFFF !important;
        box-shadow: none !important;
    }

    /* Expander, uploader, dataframe */
    .streamlit-expanderHeader,
    [data-testid="stExpander"] {
        background: #111827 !important;
        color: #F8FAFC !important;
        border-color: #263244 !important;
    }
    .stFileUploader > div {
        background: #0B1220 !important;
        border: 1px dashed #475569 !important;
        border-radius: 16px !important;
        box-shadow: none !important;
    }
    [data-testid="stDataFrame"] {
        background: #0B1220 !important;
        border-radius: 16px !important;
    }
    [data-testid="stDataFrame"] th {
        background: #111827 !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
    }
    [data-testid="stDataFrame"] td {
        background: #0B1220 !important;
        color: #E5E7EB !important;
        border: 1px solid #263244 !important;
    }

    /* Alert tetap kebaca di background hitam */
    .alert-success { background: rgba(16,185,129,0.14) !important; color: #A7F3D0 !important; border: 1px solid rgba(16,185,129,0.45) !important; box-shadow: none !important; border-radius: 14px !important; }
    .alert-info { background: rgba(59,130,246,0.14) !important; color: #BFDBFE !important; border: 1px solid rgba(59,130,246,0.45) !important; box-shadow: none !important; border-radius: 14px !important; }
    .alert-warning { background: rgba(250,204,21,0.13) !important; color: #FDE68A !important; border: 1px solid rgba(250,204,21,0.45) !important; box-shadow: none !important; border-radius: 14px !important; }
    .alert-error { background: rgba(248,113,113,0.14) !important; color: #FECACA !important; border: 1px solid rgba(248,113,113,0.45) !important; box-shadow: none !important; border-radius: 14px !important; }

    /* Footer */
    .footer {
        background: #0B0F19 !important;
        border: 1px solid #263244 !important;
        color: #CBD5E1 !important;
    }
    </style>
    """, unsafe_allow_html=True)


def make_plotly_theme():
    """Return consistent Plotly theme dict — DARK MODE BLACK BACKGROUND."""
    return dict(
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font=dict(family="Space Grotesk, sans-serif", color="#E5E7EB", size=12),
        margin=dict(l=20, r=20, t=50, b=20),
        title_font=dict(family="Archivo Black, sans-serif", size=15, color="#FFFFFF"),
        legend_font=dict(color="#E5E7EB"),
        xaxis=dict(
            showgrid=True, 
            gridcolor="#333333", 
            linecolor="#555555", 
            linewidth=2,
            tickfont=dict(family="IBM Plex Mono, monospace", size=11, color="#BBBBBB"),
            title_font=dict(color="#E5E7EB")
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor="#333333", 
            linecolor="#555555", 
            linewidth=2,
            tickfont=dict(family="IBM Plex Mono, monospace", size=11, color="#BBBBBB"),
            title_font=dict(color="#E5E7EB")
        ),
        colorway=["#60A5FA", "#F87171", "#34D399", "#FBBF24", "#A78BFA", "#22D3EE"]
    )


def make_plotly_colors():
    """Return color scheme untuk visualisasi konsisten di dark background."""
    return {
        'penerima': '#34D399',           # Emerald green
        'tidak_penerima': '#F87171',     # Red
        'primary': '#60A5FA',             # Blue
        'secondary': '#A78BFA',           # Purple
        'accent': '#FBBF24',              # Amber
        'info': '#22D3EE',                # Cyan
        'gradient_blue': ['#1E3A5F', '#1E40AF', '#2563EB', '#3B82F6', '#60A5FA', '#93C5FD', '#BFDBFE'],
        'gradient_red': ['#5F1A1A', '#991B1B', '#DC2626', '#EF4444', '#F87171', '#FCA5A5', '#FECACA'],
        'gradient_green': ['#1A3F32', '#065F46', '#059669', '#10B981', '#34D399', '#6EE7B7', '#A7F3D0'],
        'pie_colors': ['#60A5FA', '#F87171', '#34D399', '#FBBF24', '#A78BFA'],
        'bar_blue': '#3B82F6',
        'bar_red': '#EF4444',
        'bar_green': '#10B981',
    }
