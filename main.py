from database import load_donors, load_receivers
from food_matching import find_matches
from emergency import priority_label
from route_optimizer import optimize_routes

def show_donors(donors):
    print("\n--- Food Donors ---")
    for d in donors:
        print(f"{d['id']}: {d['name']} | {d['food_type']} | {d['quantity_kg']} kg | {d['location']}")

def show_receivers(receivers):
    print("\n--- Food Receivers ---")
    for r in receivers:
        print(f"{r['id']}: {r['name']} | Need: {r['required_kg']} kg | {r['location']} | Priority: {priority_label(r['priority'])}")

def run_matching(donors, receivers):
    matches = find_matches(donors, receivers)
    print("\n--- Suggested Matches ---")
    if not matches:
        print("No suitable matches found.")
        return

    for m in matches:
        print(
            f"{m['donor_name']} -> {m['receiver_name']} | "
            f"{m['food_type']} | {m['quantity_kg']} kg | "
            f"{m['distance_km']} km | Priority: {m['priority']}"
        )

def run_routes(donors, receivers):
    routes = optimize_routes(donors, receivers)
    print("\n--- Optimized Routes ---")
    if not routes:
        print("No routes available.")
        return
    for route in routes:
        print(
            f"{route['donor_name']} -> {route['receiver_name']} | "
            f"{route['distance_km']} km | Priority: {route['priority']}"
        )

def main():
    donors = load_donors()
    receivers = load_receivers()

    while True:
        print("\n===================================")
        print(" SMART FOOD REDISTRIBUTION SYSTEM")
        print("===================================")
        print("1. View food donors")
        print("2. View food receivers")
        print("3. Find best food matches")
        print("4. Show optimized routes")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_donors(donors)
        elif choice == "2":
            show_receivers(receivers)
        elif choice == "3":
            run_matching(donors, receivers)
        elif choice == "4":
            run_routes(donors, receivers)
        elif choice == "5":
            print("Thank you for using Smart Food Redistribution System.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
