from distance import haversine_km
from emergency import priority_score, priority_label

def find_matches(donors, receivers):
    candidates = []

    for donor in donors:
        for receiver in receivers:
            if donor["food_type"].lower() != receiver["accepted_food"].lower():
                continue
            if donor["quantity_kg"] <= 0 or receiver["required_kg"] <= 0:
                continue

            distance = haversine_km(
                donor["latitude"], donor["longitude"],
                receiver["latitude"], receiver["longitude"]
            )

            # Higher priority first, then shorter distance.
            score = priority_score(receiver["priority"]) * 100 - distance
            quantity = min(donor["quantity_kg"], receiver["required_kg"])

            candidates.append({
                "score": score,
                "donor_name": donor["name"],
                "receiver_name": receiver["name"],
                "food_type": donor["food_type"],
                "quantity_kg": quantity,
                "distance_km": distance,
                "priority": priority_label(receiver["priority"])
            })

    candidates.sort(key=lambda x: (-x["score"], x["distance_km"]))

    # Keep one best recommendation per donor/receiver pair.
    result = []
    used_donors = set()
    used_receivers = set()

    for item in candidates:
        key_d = item["donor_name"]
        key_r = item["receiver_name"]
        if key_d not in used_donors and key_r not in used_receivers:
            result.append(item)
            used_donors.add(key_d)
            used_receivers.add(key_r)

    return result
