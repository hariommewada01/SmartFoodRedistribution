from database import load_donors, load_receivers
from food_matching import find_matches
from route_optimizer import optimize_routes

donors = load_donors()
receivers = load_receivers()
matches = find_matches(donors, receivers)
routes = optimize_routes(donors, receivers)

assert len(donors) == 5
assert len(receivers) == 5
assert matches
assert routes
print("All basic project tests passed.")
