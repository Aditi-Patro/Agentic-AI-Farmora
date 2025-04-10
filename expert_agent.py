from db.memory import log_decision

def run_expert_agent():
    print("[Agricultural Expert] Analyzing sustainable practices...")
    
    # Simulated decision
    recommendation = "Use crop rotation and organic manure to reduce soil erosion."
    
    print(f"[Expert Agent] {recommendation}")
    log_decision("Expert Agent", recommendation)
