from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Social Media Engagement", page_icon="📊", layout="wide")
ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "social_media_engagement_clean.csv"

st.markdown("""
<style>
.main {background-color:#f6f8fc;}
.block-container {padding-top:1.6rem; padding-bottom:2rem;}
[data-testid="stMetric"] {background:#ffffff; border:1px solid #e8edf5; padding:16px; border-radius:14px;}
h1,h2,h3 {color:#172554;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
    for col in ["likes_count","shares_count","comments_count","impressions","engagement_rate","sentiment_score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

df = load_data()
st.title("📊 Social Media Engagement Dashboard")
st.caption("Analisis interaksi, sentimen, dan performa konten media sosial | Dataset: 12.000+ observasi")

# Sidebar filters
st.sidebar.header("🎛️ Filter Dashboard")
platforms = sorted(df["platform"].dropna().unique().tolist())
selected_platforms = st.sidebar.multiselect("Platform", platforms, default=platforms)
date_min, date_max = df["timestamp"].min().date(), df["timestamp"].max().date()
date_range = st.sidebar.date_input("Rentang tanggal", value=(date_min, date_max), min_value=date_min, max_value=date_max)
sentiments = ["Semua"] + sorted(df["sentiment_label"].dropna().unique().tolist())
selected_sentiment = st.sidebar.selectbox("Sentimen", sentiments)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range[0]

filtered = df[
    df["platform"].isin(selected_platforms)
    & df["timestamp"].dt.date.between(start_date, end_date)
].copy()
if selected_sentiment != "Semua":
    filtered = filtered[filtered["sentiment_label"] == selected_sentiment]

if filtered.empty:
    st.warning("Tidak ada data untuk kombinasi filter ini. Silakan ubah filter.")
    st.stop()

# KPI cards
total_interactions = filtered[["likes_count","shares_count","comments_count"]].fillna(0).sum().sum()
avg_engagement = filtered["engagement_rate"].mean()
total_impressions = filtered["impressions"].fillna(0).sum()
total_posts = len(filtered)
k1,k2,k3,k4 = st.columns(4)
k1.metric("Total Interaksi", f"{total_interactions:,.0f}")
k2.metric("Rata-rata Engagement Rate", f"{avg_engagement:.2%}" if pd.notna(avg_engagement) else "—")
k3.metric("Total Impressions", f"{total_impressions:,.0f}")
k4.metric("Jumlah Postingan", f"{total_posts:,.0f}")

st.divider()
left,right = st.columns(2)
with left:
    st.subheader("Tren Interaksi dari Waktu ke Waktu")
    trend = filtered.set_index("timestamp").resample("W")[["likes_count","shares_count","comments_count"]].sum().reset_index()
    trend_long = trend.melt(id_vars="timestamp", var_name="Jenis Interaksi", value_name="Jumlah")
    fig = px.line(trend_long, x="timestamp", y="Jumlah", color="Jenis Interaksi", markers=True,
                  template="plotly_white", labels={"timestamp":"Tanggal","Jumlah":"Jumlah interaksi"})
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Rata-rata Engagement Rate per Platform")
    by_platform = filtered.groupby("platform", as_index=False)["engagement_rate"].mean().sort_values("engagement_rate", ascending=False)
    fig = px.bar(by_platform, x="platform", y="engagement_rate", color="platform",
                 template="plotly_white", labels={"platform":"Platform","engagement_rate":"Rata-rata engagement rate"})
    st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
with left:
    st.subheader("Komposisi Sentimen")
    sentiment = filtered["sentiment_label"].value_counts().rename_axis("Sentimen").reset_index(name="Jumlah")
    fig = px.pie(sentiment, names="Sentimen", values="Jumlah", hole=.48, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Hubungan Impressions dan Likes")
    fig = px.scatter(filtered, x="impressions", y="likes_count", color="sentiment_label",
                     hover_data=["platform","brand_name","topic_category"],
                     template="plotly_white", opacity=.65,
                     labels={"impressions":"Impressions","likes_count":"Likes","sentiment_label":"Sentimen"})
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Kategori Topik dengan Interaksi Terbesar")
topic = filtered.assign(total_interaksi=filtered[["likes_count","shares_count","comments_count"]].fillna(0).sum(axis=1))
topic = topic.groupby("topic_category", as_index=False)["total_interaksi"].sum().sort_values("total_interaksi", ascending=False).head(10)
fig = px.bar(topic, x="total_interaksi", y="topic_category", orientation="h", template="plotly_white",
             labels={"total_interaksi":"Total interaksi","topic_category":"Kategori topik"})
st.plotly_chart(fig, use_container_width=True)

# Dynamic insights
st.subheader("💡 Insight Otomatis")
top_platform = by_platform.iloc[0]["platform"] if not by_platform.empty else "—"
top_rate = by_platform.iloc[0]["engagement_rate"] if not by_platform.empty else float("nan")
top_sentiment = filtered["sentiment_label"].mode().iloc[0] if not filtered["sentiment_label"].mode().empty else "—"
top_topic = topic.iloc[0]["topic_category"] if not topic.empty else "—"
c1,c2 = st.columns(2)
with c1:
    st.info(f"**Platform dengan rata-rata engagement rate tertinggi:** {top_platform} ({top_rate:.2%})." if pd.notna(top_rate) else "Data engagement rate belum tersedia.")
    st.info(f"**Sentimen paling sering muncul:** {top_sentiment}.")
with c2:
    st.info(f"**Kategori topik dengan interaksi terbesar:** {top_topic}.")
    st.info(f"Dashboard sedang menampilkan **{len(filtered):,} postingan** setelah filter diterapkan.")

with st.expander("Lihat data hasil filter"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.download_button("⬇️ Unduh data hasil filter (CSV)", filtered.to_csv(index=False).encode("utf-8-sig"),
                       file_name="social_media_filtered.csv", mime="text/csv")

st.caption("Catatan: engagement rate dianalisis sebagai metrik historis/deskriptif, bukan prediksi engagement masa depan.")
