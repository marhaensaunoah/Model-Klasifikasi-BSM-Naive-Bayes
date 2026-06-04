# ============================================================
# STYLES DAN KONFIGURASI CSS - SISTEM KLASIFIKASI BSM
# ============================================================

import streamlit as st


def load_custom_css():
    """Memuat custom CSS untuk aplikasi Streamlit."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Bungee&family=IBM+Plex+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700;800;900&display=swap');

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

        --dark-bg: #05070D;
        --dark-panel: #0B1020;
        --dark-card: #111827;
        --dark-border: #1F2937;
        --dark-muted: #CBD5E1;

        --border: 3px solid #000;
        --border-thick: 5px solid #000;
        --shadow: 6px 6px 0px #000;
        --shadow-sm: 4px 4px 0px #000;
        --shadow-lg: 8px 8px 0px #000;
        --shadow-hover: 2px 2px 0px #000;
    }

    /* ===== GLOBAL BACKGROUND - DARK FIX ===== */
    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    .main,
    .block-container {
        background: var(--dark-bg) !important;
        color: var(--white) !important;
        font-family: 'Space Grotesk', sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(5, 7, 13, 0.92) !important;
    }

    .main {
        background-image: radial-gradient(circle, rgba(255,255,255,0.08) 1px, transparent 1px) !important;
        background-size: 22px 22px !important;
        background-color: var(--dark-bg) !important;
    }

    .main .block-container {
        padding: 1.2rem 2rem 3rem;
        max-width: 1440px;
        background: transparent !important;
    }

    /* ===== FONT LOCK - SESUAI DESAIN AWAL ===== */

    html, body,
    .main,
    .block-container,
    .hero-sub,
    .modern-card,
    .prediction-card,
    .alert-success,
    .alert-info,
    .alert-warning,
    .alert-error,
    .stAlert,
    .stTextInput input,
    .stNumberInput input,
    .stSelectbox,
    textarea {
        font-family: 'Space Grotesk', sans-serif !important;
    }

    .hero-title,
    .sticky-header-title,
    .metric-value,
    .prediction-result,
    .badge-penerima,
    .badge-tidak,
    .footer-brand,
    .main h1,
    .main h2,
    .main h3,
    .streamlit-expanderHeader,
    .stButton > button,
    .stDownloadButton > button,
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        font-family: 'Archivo Black', sans-serif !important;
    }

    .hero-badge,
    .metric-label,
    .metric-desc,
    .stTextInput label,
    .stNumberInput label,
    .stSelectbox label,
    [data-testid="stDataFrame"] td,
    [data-testid="stDataFrame"] th,
    [data-testid="metric-container"] label {
        font-family: 'IBM Plex Mono', monospace !important;
    }

    .footer::before {
        font-family: 'Bungee', sans-serif !important;
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

    .sticky-header-spacer {
        height: 100px;
    }

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
        color: var(--white);
    }

    .sticky-header-title {
        font-size: 1.3rem;
        font-weight: 900;
        color: var(--black);
        text-transform: uppercase;
        letter-spacing: 0.02em;
        white-space: nowrap;
        text-shadow: none !important;
    }

    @media (max-width: 768px) {
        .sticky-header {
            left: 1rem;
            right: 1rem;
            top: 4rem;
        }
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
        color: var(--black) !important;
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
        top: -40px;
        right: -40px;
        width: 200px;
        height: 200px;
        background: var(--yellow);
        border: 4px solid var(--black);
        transform: rotate(15deg);
        pointer-events: none;
        opacity: 0.35;
    }

    .hero-home::after {
        content: '';
        position: absolute;
        bottom: -30px;
        right: 120px;
        width: 120px;
        height: 120px;
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
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 1.4rem;
    }

    .hero-title {
        font-size: 3rem !important;
        font-weight: 900 !important;
        color: var(--white) !important;
        line-height: 1.05 !important;
        margin: 0 0 1rem !important;
        text-transform: uppercase !important;
        letter-spacing: -0.5px !important;
        text-shadow: none !important;
    }

    .hero-sub {
        font-size: 1rem;
        color: rgba(255,255,255,0.88);
        max-width: 680px;
        line-height: 1.6;
        margin-bottom: 2rem;
    }

    /* ===== CARDS ===== */
    .modern-card {
        background: var(--yellow);
        border: var(--border-thick);
        box-shadow: var(--shadow);
        padding: 1.6rem;
        transition: transform 0.12s, box-shadow 0.12s;
        height: 100%;
        position: relative;
        color: var(--black) !important;
    }

    .modern-card::before {
        content: '';
        position: absolute;
        top: 6px;
        left: 6px;
        right: -6px;
        bottom: -6px;
        background: var(--black);
        z-index: -1;
        border: 2px solid var(--black);
    }

    .modern-card:hover {
        transform: translate(-3px, -3px);
        box-shadow: var(--shadow-lg);
    }

    .modern-card * {
        color: inherit;
    }

    .metric-icon {
        font-size: 1.9rem;
        margin-bottom: 0.6rem;
    }

    .metric-label {
        font-size: 0.68rem;
        font-weight: 700;
        color: #222 !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 4px;
    }

    .metric-value {
        font-size: clamp(1.8rem, 3vw, 2.4rem);
        font-weight: 900;
        color: var(--blue) !important;
        line-height: 1;
        word-break: break-word;
    }

    .metric-desc {
        font-size: 0.78rem;
        color: #222 !important;
        margin-top: 5px;
    }

    /* ===== PREDICTION CARD ===== */
    .prediction-card {
        background: var(--white);
        border: var(--border-thick);
        box-shadow: var(--shadow);
        padding: 2rem;
        text-align: center;
        color: var(--black) !important;
    }

    .prediction-card.success {
        border-color: var(--black);
        background: #D1FAE5;
        color: #065F46 !important;
    }

    .prediction-card.danger {
        border-color: var(--black);
        background: #FEE2E2;
        color: #991B1B !important;
    }

    .prediction-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
    }

    .prediction-result {
        font-size: 2rem;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    .prediction-prob {
        font-size: 1rem;
        color: #333 !important;
        margin-top: 1rem;
    }

    .prediction-prob .prob-value {
        color: var(--black) !important;
    }

    .badge-penerima {
        background: #D1FAE5;
        color: #065F46 !important;
        border: 3px solid #065F46;
        box-shadow: 3px 3px 0 #065F46;
        padding: 5px 18px;
        font-weight: 900;
        font-size: 0.85rem;
        text-transform: uppercase;
        display: inline-block;
    }

    .badge-tidak {
        background: #FEE2E2;
        color: #991B1B !important;
        border: 3px solid #991B1B;
        box-shadow: 3px 3px 0 #991B1B;
        padding: 5px 18px;
        font-weight: 900;
        font-size: 0.85rem;
        text-transform: uppercase;
        display: inline-block;
    }

    /* ===== FORM & INPUT ===== */
    .stTextInput input,
    .stNumberInput input,
    .stSelectbox > div > div,
    textarea {
        background: #FFF8D6 !important;
        color: #111111 !important;
        border: 3px solid #000 !important;
        border-radius: 0 !important;
        box-shadow: 3px 3px 0 #000 !important;
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
        color: #111111 !important;
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
    .stSelectbox label,
    .stFileUploader label,
    .stSlider label {
        font-size: 0.7rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        color: var(--white) !important;
    }

    /* ===== ALERTS ===== */
    .alert-success {
        background: #D1FAE5;
        border: 3px solid #065F46;
        box-shadow: 4px 4px 0 #065F46;
        padding: 12px 18px;
        color: #065F46 !important;
        font-size: 0.9rem;
        font-weight: 600;
    }

    .alert-info {
        background: #DBEAFE;
        border: 3px solid #1E40AF;
        box-shadow: 4px 4px 0 #1E40AF;
        padding: 12px 18px;
        color: #1E40AF !important;
        font-size: 0.9rem;
        font-weight: 600;
    }

    .alert-warning {
        background: #FEF3C7;
        border: 3px solid #92400E;
        box-shadow: 4px 4px 0 #92400E;
        padding: 12px 18px;
        color: #92400E !important;
        font-size: 0.9rem;
        font-weight: 600;
    }

    .alert-error {
        background: #FEE2E2;
        border: 3px solid #991B1B;
        box-shadow: 4px 4px 0 #991B1B;
        padding: 12px 18px;
        color: #991B1B !important;
        font-size: 0.9rem;
        font-weight: 600;
    }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background: var(--blue) !important;
        color: var(--white) !important;
        border: 3px solid var(--black) !important;
        border-radius: 0 !important;
        box-shadow: 5px 5px 0 var(--black) !important;
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
        font-weight: 900 !important;
        text-transform: uppercase !important;
    }

    .streamlit-expanderContent {
        border: 3px solid var(--black) !important;
        border-top: none !important;
        border-radius: 0 !important;
        background: var(--white) !important;
        color: var(--black) !important;
    }

    .streamlit-expanderContent * {
        color: var(--black);
    }

    /* ===== DATAFRAME ===== */
    .stDataFrame {
        border: 3px solid var(--black) !important;
        box-shadow: 5px 5px 0 var(--black) !important;
    }

    [data-testid="stDataFrame"] th {
        background: var(--blue) !important;
        color: var(--white) !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        border: 2px solid var(--black) !important;
    }

    [data-testid="stDataFrame"] td {
        border: 1px solid #ddd !important;
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
        background: var(--yellow);
        border: 3px solid var(--black);
        box-shadow: var(--shadow);
        padding: 16px !important;
    }

    [data-testid="metric-container"] label {
        font-size: 0.7rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        color: #222 !important;
    }

    [data-testid="metric-container"] [data-testid="stMetricValue"] {
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
        top: 50%;
        left: -10px;
        transform: translateY(-50%);
        font-size: 5rem;
        color: rgba(255,229,0,0.08);
        white-space: nowrap;
        pointer-events: none;
        letter-spacing: 0.2em;
    }

    .footer-brand {
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

    /* ===== NATIVE ALERT ===== */
    .stAlert {
        border: 3px solid var(--black) !important;
        border-radius: 0 !important;
        box-shadow: 4px 4px 0 var(--black) !important;
        font-weight: 600 !important;
    }

    /* ===== MAIN HEADINGS ===== */
    .main h1,
    .main h2,
    .main h3 {
        color: var(--white) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.02em !important;
        text-shadow: none !important;
    }

    .main h3 {
        border-left: 5px solid var(--blue);
        padding-left: 10px;
        margin-top: 1.5rem;
    }

    .main p,
    .main span,
    .main label {
        color: inherit;
    }

    /* ===== PLOTLY ===== */
    [data-testid="stPlotlyChart"] {
        background: var(--dark-panel) !important;
        border: 3px solid var(--black) !important;
        box-shadow: 5px 5px 0 var(--black) !important;
        padding: 10px !important;
    }

    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: var(--dark-bg);
        border: 2px solid var(--black);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--blue);
        border: 2px solid var(--black);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--yellow);
        border: 2px solid var(--black);
    }

    /* ===== SPINNER ===== */
    .stSpinner > div {
        border-top-color: var(--blue) !important;
    }

    /* ===== HIDE STREAMLIT BRANDING ===== */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .stDeployButton {
        display: none;
    }

    /* ===== ANIMATIONS ===== */
    @keyframes floatY {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-8px);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .modern-card {
        animation: fadeInUp 0.3s ease both;
    }

    .hero-home {
        animation: fadeInUp 0.4s ease both;
    }

    </style>
    """, unsafe_allow_html=True)


