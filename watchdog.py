import time
from chou_sismos_v3 import main

def surveillance_continue(interval_minutes: int = 30):
    while True:
        print("\n=== Nouvelle analyse CHOU‑Sismographe ===")
        main()
        print(f"Prochaine analyse dans {interval_minutes} minutes...")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    surveillance_continue(30)
