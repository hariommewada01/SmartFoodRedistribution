# PROJECT REPORT
# Smart Food Redistribution System

## 1. Introduction
Food wastage and unequal access to food are two problems that can exist at the same time. Restaurants, canteens, bakeries, grocery stores and community kitchens may have usable surplus food, while NGOs and community centers may require food support.

The Smart Food Redistribution System is a Python command-line project designed to demonstrate how basic data processing, matching logic, priority handling and distance calculation can be combined to support food redistribution.

## 2. Problem Statement
There is a need for a simple system that can identify suitable food donors for receivers and consider both urgency and distance when making recommendations.

## 3. Objectives
- Store donor and receiver information.
- Match compatible food categories.
- Compare available and required quantities.
- Calculate approximate distance.
- Give emergency requirements higher priority.
- Generate practical donor-receiver recommendations.
- Keep the project executable from a terminal.

## 4. Scope
The current version is an educational prototype. It works with CSV files and sample location coordinates. It does not perform live road navigation, online food-safety verification, user authentication, or real-time delivery tracking.

## 5. Technologies
- Python 3.9+
- CSV
- Standard Python libraries
- Haversine distance formula

## 6. System Modules

### 6.1 main.py
Provides the command-line menu and controls the application.

### 6.2 database.py
Reads donor and receiver records from CSV files and converts numeric values into usable Python data types.

### 6.3 distance.py
Calculates approximate geographic distance using the Haversine formula.

### 6.4 emergency.py
Converts numeric priority values into Normal, High and Emergency labels.

### 6.5 food_matching.py
Compares food categories, calculates distance and ranks possible matches.

### 6.6 route_optimizer.py
Selects a suitable donor for each receiver by combining priority and distance.

### 6.7 visualization.py
Contains a small text-based summary helper for future extension.

## 7. Algorithm

### Input
- Donor records
- Receiver records
- Food category
- Available quantity
- Required quantity
- Location coordinates
- Priority level

### Processing
1. Load CSV records.
2. Read donor and receiver information.
3. Compare food categories.
4. Ignore incompatible food types.
5. Calculate distance between donor and receiver.
6. Assign higher score to higher-priority receivers.
7. Use shorter distance as an additional preference.
8. Produce a list of recommended matches.

### Output
- Donor name
- Receiver name
- Food category
- Recommended quantity
- Approximate distance
- Priority

## 8. Distance Formula
The project uses the Haversine formula to estimate the great-circle distance between two points on Earth.

For latitude/longitude points:

a = sin²(Δφ/2) + cos(φ1)cos(φ2)sin²(Δλ/2)

c = 2 atan2(√a, √(1-a))

d = R × c

where R is approximately 6371 km.

## 9. Sample Result
A typical execution can display records such as:

```text
--- Suggested Matches ---
Campus Canteen -> Helping Hands NGO | Cooked Food | 60.0 kg | 4.2 km | Priority: Emergency
Fresh Bakery -> Child Care Center | Bakery | 25.0 kg | 5.1 km | Priority: Emergency
```

The exact distance depends on the coordinates stored in the CSV files.

## 10. Advantages
- Simple terminal interface
- Easy to understand and modify
- No external packages required
- Uses structured CSV data
- Considers emergency priority
- Considers geographic distance
- Can be extended to a database or web application

## 11. Limitations
- Uses sample/static data.
- Distance is straight-line distance rather than actual road distance.
- Does not track food expiry in the current version.
- Does not perform live delivery tracking.
- Does not connect to a real NGO or restaurant database.

## 12. Future Enhancements
- SQLite/MySQL database
- User login and role management
- Food expiry-date checking
- Real map and road-distance API
- Delivery status tracking
- Notifications
- Web or mobile interface
- Historical analytics and dashboards

## 13. Conclusion
The Smart Food Redistribution System demonstrates a practical use of programming for a social problem. The project combines file handling, data processing, geographic distance calculation, priority logic and command-line interaction in one small application. The modular design also makes it suitable for future expansion.

## 14. How to Run
```bash
python main.py
```

The complete setup and execution instructions are available in `README.md`.