def make_plotly_theme():
    """Return consistent Plotly theme dict — DARK MODE BLACK BACKGROUND."""
    return dict(
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font=dict(
            family="Space Grotesk, sans-serif",
            color="#E5E7EB",
            size=12
        ),
        margin=dict(l=20, r=20, t=50, b=20),
        title_font=dict(
            family="Archivo Black, sans-serif",
            size=15,
            color="#FFFFFF"
        ),
        legend_font=dict(
            color="#E5E7EB"
        ),
        xaxis=dict(
            showgrid=True,
            gridcolor="#333333",
            linecolor="#555555",
            linewidth=2,
            tickfont=dict(
                family="IBM Plex Mono, monospace",
                size=11,
                color="#BBBBBB"
            ),
            title_font=dict(color="#E5E7EB")
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="#333333",
            linecolor="#555555",
            linewidth=2,
            tickfont=dict(
                family="IBM Plex Mono, monospace",
                size=11,
                color="#BBBBBB"
            ),
            title_font=dict(color="#E5E7EB")
        ),
        colorway=[
            "#60A5FA",
            "#F87171",
            "#34D399",
            "#FBBF24",
            "#A78BFA",
            "#22D3EE"
        ]
    )


def make_plotly_colors():
    """Return color scheme untuk visualisasi konsisten di dark background."""
    return {
        "penerima": "#34D399",
        "tidak_penerima": "#F87171",
        "primary": "#60A5FA",
        "secondary": "#A78BFA",
        "accent": "#FBBF24",
        "info": "#22D3EE",

        "gradient_blue": [
            "#1E3A5F",
            "#1E40AF",
            "#2563EB",
            "#3B82F6",
            "#60A5FA",
            "#93C5FD",
            "#BFDBFE"
        ],
        "gradient_red": [
            "#5F1A1A",
            "#991B1B",
            "#DC2626",
            "#EF4444",
            "#F87171",
            "#FCA5A5",
            "#FECACA"
        ],
        "gradient_green": [
            "#1A3F32",
            "#065F46",
            "#059669",
            "#10B981",
            "#34D399",
            "#6EE7B7",
            "#A7F3D0"
        ],

        "pie_colors": [
            "#60A5FA",
            "#F87171",
            "#34D399",
            "#FBBF24",
            "#A78BFA"
        ],

        "bar_blue": "#3B82F6",
        "bar_red": "#EF4444",
        "bar_green": "#10B981"
    }
