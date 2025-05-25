#!/usr/bin/env python3
"""
Oslo Planning Premium - Advanced Design System
Professional UI components with modern design principles
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Enhanced Oslo Design System
OSLO_DESIGN = {
    # Color Palette - Expanded and refined
    'colors': {
        'primary': '#1B4F72',
        'primary_light': '#2E6DA4',
        'primary_dark': '#0F2A44',
        'secondary': '#2E86AB',
        'secondary_light': '#4A9BC1',
        'secondary_dark': '#1A5F7A',
        'accent': '#A23B72',
        'accent_light': '#B8518A',
        'accent_dark': '#7A2C54',
        'success': '#148F77',
        'success_light': '#1ABC9C',
        'success_dark': '#0F6B5A',
        'warning': '#F39C12',
        'warning_light': '#F5B041',
        'warning_dark': '#D68910',
        'danger': '#E74C3C',
        'danger_light': '#EC7063',
        'danger_dark': '#C0392B',
        'info': '#3498DB',
        'info_light': '#5DADE2',
        'info_dark': '#2874A6',
        'light': '#F8F9FA',
        'light_gray': '#E9ECEF',
        'medium_gray': '#6C757D',
        'dark_gray': '#495057',
        'dark': '#2C3E50',
        'white': '#FFFFFF',
        'black': '#1A1A1A'
    },
    
    # Typography
    'typography': {
        'font_family': '"Inter", "Segoe UI", "Roboto", "Helvetica Neue", Arial, sans-serif',
        'font_family_mono': '"JetBrains Mono", "Fira Code", "Consolas", monospace',
        'font_sizes': {
            'xs': '0.75rem',
            'sm': '0.875rem',
            'md': '1rem',
            'lg': '1.125rem',
            'xl': '1.25rem',
            'xxl': '1.5rem',
            'xxxl': '2rem',
            'display': '2.5rem'
        },
        'font_weights': {
            'light': '300',
            'normal': '400',
            'medium': '500',
            'semibold': '600',
            'bold': '700',
            'extrabold': '800'
        }
    },
    
    # Spacing System
    'spacing': {
        'xs': '0.25rem',
        'sm': '0.5rem',
        'md': '1rem',
        'lg': '1.5rem',
        'xl': '2rem',
        'xxl': '3rem',
        'xxxl': '4rem'
    },
    
    # Border Radius
    'radius': {
        'none': '0',
        'sm': '0.375rem',
        'md': '0.5rem',
        'lg': '0.75rem',
        'xl': '1rem',
        'xxl': '1.5rem',
        'full': '9999px'
    },
    
    # Shadows
    'shadows': {
        'sm': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'xl': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        'inner': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
        'glow': '0 0 20px rgba(27, 79, 114, 0.15)'
    }
}

def inject_advanced_css():
    """Inject advanced CSS for premium design"""
    
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    /* Global Styles */
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {OSLO_DESIGN['colors']['light']};
        border-radius: {OSLO_DESIGN['radius']['full']};
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {OSLO_DESIGN['colors']['medium_gray']};
        border-radius: {OSLO_DESIGN['radius']['full']};
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: {OSLO_DESIGN['colors']['primary']};
    }}
    
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Navigation Styles */
    .stRadio > div {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['white']} 0%, {OSLO_DESIGN['colors']['light']} 100%);
        border-radius: {OSLO_DESIGN['radius']['xl']};
        padding: {OSLO_DESIGN['spacing']['lg']};
        box-shadow: {OSLO_DESIGN['shadows']['md']};
        border: 1px solid {OSLO_DESIGN['colors']['light_gray']};
    }}
    
    .stRadio > div > label {{
        background: transparent;
        border-radius: {OSLO_DESIGN['radius']['lg']};
        padding: {OSLO_DESIGN['spacing']['md']} {OSLO_DESIGN['spacing']['lg']};
        margin: {OSLO_DESIGN['spacing']['xs']} 0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid transparent;
        font-family: {OSLO_DESIGN['typography']['font_family']};
        font-weight: {OSLO_DESIGN['typography']['font_weights']['medium']};
    }}
    
    .stRadio > div > label:hover {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['primary']}10 0%, {OSLO_DESIGN['colors']['secondary']}10 100%);
        border-color: {OSLO_DESIGN['colors']['primary']};
        transform: translateX(4px);
        box-shadow: {OSLO_DESIGN['shadows']['md']};
    }}
    
    .stRadio > div > label > div[data-testid="stMarkdownContainer"] {{
        font-family: {OSLO_DESIGN['typography']['font_family']};
    }}
    
    /* Tab Styles */
    .stTabs [data-baseweb="tab-list"] {{
        gap: {OSLO_DESIGN['spacing']['sm']};
        background: {OSLO_DESIGN['colors']['light']};
        border-radius: {OSLO_DESIGN['radius']['xl']};
        padding: {OSLO_DESIGN['spacing']['sm']};
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border-radius: {OSLO_DESIGN['radius']['lg']};
        padding: {OSLO_DESIGN['spacing']['md']} {OSLO_DESIGN['spacing']['lg']};
        color: {OSLO_DESIGN['colors']['medium_gray']};
        font-family: {OSLO_DESIGN['typography']['font_family']};
        font-weight: {OSLO_DESIGN['typography']['font_weights']['medium']};
        transition: all 0.3s ease;
        border: none;
    }}
    
    .stTabs [data-baseweb="tab"]:hover {{
        background: {OSLO_DESIGN['colors']['white']};
        color: {OSLO_DESIGN['colors']['primary']};
        box-shadow: {OSLO_DESIGN['shadows']['sm']};
    }}
    
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['primary']} 0%, {OSLO_DESIGN['colors']['secondary']} 100%);
        color: {OSLO_DESIGN['colors']['white']};
        box-shadow: {OSLO_DESIGN['shadows']['md']};
    }}
    
    /* Button Styles */
    .stButton > button {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['primary']} 0%, {OSLO_DESIGN['colors']['secondary']} 100%);
        border: none;
        border-radius: {OSLO_DESIGN['radius']['lg']};
        color: {OSLO_DESIGN['colors']['white']};
        font-family: {OSLO_DESIGN['typography']['font_family']};
        font-weight: {OSLO_DESIGN['typography']['font_weights']['semibold']};
        padding: {OSLO_DESIGN['spacing']['md']} {OSLO_DESIGN['spacing']['xl']};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: {OSLO_DESIGN['shadows']['md']};
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: {OSLO_DESIGN['shadows']['lg']};
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['primary_dark']} 0%, {OSLO_DESIGN['colors']['secondary_dark']} 100%);
    }}
    
    .stButton > button:active {{
        transform: translateY(0);
        box-shadow: {OSLO_DESIGN['shadows']['md']};
    }}
    
    /* Metric Styles */
    [data-testid="metric-container"] {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['white']} 0%, {OSLO_DESIGN['colors']['light']} 100%);
        border: 1px solid {OSLO_DESIGN['colors']['light_gray']};
        border-radius: {OSLO_DESIGN['radius']['xl']};
        padding: {OSLO_DESIGN['spacing']['lg']};
        box-shadow: {OSLO_DESIGN['shadows']['md']};
        transition: all 0.3s ease;
    }}
    
    [data-testid="metric-container"]:hover {{
        transform: translateY(-4px);
        box-shadow: {OSLO_DESIGN['shadows']['xl']};
    }}
    
    /* Sidebar Styles */
    .css-1d391kg {{
        background: linear-gradient(180deg, {OSLO_DESIGN['colors']['white']} 0%, {OSLO_DESIGN['colors']['light']} 100%);
        border-right: 1px solid {OSLO_DESIGN['colors']['light_gray']};
    }}
    
    /* Input Styles */
    .stTextInput > div > div > input {{
        border-radius: {OSLO_DESIGN['radius']['lg']};
        border: 2px solid {OSLO_DESIGN['colors']['light_gray']};
        font-family: {OSLO_DESIGN['typography']['font_family']};
        transition: all 0.3s ease;
    }}
    
    .stTextInput > div > div > input:focus {{
        border-color: {OSLO_DESIGN['colors']['primary']};
        box-shadow: 0 0 0 3px {OSLO_DESIGN['colors']['primary']}20;
    }}
    
    .stSelectbox > div > div > div {{
        border-radius: {OSLO_DESIGN['radius']['lg']};
        border: 2px solid {OSLO_DESIGN['colors']['light_gray']};
        font-family: {OSLO_DESIGN['typography']['font_family']};
    }}
    
    /* Dataframe Styles */
    .stDataFrame {{
        border-radius: {OSLO_DESIGN['radius']['xl']};
        overflow: hidden;
        box-shadow: {OSLO_DESIGN['shadows']['lg']};
        border: 1px solid {OSLO_DESIGN['colors']['light_gray']};
    }}
    
    /* Expander Styles */
    .streamlit-expanderHeader {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['light']} 0%, {OSLO_DESIGN['colors']['white']} 100%);
        border-radius: {OSLO_DESIGN['radius']['lg']};
        font-family: {OSLO_DESIGN['typography']['font_family']};
        font-weight: {OSLO_DESIGN['typography']['font_weights']['semibold']};
        border: 1px solid {OSLO_DESIGN['colors']['light_gray']};
        transition: all 0.3s ease;
    }}
    
    .streamlit-expanderHeader:hover {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['primary']}10 0%, {OSLO_DESIGN['colors']['secondary']}10 100%);
        border-color: {OSLO_DESIGN['colors']['primary']};
    }}
    
    /* Animation Classes */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes slideInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-30px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes pulse {{
        0%, 100% {{
            opacity: 1;
        }}
        50% {{
            opacity: 0.5;
        }}
    }}
    
    .fade-in-up {{
        animation: fadeInUp 0.6s ease-out;
    }}
    
    .slide-in-left {{
        animation: slideInLeft 0.6s ease-out;
    }}
    
    .pulse {{
        animation: pulse 2s infinite;
    }}
    
    /* Glass morphism effect */
    .glass {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: {OSLO_DESIGN['radius']['xl']};
    }}
    
    /* Oslo specific components */
    .oslo-card {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['white']} 0%, {OSLO_DESIGN['colors']['light']} 100%);
        border-radius: {OSLO_DESIGN['radius']['xl']};
        padding: {OSLO_DESIGN['spacing']['xl']};
        box-shadow: {OSLO_DESIGN['shadows']['lg']};
        border: 1px solid {OSLO_DESIGN['colors']['light_gray']};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}
    
    .oslo-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, {OSLO_DESIGN['colors']['primary']} 0%, {OSLO_DESIGN['colors']['secondary']} 50%, {OSLO_DESIGN['colors']['accent']} 100%);
    }}
    
    .oslo-card:hover {{
        transform: translateY(-8px);
        box-shadow: {OSLO_DESIGN['shadows']['xl']};
    }}
    
    .oslo-gradient-text {{
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['primary']} 0%, {OSLO_DESIGN['colors']['secondary']} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: {OSLO_DESIGN['typography']['font_weights']['bold']};
    }}
    
    /* Status indicators */
    .status-indicator {{
        display: inline-flex;
        align-items: center;
        padding: {OSLO_DESIGN['spacing']['xs']} {OSLO_DESIGN['spacing']['md']};
        border-radius: {OSLO_DESIGN['radius']['full']};
        font-size: {OSLO_DESIGN['typography']['font_sizes']['sm']};
        font-weight: {OSLO_DESIGN['typography']['font_weights']['medium']};
        font-family: {OSLO_DESIGN['typography']['font_family']};
    }}
    
    .status-success {{
        background: {OSLO_DESIGN['colors']['success']}20;
        color: {OSLO_DESIGN['colors']['success_dark']};
        border: 1px solid {OSLO_DESIGN['colors']['success']};
    }}
    
    .status-warning {{
        background: {OSLO_DESIGN['colors']['warning']}20;
        color: {OSLO_DESIGN['colors']['warning_dark']};
        border: 1px solid {OSLO_DESIGN['colors']['warning']};
    }}
    
    .status-danger {{
        background: {OSLO_DESIGN['colors']['danger']}20;
        color: {OSLO_DESIGN['colors']['danger_dark']};
        border: 1px solid {OSLO_DESIGN['colors']['danger']};
    }}
    
    .status-info {{
        background: {OSLO_DESIGN['colors']['info']}20;
        color: {OSLO_DESIGN['colors']['info_dark']};
        border: 1px solid {OSLO_DESIGN['colors']['info']};
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

def create_hero_section(title, subtitle, description, background_gradient=None):
    """Create a modern hero section"""
    
    if background_gradient is None:
        background_gradient = f"linear-gradient(135deg, {OSLO_DESIGN['colors']['primary']} 0%, {OSLO_DESIGN['colors']['secondary']} 50%, {OSLO_DESIGN['colors']['accent']} 100%)"
    
    hero_html = f"""
    <div style="
        background: {background_gradient};
        color: {OSLO_DESIGN['colors']['white']};
        padding: {OSLO_DESIGN['spacing']['xxxl']} {OSLO_DESIGN['spacing']['xl']};
        border-radius: {OSLO_DESIGN['radius']['xxl']};
        margin-bottom: {OSLO_DESIGN['spacing']['xl']};
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: {OSLO_DESIGN['shadows']['xl']};
    " class="fade-in-up">
        <div style="position: relative; z-index: 2;">
            <h1 style="
                margin: 0 0 {OSLO_DESIGN['spacing']['md']} 0;
                font-size: {OSLO_DESIGN['typography']['font_sizes']['display']};
                font-weight: {OSLO_DESIGN['typography']['font_weights']['extrabold']};
                font-family: {OSLO_DESIGN['typography']['font_family']};
                line-height: 1.2;
            ">{title}</h1>
            <h2 style="
                margin: 0 0 {OSLO_DESIGN['spacing']['lg']} 0;
                font-size: {OSLO_DESIGN['typography']['font_sizes']['xl']};
                font-weight: {OSLO_DESIGN['typography']['font_weights']['medium']};
                opacity: 0.9;
                font-family: {OSLO_DESIGN['typography']['font_family']};
            ">{subtitle}</h2>
            <p style="
                margin: 0;
                font-size: {OSLO_DESIGN['typography']['font_sizes']['lg']};
                opacity: 0.8;
                max-width: 600px;
                margin: 0 auto;
                line-height: 1.6;
                font-family: {OSLO_DESIGN['typography']['font_family']};
            ">{description}</p>
        </div>
        <div style="
            position: absolute;
            top: -50%;
            right: -20%;
            width: 200px;
            height: 200px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            opacity: 0.5;
        "></div>
        <div style="
            position: absolute;
            bottom: -30%;
            left: -10%;
            width: 150px;
            height: 150px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 50%;
            opacity: 0.7;
        "></div>
    </div>
    """
    
    st.markdown(hero_html, unsafe_allow_html=True)

def create_modern_metric_card(title, value, description, icon, color_scheme="primary", trend=None):
    """Create a modern metric card with enhanced visuals"""
    
    color_map = {
        "primary": OSLO_DESIGN['colors']['primary'],
        "success": OSLO_DESIGN['colors']['success'],
        "warning": OSLO_DESIGN['colors']['warning'],
        "danger": OSLO_DESIGN['colors']['danger'],
        "info": OSLO_DESIGN['colors']['info'],
        "secondary": OSLO_DESIGN['colors']['secondary']
    }
    
    main_color = color_map.get(color_scheme, OSLO_DESIGN['colors']['primary'])
    light_color = f"{main_color}15"
    
    trend_html = ""
    if trend:
        trend_color = OSLO_DESIGN['colors']['success'] if trend.startswith('+') else OSLO_DESIGN['colors']['danger']
        trend_html = f"""
        <div style="
            display: flex;
            align-items: center;
            margin-top: {OSLO_DESIGN['spacing']['sm']};
            font-size: {OSLO_DESIGN['typography']['font_sizes']['sm']};
            color: {trend_color};
            font-weight: {OSLO_DESIGN['typography']['font_weights']['medium']};
        ">
            <span style="margin-right: {OSLO_DESIGN['spacing']['xs']};">
                {'↗️' if trend.startswith('+') else '↘️'}
            </span>
            {trend}
        </div>
        """
    
    card_html = f"""
    <div class="oslo-card slide-in-left" style="
        background: linear-gradient(135deg, {OSLO_DESIGN['colors']['white']} 0%, {light_color} 100%);
        text-align: center;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    ">
        <div style="
            font-size: 3rem;
            margin-bottom: {OSLO_DESIGN['spacing']['md']};
            color: {main_color};
        ">{icon}</div>
        <div style="
            font-size: {OSLO_DESIGN['typography']['font_sizes']['xxxl']};
            font-weight: {OSLO_DESIGN['typography']['font_weights']['bold']};
            color: {main_color};
            margin-bottom: {OSLO_DESIGN['spacing']['xs']};
            font-family: {OSLO_DESIGN['typography']['font_family']};
        ">{value}</div>
        <div style="
            font-size: {OSLO_DESIGN['typography']['font_sizes']['md']};
            font-weight: {OSLO_DESIGN['typography']['font_weights']['semibold']};
            color: {OSLO_DESIGN['colors']['dark']};
            margin-bottom: {OSLO_DESIGN['spacing']['xs']};
            font-family: {OSLO_DESIGN['typography']['font_family']};
        ">{title}</div>
        <div style="
            font-size: {OSLO_DESIGN['typography']['font_sizes']['sm']};
            color: {OSLO_DESIGN['colors']['medium_gray']};
            font-family: {OSLO_DESIGN['typography']['font_family']};
        ">{description}</div>
        {trend_html}
    </div>
    """
    
    return card_html

def create_feature_showcase_card(title, description, icon, features_list, color="primary"):
    """Create a feature showcase card"""
    
    color_map = {
        "primary": OSLO_DESIGN['colors']['primary'],
        "success": OSLO_DESIGN['colors']['success'],
        "warning": OSLO_DESIGN['colors']['warning'],
        "danger": OSLO_DESIGN['colors']['danger'],
        "info": OSLO_DESIGN['colors']['info'],
        "secondary": OSLO_DESIGN['colors']['secondary']
    }
    
    main_color = color_map.get(color, OSLO_DESIGN['colors']['primary'])
    
    features_html = ""
    for feature in features_list:
        features_html += f"""
        <div style="
            display: flex;
            align-items: center;
            margin-bottom: {OSLO_DESIGN['spacing']['sm']};
            font-size: {OSLO_DESIGN['typography']['font_sizes']['md']};
            color: {OSLO_DESIGN['colors']['dark_gray']};
            font-family: {OSLO_DESIGN['typography']['font_family']};
        ">
            <span style="
                color: {main_color};
                margin-right: {OSLO_DESIGN['spacing']['md']};
                font-weight: {OSLO_DESIGN['typography']['font_weights']['bold']};
            ">✓</span>
            {feature}
        </div>
        """
    
    card_html = f"""
    <div class="oslo-card" style="height: 100%;">
        <div style="
            display: flex;
            align-items: center;
            margin-bottom: {OSLO_DESIGN['spacing']['lg']};
        ">
            <div style="
                font-size: 2.5rem;
                margin-right: {OSLO_DESIGN['spacing']['md']};
                color: {main_color};
            ">{icon}</div>
            <div>
                <h3 style="
                    margin: 0;
                    font-size: {OSLO_DESIGN['typography']['font_sizes']['xl']};
                    font-weight: {OSLO_DESIGN['typography']['font_weights']['bold']};
                    color: {OSLO_DESIGN['colors']['dark']};
                    font-family: {OSLO_DESIGN['typography']['font_family']};
                ">{title}</h3>
            </div>
        </div>
        <p style="
            margin: 0 0 {OSLO_DESIGN['spacing']['lg']} 0;
            font-size: {OSLO_DESIGN['typography']['font_sizes']['md']};
            color: {OSLO_DESIGN['colors']['medium_gray']};
            line-height: 1.6;
            font-family: {OSLO_DESIGN['typography']['font_family']};
        ">{description}</p>
        <div>{features_html}</div>
    </div>
    """
    
    return card_html

def create_status_badge(text, status_type="info"):
    """Create a modern status badge"""
    
    return f'<span class="status-indicator status-{status_type}">{text}</span>'

def create_modern_plotly_theme():
    """Create a modern Plotly theme matching the Oslo design"""
    
    return {
        'layout': {
            'font': {
                'family': OSLO_DESIGN['typography']['font_family'],
                'size': 12,
                'color': OSLO_DESIGN['colors']['dark_gray']
            },
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'colorway': [
                OSLO_DESIGN['colors']['primary'],
                OSLO_DESIGN['colors']['secondary'],
                OSLO_DESIGN['colors']['accent'],
                OSLO_DESIGN['colors']['success'],
                OSLO_DESIGN['colors']['warning'],
                OSLO_DESIGN['colors']['info'],
                OSLO_DESIGN['colors']['danger']
            ],
            'title': {
                'font': {
                    'family': OSLO_DESIGN['typography']['font_family'],
                    'size': 18,
                    'color': OSLO_DESIGN['colors']['dark']
                },
                'x': 0.5,
                'xanchor': 'center'
            },
            'xaxis': {
                'gridcolor': OSLO_DESIGN['colors']['light_gray'],
                'linecolor': OSLO_DESIGN['colors']['medium_gray'],
                'tickcolor': OSLO_DESIGN['colors']['medium_gray'],
                'title_font': {'size': 14}
            },
            'yaxis': {
                'gridcolor': OSLO_DESIGN['colors']['light_gray'],
                'linecolor': OSLO_DESIGN['colors']['medium_gray'],
                'tickcolor': OSLO_DESIGN['colors']['medium_gray'],
                'title_font': {'size': 14}
            },
            'margin': {'l': 60, 'r': 60, 't': 80, 'b': 60}
        }
    }

def create_loading_animation():
    """Create a loading animation"""
    
    loading_html = f"""
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        padding: {OSLO_DESIGN['spacing']['xl']};
    ">
        <div style="
            width: 40px;
            height: 40px;
            border: 4px solid {OSLO_DESIGN['colors']['light_gray']};
            border-top: 4px solid {OSLO_DESIGN['colors']['primary']};
            border-radius: 50%;
            animation: spin 1s linear infinite;
        "></div>
    </div>
    
    <style>
    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    </style>
    """
    
    return loading_html

if __name__ == "__main__":
    # Demo of the design system
    st.set_page_config(page_title="Oslo Design System", layout="wide")
    inject_advanced_css()
    
    create_hero_section(
        "🎨 Oslo Design System",
        "Professional UI Components",
        "Modern, accessible, and beautiful design components for Oslo Planning Premium"
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(create_modern_metric_card(
            "Total Documents", "150", "Verified planning docs", "📋", "primary", "+12%"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_modern_metric_card(
            "Categories", "8", "Complete coverage", "🎯", "success", "+5%"
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_modern_metric_card(
            "Completion", "94%", "Implementation rate", "✅", "info", "+2%"
        ), unsafe_allow_html=True)