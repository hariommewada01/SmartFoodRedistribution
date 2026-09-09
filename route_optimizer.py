from distance import haversine_km
from emergency import priority_score, priority_label

def optimize_routes(donors, receivers):
    routes = []

    for receiver in receivers:
        best = None

        for donor in donors:
            if donor["food_type"].lower() != receiver["accepted_food"].lower():
                continue
            if donor["quantity_kg"] <= 0:
                continue

            distance = haversine_km(
                donor["latitude"], donor["longitude"],
                receiver["latitude"], receiver["longitude"]
            )

            # Priority dominates distance so emergency needs are handled first.
            route_score = priority_score(receiver["priority"]) * 1000 - distance

            candidate = {
                "score": route_score,
                "donor_name": donor["name"],
                "receiver_name": receiver["name"],
                "distance_km": distance,
                "priority": priority_label(receiver["priority"])
            }

            if best is None or candidate["score"] > best["score"]:
                best = candidate

        if best:
            routes.append(best)

    routes.sort(key=lambda x: (-priority_score_from_label(x["priority"]), x["distance_km"]))
    return routes

def priority_score_from_label(label):
    return {"Normal": 1, "High": 2, "Emergency": 3}.get(label, 1)
