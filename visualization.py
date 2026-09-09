def print_summary(donors, receivers, matches):
    total_food = sum(d["quantity_kg"] for d in donors)
    total_need = sum(r["required_kg"] for r in receivers)
    matched_food = sum(m["quantity_kg"] for m in matches)

    print("\n--- Project Summary ---")
    print(f"Total donated food: {total_food:.1f} kg")
    print(f"Total receiver requirement: {total_need:.1f} kg")
    print(f"Food included in recommended matches: {matched_food:.1f} kg")
    print(f"Number of recommendations: {len(matches)}")
