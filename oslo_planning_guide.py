#!/usr/bin/env python3
"""
Oslo Planning Guide - Interactive Planning Document Hierarchy
Comprehensive guide for navigating Oslo's planning framework
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import pandas as pd

# Import Oslo colors and premium components
from oslo_planning_premium import OSLO_COLORS

def render_planning_guide():
    """Render the comprehensive Oslo Planning Guide"""
    
    st.markdown("## 📋 Oslo Planleggingsguide - Dokumenthierarki")
    st.markdown("*Interaktiv guide for navigering i Oslos planverk*")
    
    # Header with key information
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {OSLO_COLORS['primary']} 0%, {OSLO_COLORS['secondary']} 100%);
                color: white; padding: 2rem; border-radius: 15px; margin-bottom: 2rem;">
        <h3 style="margin: 0 0 1rem 0;">🎯 Komplettguide til Oslo Planverk</h3>
        <p style="margin: 0; font-size: 1.1rem; opacity: 0.9;">
            Fra juridisk bindende planer til praktiske implementeringstips
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive hierarchy tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "⚖️ Juridisk Bindende",
        "📏 Kommunale Normer", 
        "🎯 Strategier & Føringer",
        "🌱 Miljø & Klima",
        "🏗️ Tematiske Planer",
        "💡 Praktiske Tips"
    ])
    
    with tab1:
        render_juridisk_bindende()
    
    with tab2:
        render_kommunale_normer()
    
    with tab3:
        render_strategier_foringer()
    
    with tab4:
        render_miljo_klima()
    
    with tab5:
        render_tematiske_planer()
    
    with tab6:
        render_praktiske_tips()

def render_juridisk_bindende():
    """Render juridisk bindende planer section"""
    
    st.markdown("### ⚖️ Juridisk Bindende Overordnede Planer")
    st.markdown("**🚨 MÅ FØLGES** - Disse planene er juridisk bindende")
    
    # Kommuneplan section
    st.markdown("#### 🏛️ Kommuneplan")
    
    kommuneplan_data = [
        {
            'plan': 'Kommuneplan 2015 - Juridisk arealdel',
            'status': 'Juridisk bindende',
            'beskrivelse': 'Det øverste juridisk bindende plandokumentet',
            'prioritet': 'Kritisk',
            'url': 'https://www.oslo.kommune.no/politikk/kommuneplan/'
        },
        {
            'plan': 'Kommuneplanens samfunnsdel 2025',
            'status': 'Førende',
            'beskrivelse': 'Gir føringer for byutviklingen',
            'prioritet': 'Høy',
            'url': 'https://www.oslo.kommune.no/politikk/kommuneplan/'
        }
    ]
    
    for plan in kommuneplan_data:
        priority_color = OSLO_COLORS['danger'] if plan['prioritet'] == 'Kritisk' else OSLO_COLORS['warning']
        
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid {priority_color}; margin-bottom: 1rem;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div style="flex: 1;">
                    <h4 style="margin: 0 0 0.5rem 0; color: {OSLO_COLORS['dark']};">
                        📋 {plan['plan']}
                    </h4>
                    <p style="margin: 0 0 1rem 0; color: #666;">{plan['beskrivelse']}</p>
                    <div style="display: flex; gap: 1rem;">
                        <span style="background: {priority_color}; color: white; 
                                   padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.8rem;">
                            {plan['prioritet']}
                        </span>
                        <span style="background: #E8F4FD; color: {OSLO_COLORS['primary']}; 
                                   padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.8rem;">
                            {plan['status']}
                        </span>
                    </div>
                </div>
                <a href="{plan['url']}" target="_blank" style="
                    background: {OSLO_COLORS['primary']}; color: white; 
                    padding: 0.5rem 1rem; border-radius: 8px; text-decoration: none;
                    font-size: 0.9rem; margin-left: 1rem;">
                    📖 Les mer
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Reguleringsplaner section
    st.markdown("#### 🗺️ Gjeldende Reguleringsplaner")
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #FFF3CD 0%, #FCF3CF 100%);
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid {OSLO_COLORS['warning']};">
        <h4 style="margin: 0 0 1rem 0; color: {OSLO_COLORS['dark']};">
            🔍 Sjekk Planinnsyn
        </h4>
        <p style="margin: 0; color: #666;">
            <strong>Viktig:</strong> Sjekk alltid Planinnsyn for å se om det finnes gjeldende 
            reguleringsplaner for ditt spesifikke område før du starter planleggingen.
        </p>
        <a href="https://innsyn.pbe.oslo.kommune.no/saksinnsyn/" target="_blank" 
           style="display: inline-block; margin-top: 1rem; background: {OSLO_COLORS['warning']}; 
                  color: white; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none;">
            🗺️ Åpne Planinnsyn
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Kommunedelplaner section
    st.markdown("#### 🏙️ Kommunedelplaner (hvis relevant)")
    
    kommunedelplaner = [
        'Kommunedelplan for torg og møteplasser',
        'Kommunedelplan for lokalisering av varehandel'
    ]
    
    for plan in kommunedelplaner:
        st.markdown(f"""
        <div style="background: #F8F9FA; padding: 1rem; border-radius: 8px; 
                    margin-bottom: 0.5rem; border-left: 3px solid {OSLO_COLORS['secondary']};">
            📋 <strong>{plan}</strong>
        </div>
        """, unsafe_allow_html=True)

def render_kommunale_normer():
    """Render kommunale normer section"""
    
    st.markdown("### 📏 Kommunale Normer")
    st.markdown("**📋 Forventes fulgt** og innarbeides i planbestemmelser")
    
    st.markdown("#### 🚨 Kritiske Normer for Utbygging")
    
    normer = [
        {
            'norm': 'Parkeringsnorm for bolig og næring',
            'beskrivelse': 'Fastsetter krav til antall parkeringsplasser',
            'relevans': 'Alle byggeprosjekter',
            'konsekvens': 'Juridisk bindende gjennom planbestemmelser'
        },
        {
            'norm': 'Norm for vegetasjon og vannhåndtering (blågrønn faktor)',
            'beskrivelse': 'Krav til grønne løsninger og overvannshåndtering',
            'relevans': 'Alle utbyggingsprosjekter',
            'konsekvens': 'Påvirker byggbar areal og kostnader'
        },
        {
            'norm': 'Norm for leke- og uteoppholdsarealer',
            'beskrivelse': 'Krav til uteareal for barn og opphold',
            'relevans': 'Boligprosjekter',
            'konsekvens': 'Påvirker utforming og arealøkonomi'
        },
        {
            'norm': 'Leilighetsfordeling i indre Oslo – normer',
            'beskrivelse': 'Krav til fordeling av leilighetsstørrelser',
            'relevans': 'Kun indre by',
            'konsekvens': 'Påvirker prosjektets økonomi og salgsbarhet'
        }
    ]
    
    for norm in normer:
        relevans_color = OSLO_COLORS['danger'] if 'Alle' in norm['relevans'] else OSLO_COLORS['warning']
        
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid {relevans_color}; margin-bottom: 1rem;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h4 style="margin: 0 0 0.5rem 0; color: {OSLO_COLORS['dark']};">
                📏 {norm['norm']}
            </h4>
            <p style="margin: 0 0 1rem 0; color: #666;">{norm['beskrivelse']}</p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <strong style="color: {OSLO_COLORS['primary']};">Relevans:</strong><br>
                    <span style="color: #666;">{norm['relevans']}</span>
                </div>
                <div>
                    <strong style="color: {OSLO_COLORS['primary']};">Konsekvens:</strong><br>
                    <span style="color: #666;">{norm['konsekvens']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Important note about norms
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #D1ECF1 0%, #BEE5EB 100%);
                padding: 1.5rem; border-radius: 10px; border-left: 4px solid {OSLO_COLORS['primary']};">
        <h4 style="margin: 0 0 1rem 0; color: {OSLO_COLORS['dark']};">
            💡 Viktig om normene
        </h4>
        <ul style="margin: 0; color: #666;">
            <li><strong>Normene blir ofte juridisk bindende</strong> gjennom planbestemmelsene</li>
            <li><strong>Avvik må begrunnes godt</strong> og kan være vanskelig å få godkjent</li>
            <li><strong>Innarbeid normene tidlig</strong> i prosjekteringen for å unngå problemer senere</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def render_strategier_foringer():
    """Render strategier og føringer section"""
    
    st.markdown("### 🎯 Strategier og Planer som Gir Viktige Føringer")
    
    # Subsections with expandable content
    
    # Byutvikling og arkitektur
    with st.expander("🏗️ For byutvikling og arkitektur", expanded=True):
        byutvikling_strategier = [
            {
                'strategi': 'Strategi for høyhus i Oslo',
                'beskrivelse': 'Retningslinjer for høybygg og lokalisering',
                'relevans': 'Bygninger over 8 etasjer'
            },
            {
                'strategi': 'Arkitekturpolitikk for Oslo',
                'beskrivelse': 'Kvalitetskrav til arkitektur og utforming',
                'relevans': 'Alle byggeprosjekter'
            },
            {
                'strategi': 'Kulturmiljøstrategi 2023-2034',
                'beskrivelse': 'Håndtering av kulturminner og kulturmiljø',
                'relevans': 'Prosjekter med kulturverdier'
            },
            {
                'strategi': 'Strategi for grønne tak og fasader',
                'beskrivelse': 'Fremme av grønne løsninger på bygninger',
                'relevans': 'Alle byggeprosjekter'
            }
        ]
        
        for strategi in byutvikling_strategier:
            st.markdown(f"""
            <div style="background: #F8F9FA; padding: 1rem; border-radius: 8px; 
                        margin-bottom: 0.5rem; border-left: 3px solid {OSLO_COLORS['secondary']};">
                <strong style="color: {OSLO_COLORS['dark']};">📋 {strategi['strategi']}</strong><br>
                <span style="color: #666; font-size: 0.9rem;">{strategi['beskrivelse']}</span><br>
                <span style="background: {OSLO_COLORS['light']}; color: {OSLO_COLORS['primary']}; 
                           padding: 0.2rem 0.5rem; border-radius: 12px; font-size: 0.8rem; margin-top: 0.5rem; display: inline-block;">
                    🎯 {strategi['relevans']}
                </span>
            </div>
            """, unsafe_allow_html=True)
    
    # Spesifikke områder
    with st.expander("📍 For spesifikke områder (hvis relevant)"):
        omrade_planer = [
            {
                'plan': 'Strategisk plan for Hovinbyen',
                'omrade': 'Hovinbyen',
                'beskrivelse': 'Utviklingsplan for Hovinbyen området'
            },
            {
                'plan': 'Helhetlig utviklingsplan for Groruddalen',
                'omrade': 'Groruddalen',
                'beskrivelse': 'Oppgradering og utvikling av Groruddalen'
            },
            {
                'plan': 'Estetisk plan – Designhåndbok Oslo sentrum',
                'omrade': 'Oslo sentrum',
                'beskrivelse': 'Designretningslinjer for sentrumsområdet'
            }
        ]
        
        for plan in omrade_planer:
            st.markdown(f"""
            <div style="background: #FFF3CD; padding: 1rem; border-radius: 8px; 
                        margin-bottom: 0.5rem; border-left: 3px solid {OSLO_COLORS['warning']};">
                <strong style="color: {OSLO_COLORS['dark']};">📍 {plan['plan']}</strong><br>
                <span style="color: #666; font-size: 0.9rem;">{plan['beskrivelse']}</span><br>
                <span style="background: {OSLO_COLORS['warning']}; color: white; 
                           padding: 0.2rem 0.5rem; border-radius: 12px; font-size: 0.8rem; margin-top: 0.5rem; display: inline-block;">
                    📍 Kun {plan['omrade']}
                </span>
            </div>
            """, unsafe_allow_html=True)
    
    # Infrastruktur og mobilitet
    with st.expander("🚴 For infrastruktur og mobilitet"):
        mobilitet_planer = [
            'Plan for sykkelveinettet',
            'Sykkelstrategi 2015-2025',
            'Rekkefølgebestemmelser i indre by (hvis i indre by)'
        ]
        
        for plan in mobilitet_planer:
            st.markdown(f"""
            <div style="background: #D1ECF1; padding: 1rem; border-radius: 8px; 
                        margin-bottom: 0.5rem; border-left: 3px solid {OSLO_COLORS['accent']};">
                🚴 <strong>{plan}</strong>
            </div>
            """, unsafe_allow_html=True)

def render_miljo_klima():
    """Render miljø og klima section"""
    
    st.markdown("### 🌱 Miljø- og Klimaplaner")
    st.markdown("**🌍 Viktige for bærekraft** - påvirker alle utbyggingsprosjekter")
    
    klima_planer = [
        {
            'plan': 'Klimastrategi for Oslo mot 2030',
            'beskrivelse': 'Oslos overordnede klimastrategi og utslippsmål',
            'påvirkning': 'Krav til energiløsninger og utslippsreduksjon',
            'relevans': 'Alle prosjekter'
        },
        {
            'plan': 'Strategi for overvannshåndtering',
            'beskrivelse': 'Håndtering av overvann og flomforebygging',
            'påvirkning': 'Krav til blågrønne løsninger og drenering',
            'relevans': 'Alle utbyggingsprosjekter'
        },
        {
            'plan': 'Handlingsplan for overvannshåndtering',
            'beskrivelse': 'Konkrete tiltak for overvannshåndtering',
            'påvirkning': 'Spesifikke tekniske krav og løsninger',
            'relevans': 'Områder med overvannsutfordringer'
        }
    ]
    
    for plan in klima_planer:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #D4EDDA 0%, #C3E6CB 100%);
                    padding: 1.5rem; border-radius: 10px; border-left: 4px solid {OSLO_COLORS['success']};
                    margin-bottom: 1rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <h4 style="margin: 0 0 0.5rem 0; color: {OSLO_COLORS['dark']};">
                🌱 {plan['plan']}
            </h4>
            <p style="margin: 0 0 1rem 0; color: #666;">{plan['beskrivelse']}</p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <strong style="color: {OSLO_COLORS['success']};">Påvirkning:</strong><br>
                    <span style="color: #666; font-size: 0.9rem;">{plan['påvirkning']}</span>
                </div>
                <div>
                    <strong style="color: {OSLO_COLORS['success']};">Relevans:</strong><br>
                    <span style="color: #666; font-size: 0.9rem;">{plan['relevans']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Climate impact visualization
    st.markdown("#### 📊 Klimapåvirkning på Prosjekter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Climate requirements chart
        klima_krav = {
            'Energiløsninger': 85,
            'Overvannshåndtering': 75, 
            'Grønne tak/fasader': 60,
            'Materialvalg': 70,
            'Transport/mobilitet': 65
        }
        
        fig_klima = go.Figure(data=[
            go.Bar(
                x=list(klima_krav.values()),
                y=list(klima_krav.keys()),
                orientation='h',
                marker_color=OSLO_COLORS['success'],
                text=[f"{v}%" for v in klima_krav.values()],
                textposition='inside'
            )
        ])
        
        fig_klima.update_layout(
            title="Klimakrav - Påvirkning på Prosjekter (%)",
            xaxis_title="Påvirkning",
            height=400,
            font_family="Arial"
        )
        
        st.plotly_chart(fig_klima, use_container_width=True)
    
    with col2:
        st.markdown("#### 💡 Klimatips for Planleggere")
        
        klimatips = [
            "Start med klimavurdering tidlig i prosessen",
            "Vurder alternative energiløsninger",
            "Planlegg for framtidens klimaendringer", 
            "Integrer blågrønne løsninger fra start",
            "Dokumenter klimagevinster i søknaden"
        ]
        
        for i, tip in enumerate(klimatips, 1):
            st.markdown(f"""
            <div style="background: white; padding: 1rem; border-radius: 8px; 
                        margin-bottom: 0.5rem; border-left: 3px solid {OSLO_COLORS['success']};">
                <strong style="color: {OSLO_COLORS['success']};">{i}.</strong> {tip}
            </div>
            """, unsafe_allow_html=True)

def render_tematiske_planer():
    """Render tematiske planer section"""
    
    st.markdown("### 🏗️ Tematiske Planer")
    st.markdown("**📋 Avhengig av prosjekttype** - gjelder spesifikke typer utbygging")
    
    # Boligprosjekter
    with st.expander("🏠 For boligprosjekter", expanded=True):
        bolig_planer = [
            {
                'plan': 'Handlingsplan for økt boligbygging',
                'beskrivelse': 'Tiltak for å øke boligproduksjonen i Oslo',
                'relevans': 'Alle boligprosjekter',
                'fordeler': 'Kan gi raskere saksbehandling og incentiver'
            },
            {
                'plan': 'Temaplan for kommunale boliger 2024-2033',
                'beskrivelse': 'Plan for kommunal boligutvikling',
                'relevans': 'Kommunale boligprosjekter',
                'fordeler': 'Spesiell saksbehandling og finansieringsordninger'
            }
        ]
        
        for plan in bolig_planer:
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                        border-left: 4px solid {OSLO_COLORS['accent']}; margin-bottom: 1rem;
                        box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h4 style="margin: 0 0 0.5rem 0; color: {OSLO_COLORS['dark']};">
                    🏠 {plan['plan']}
                </h4>
                <p style="margin: 0 0 1rem 0; color: #666;">{plan['beskrivelse']}</p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div>
                        <strong style="color: {OSLO_COLORS['accent']};">Relevans:</strong><br>
                        <span style="color: #666; font-size: 0.9rem;">{plan['relevans']}</span>
                    </div>
                    <div>
                        <strong style="color: {OSLO_COLORS['accent']};">Fordeler:</strong><br>
                        <span style="color: #666; font-size: 0.9rem;">{plan['fordeler']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Universell utforming
    with st.expander("♿ For prosjekter med universell utforming"):
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #E2E3F3 0%, #D6D8E7 100%);
                    padding: 1.5rem; border-radius: 10px; border-left: 4px solid {OSLO_COLORS['primary']};">
            <h4 style="margin: 0 0 1rem 0; color: {OSLO_COLORS['dark']};">
                ♿ Strategi for universell utforming
            </h4>
            <p style="margin: 0 0 1rem 0; color: #666;">
                Retningslinjer for tilgjengelighet og universell utforming i alle byggeprosjekter.
                Spesielt viktig for offentlige bygninger og større boligprosjekter.
            </p>
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <strong style="color: {OSLO_COLORS['primary']};">Viktige områder:</strong>
                <ul style="margin: 0.5rem 0 0 0; color: #666;">
                    <li>Tilgjengelige innganger og rømningsveier</li>
                    <li>Heisløsninger og trappeløsninger</li>
                    <li>Uteområder og parkering</li>
                    <li>Sanitæranlegg og oppholdsområder</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_praktiske_tips():
    """Render praktiske tips section"""
    
    st.markdown("### 💡 Praktiske Tips for Planleggere")
    
    # Workflow steps
    st.markdown("#### 🔄 Anbefalt Arbeidsflyt")
    
    workflow_steps = [
        {
            'steg': 1,
            'tittel': 'Start alltid med',
            'beskrivelse': 'Grunnleggende kartlegging',
            'oppgaver': [
                'Sjekk Planinnsyn for gjeldende planer',
                'Les kommuneplanens arealdel',
                'Identifiser relevante kommunedelplaner'
            ]
        },
        {
            'steg': 2,
            'tittel': 'Innarbeid normene tidlig',
            'beskrivelse': 'Juridisk forankring',
            'oppgaver': [
                'Normene blir ofte juridisk bindende gjennom planbestemmelsene',
                'Avvik må begrunnes godt',
                'Beregn konsekvenser for prosjektøkonomi'
            ]
        },
        {
            'steg': 3,
            'tittel': 'Bruk Plan- og bygningsetatens veiledere',
            'beskrivelse': 'Oppdatert veiledning',
            'oppgaver': [
                'Se Plan- og bygningsetatens område for oppdaterte veiledere',
                'Følg med på nye retningslinjer',
                'Delta på informasjonsmøter'
            ]
        },
        {
            'steg': 4,
            'tittel': 'Ta kontakt med Plan- og bygningsetaten',
            'beskrivelse': 'Proaktiv dialog',
            'oppgaver': [
                'Book et oppstartsmøte tidlig',
                'Avklar hvilke planer som gjelder for ditt spesifikke område',
                'Diskuter utfordringer og løsninger'
            ]
        }
    ]
    
    for step in workflow_steps:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; 
                    border-left: 4px solid {OSLO_COLORS['primary']}; margin-bottom: 1rem;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="background: {OSLO_COLORS['primary']}; color: white; 
                           width: 2.5rem; height: 2.5rem; border-radius: 50%; 
                           display: flex; align-items: center; justify-content: center; 
                           font-weight: bold; margin-right: 1rem;">
                    {step['steg']}
                </div>
                <div>
                    <h4 style="margin: 0; color: {OSLO_COLORS['dark']};">{step['tittel']}</h4>
                    <p style="margin: 0; color: #666; font-size: 0.9rem;">{step['beskrivelse']}</p>
                </div>
            </div>
            <ul style="margin: 0; color: #666;">
        """, unsafe_allow_html=True)
        
        for oppgave in step['oppgaver']:
            st.markdown(f"                <li>{oppgave}</li>", unsafe_allow_html=True)
        
        st.markdown("            </ul></div>", unsafe_allow_html=True)
    
    # Important considerations
    st.markdown("#### ⚠️ Husk at relevante dokumenter varierer")
    
    variasjoner = [
        {
            'faktor': 'Geografisk plassering',
            'eksempel': 'Sentrum vs. ytre by har ulike krav',
            'ikon': '📍'
        },
        {
            'faktor': 'Type utbygging',
            'eksempel': 'Bolig, næring, eller kombinert bruk',
            'ikon': '🏗️'
        },
        {
            'faktor': 'Størrelse og kompleksitet',
            'eksempel': 'Store prosjekter har flere krav',
            'ikon': '📏'
        },
        {
            'faktor': 'Spesielle forhold på tomten',
            'eksempel': 'Kulturminner, naturverdier, flomrisiko',
            'ikon': '🏛️'
        }
    ]
    
    col1, col2 = st.columns(2)
    
    for i, variasjon in enumerate(variasjoner):
        col = col1 if i % 2 == 0 else col2
        
        with col:
            st.markdown(f"""
            <div style="background: {OSLO_COLORS['light']}; padding: 1rem; border-radius: 8px; 
                        margin-bottom: 1rem; border-left: 3px solid {OSLO_COLORS['secondary']};">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.5rem; margin-right: 0.5rem;">{variasjon['ikon']}</span>
                    <strong style="color: {OSLO_COLORS['dark']};">{variasjon['faktor']}</strong>
                </div>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">{variasjon['eksempel']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Contact information
    st.markdown("#### 📞 Viktige Kontakter")
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {OSLO_COLORS['primary']} 0%, {OSLO_COLORS['secondary']} 100%);
                color: white; padding: 2rem; border-radius: 15px; margin-top: 2rem;">
        <h4 style="margin: 0 0 1rem 0;">📞 Plan- og bygningsetaten</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
            <div>
                <p style="margin: 0 0 0.5rem 0;"><strong>📧 E-post:</strong></p>
                <p style="margin: 0 0 1rem 0;">postmottak.pbe@oslo.kommune.no</p>
                <p style="margin: 0 0 0.5rem 0;"><strong>📞 Telefon:</strong></p>
                <p style="margin: 0;">21 80 21 80</p>
            </div>
            <div>
                <p style="margin: 0 0 0.5rem 0;"><strong>🌐 Nettsider:</strong></p>
                <p style="margin: 0 0 1rem 0;">oslo.kommune.no/plan-bygg-og-eiendom/</p>
                <p style="margin: 0 0 0.5rem 0;"><strong>🗺️ Planinnsyn:</strong></p>
                <p style="margin: 0;">innsyn.pbe.oslo.kommune.no</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_planning_guide()