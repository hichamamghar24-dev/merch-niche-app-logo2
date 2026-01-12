import streamlit as st
import math

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Merch Niche Finder PRO",
    page_icon="📊",
    layout="wide"
)

# =========================
# STYLE PREMIUM
# =========================
st.markdown("""
<style>
body { background-color: #0e1117; color: white; }
.big-title { font-size: 40px; font-weight: 700; color: #ff9900; }
.card {
    background-color: #1f1f1f;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 15px;
}
button {
    background-color: #ff9900 !important;
    color: black !important;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="big-title">🚀 Merch Niche Finder PRO</div>', unsafe_allow_html=True)
st.caption("Helium 10–like tool for Merch by Amazon")

# =========================
# DASHBOARD
# =========================
col1, col2, col3, col4 = st.columns(4)
col1.metric("🔎 Niches analysées", "128")
col2.metric("🔥 Niches gagnantes", "41")
col3.metric("⚔️ Concurrence moyenne", "Medium")
col4.metric("📈 Opportunité moyenne", "79/100")

st.divider()

# =========================
# MENU
# =========================
mode = st.radio(
    "Choisissez un outil",
    [
        "🔎 Keyword Research",
        "📊 Analyse de niche (Score automatique)",
        "🧲 Suggestions de mots-clés"
    ]
)

# =========================
# KEYWORD RESEARCH
# =========================
if mode == "🔎 Keyword Research":
    st.subheader("🔎 Recherche de mots-clés")

    keyword = st.text_input("Mot-clé Merch", "funny cat shirt")

    if st.button("Analyser le mot-clé"):
        results = len(keyword) * 900
        volume = int(math.log(results + 1) * 10000)
        competition = "Faible" if results < 2000 else "Moyenne" if results < 6000 else "Élevée"
        score = min(100, int((volume / (results + 1)) * 10))

        st.markdown(f"""
        <div class="card">
        <b>Résultats Amazon :</b> {results}<br>
        <b>Volume estimé :</b> {volume}<br>
        <b>Concurrence :</b> {competition}<br>
        <b>Score opportunité :</b> {score}/100
        </div>
        """, unsafe_allow_html=True)

        if score >= 70:
            st.success("✅ Bonne niche Merch")
        elif score >= 40:
            st.warning("⚠️ Niche moyenne")
        else:
            st.error("❌ Trop concurrentielle")

# =========================
# ANALYSE DE NICHE
# =========================
if mode == "📊 Analyse de niche (Score automatique)":
    st.subheader("📊 Analyse complète de niche")

    niche = st.text_input("Niche Merch", "funny cats")

    if st.button("Analyser la niche"):
        competition = len(niche) * 1200
        demand = max(10, 100 - len(niche) * 2)
        profit = min(100, len(niche) * 6)
        seo = 100 if len(niche.split()) >= 3 else 60
        score = int((demand + profit + seo + max(10, 100 - competition // 100)) / 4)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("📦 Concurrence", competition)
        col2.metric("📈 Demande", f"{demand}/100")
        col3.metric("💰 Profit", f"{profit}/100")
        col4.metric("🔎 SEO", f"{seo}/100")

        st.progress(score)
        st.markdown(f"### 🔥 Score global : **{score}/100**")

        if score >= 75:
            st.success("✅ Niche EXCELLENTE")
        elif score >= 50:
            st.warning("⚠️ Niche exploitable")
        else:
            st.error("❌ Niche à éviter")

# =========================
# SUGGESTIONS KEYWORDS
# =========================
if mode == "🧲 Suggestions de mots-clés":
    st.subheader("🧲 Suggestions automatiques")

    base = st.text_input("Mot-clé principal", "cat shirt")

    if st.button("Générer"):
        suggestions = [
            f"funny {base}",
            f"{base} gift",
            f"{base} for men",
            f"{base} for women",
            f"cute {base}",
            f"vintage {base}"
        ]

        for s in suggestions:
            st.markdown(f"👉 **{s}**")

        st.success("Suggestions générées")
