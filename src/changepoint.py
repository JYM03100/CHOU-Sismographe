def detecter_ruptures_avance(series, seuil_ratio: float = 0.5):
    if not series:
        return []

    moyenne = sum(series) / len(series)
    seuil = moyenne * seuil_ratio

    ruptures = []
    for i in range(1, len(series)):
        if abs(series[i] - series[i - 1]) > seuil:
            ruptures.append({"index": i, "valeur": float(series[i])})

    return ruptures
