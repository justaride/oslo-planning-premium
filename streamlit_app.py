#!/usr/bin/env python3
"""
Oslo Planning Premium - Streamlit Cloud Entry Point

This is the main entry point for Streamlit Cloud deployment.
Streamlit Cloud looks for either app.py or streamlit_app.py in the root directory.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the main application
from oslo_planning_premium import create_premium_app

if __name__ == "__main__":
    create_premium_app()
