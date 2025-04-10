import pandas as pd
from db.memory import log_decision

def run_farmer_advisor():
    print("[Farmer Advisor] Loading farmer dataset...")

    df = pd.read_csv("farmer_advisor_dataset.csv")

    for index, row in df.iterrows():
        soil = row.get("soil_type", "unknown")
        budget = row.get("budget", 0)

        if soil == "loamy" and budget > 5000:
            crop = "Wheat"
        elif soil == "sandy":
            crop = "Millet"
        else:
            crop = "Legumes"

        message = f"Suggested crop: {crop} for soil '{soil}' and budget {budget}"
        print(f"[Farmer Advisor] {message}")
        log_decision("Farmer Advisor", message)
