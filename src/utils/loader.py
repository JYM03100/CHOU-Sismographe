import pandas as pd

def charger_csv(path):
    """
    Charge un CSV contenant une colonne 'date'.
    """
    try:
        df = pd.read_csv(path)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date').set_index('date')
        return df
    except Exception as e:
        print(f"[ERREUR] Impossible de charger {path} : {e}")
        return None
