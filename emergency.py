def priority_label(priority):
    labels = {
        1: "Normal",
        2: "High",
        3: "Emergency"
    }
    return labels.get(priority, "Normal")

def priority_score(priority):
    return {1: 1, 2: 2, 3: 3}.get(priority, 1)
