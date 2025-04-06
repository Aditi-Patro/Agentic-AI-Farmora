from db.memory import init_db
from agents.farmer_advisor import run_farmer_advisor
from agents.market_researcher import run_market_researcher
from agents.weather_agent import run_weather_agent
from agents.expert_agent import run_expert_agent

def main():
    print("Initializing Sustainable Farming AI System...")
    init_db()

    run_farmer_advisor()
    run_market_researcher()
    run_weather_agent()
    run_expert_agent()

if __name__ == "__main__":
    main()
