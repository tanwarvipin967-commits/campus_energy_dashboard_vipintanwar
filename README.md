# campus_energy_dashboard_vipintanwar
📘 Campus Energy-Use Dashboard
📌 Course:

Programming for Problem Solving Using Python

🧑‍💻 Capstone Project — Individual
🚀 Project Overview

This project analyzes energy-consumption data of different campus buildings and generates:

Cleaned combined dataset

Daily/weekly summaries

Building-wise statistics

Multi-chart dashboard

Automated text summary

Project uses Pandas for data handling and Matplotlib for visualization.

📂 Folder Structure
campus-energy-dashboard-yourname/
│
├── data/
│     ├── building1.csv
│     ├── building2.csv
│
├── output/
│     ├── cleaned_energy_data.csv
│     ├── building_summary.csv
│     ├── summary.txt
│     └── dashboard.png
│
├── main.py
└── README.md

⚙ How to Run
1. Install dependencies
pip install pandas matplotlib

2. Run main script
python main.py

3. Output generated in /output/ folder

cleaned_energy_data.csv – merged & cleaned data

building_summary.csv – building-wise stats

dashboard.png – visualization dashboard

summary.txt – key insights summary

🧩 Tasks Explained
✔ Task 1 — Data Ingestion

Read all CSVs from /data/

Add building metadata

Handle missing/corrupt files

Export cleaned dataset

✔ Task 2 — Aggregation

Daily totals

Weekly totals

Building summary (min, max, mean, total)

Export to CSV

✔ Task 3 — Object-Oriented Design

Classes used:

Building

MeterReading

BuildingManager

Data is structured using OOP for scalability.

✔ Task 4 — Visualization Dashboard

Generated with Matplotlib:

Daily trend lines

Weekly comparison

Peak-hour scatter insights

Saved as dashboard.png

✔ Task 5 — Summary Report

Automatically generates:

Total campus consumption

Highest consuming building

Peak trends

Saved as summary.txt

🧾 Academic Integrity

This is an individual assignment.

All code must be your own.

Do not copy others' work.

Acknowledge any datasets used.
