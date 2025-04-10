import sqlite3

def init_db():
    conn = sqlite3.connect("db/farming_memory.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agent_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_name TEXT,
        decision TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def log_decision(agent_name, decision):
    conn = sqlite3.connect("db/farming_memory.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO agent_logs (agent_name, decision) VALUES (?, ?)", (agent_name, decision))
    conn.commit()
    conn.close()
