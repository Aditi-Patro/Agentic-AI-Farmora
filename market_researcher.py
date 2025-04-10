import pandas as pd
from db.memory import log_decision

def run_market_researcher():
    print("[Market Researcher] Loading market dataset...")

    df = pd.read_csv("market_researcher_dataset.csv")

    if "crop" in df.columns and "demand" in df.columns and "price_per_kg" in df.columns:
        top_crops = df.sort_values(by=["demand", "price_per_kg"], ascending=[False, False])
        if not top_crops.empty:
            top_crop = top_crops.iloc[0]
            message = f"Recommended crop: {top_crop['crop']} - Demand: {top_crop['demand']}, Price: ₹{top_crop['price_per_kg']} per kg"
            print(f"[Market Researcher] {message}")
            log_decision("Market Researcher", message)
