"""
Membersihkan Social Media Engagement Dataset.
Dataset sumber menggunakan pemisah titik koma (;), bukan koma.
"""
from pathlib import Path
import pandas as pd
import csv

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "Social Media Engagement Dataset.csv"
OUTPUT = ROOT / "data" / "social_media_engagement_clean.csv"

def clean_data(source=SOURCE, output=OUTPUT):
    df = pd.read_csv(
        source,
        sep=";",
        engine="python",
        quoting=csv.QUOTE_NONE,
        on_bad_lines="warn"
    )
    df["timestamp"] = pd.to_datetime(
        df["timestamp"], format="%d/%m/%Y %H:%M", errors="coerce"
    )
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].fillna("").astype(str).str.strip()

    numeric_cols = [
        "sentiment_score", "toxicity_score", "likes_count", "shares_count",
        "comments_count", "impressions", "engagement_rate",
        "user_past_sentiment_avg", "user_engagement_growth", "buzz_change_rate"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    before = len(df)
    df = df.drop_duplicates().dropna(subset=["timestamp"])
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False, encoding="utf-8-sig")
    print(f"Baris sebelum: {before:,}")
    print(f"Baris sesudah: {len(df):,}")
    print(f"Duplikat/ tanggal invalid yang dihapus: {before-len(df):,}")
    print(f"File bersih tersimpan: {output}")
    print("Catatan: nilai mentions yang kosong dipertahankan sebagai string kosong.")
    return df

if __name__ == "__main__":
    clean_data()
