# Smart Food Redistribution System

## 1. Project Overview
Smart Food Redistribution System is a command-line Python project that helps connect food donors with organizations or communities that need food.

The system considers:
- Type of food
- Available quantity
- Receiver requirement
- Geographic distance
- Receiver priority
- Suggested donor-receiver matches
- Route recommendations

## 2. Objectives
1. Reduce avoidable food wastage.
2. Connect available food with nearby receivers.
3. Give emergency requirements higher priority.
4. Use distance to make redistribution more practical.
5. Provide a simple terminal-based system that can run without a GUI.

## 3. Technologies Used
- Python 3.9 or later
- CSV files for sample data
- Python standard library
- Haversine formula for approximate geographic distance

No external Python package is required.

## 4. Project Structure
```text
SmartFoodRedistribution/
├── main.py
├── food_matching.py
├── emergency.py
├── distance.py
├── route_optimizer.py
├── database.py
├── visualization.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── data/
    ├── donors.csv
    └── receivers.csv
```

## 5. Installation

### Step 1: Install Python
Install Python 3.9 or newer and verify:

```bash
python --version
```

On some systems use:

```bash
python3 --version
```

### Step 2: Download or clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/SmartFoodRedistribution.git
cd SmartFoodRedistribution
```

Replace `YOUR-USERNAME` with the GitHub username of the repository owner.

### Step 3: Create a virtual environment (recommended)
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install dependencies
```bash
pip install -r requirements.txt
```

The requirements file is intentionally empty because the project uses only the Python standard library.

## 6. Run the Project
```bash
python main.py
```

Linux/macOS:
```bash
python3 main.py
```

## 7. Menu
The program provides:
1. View food donors
2. View food receivers
3. Find best food matches
4. Show optimized routes
5. Exit

## 8. Sample Workflow
Choose option `3` to generate donor-receiver recommendations.

The algorithm:
1. Checks whether food types are compatible.
2. Calculates approximate geographic distance.
3. Gives higher priority to emergency requirements.
4. Uses distance as a practical tie-breaker.
5. Displays the recommended matches.

## 9. Data Files
`data/donors.csv` contains donor information.

`data/receivers.csv` contains receiver requirements.

You can add your own rows while keeping the same column names.

# 10. Important Note
The coordinates and food records included in this repository are sample educational data. The route distance is an approximate straight-line geographic distance and is not a replacement for a live road-navigation service.

## 11. Author
Student Project - Smart Food Redistribution System
