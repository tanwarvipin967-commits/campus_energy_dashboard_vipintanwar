
import os
import pandas as pd
import matplotlib.pyplot as plt
from classes import MeterReading, BuildingManager
from utils import calculate_daily_totals, calculate_weekly_aggregates, building_wise_summary

DATA_DIR = "data"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("\n[1/5] Reading and validating data...")

df_list = []

for file in os.listdir(DATA_DIR):
    if file.endswith(".csv"):
        try:
            file_path = os.path.join(DATA_DIR, file)
            df = pd.read_csv(file_path)

            df['building'] = file.replace(".csv", "")

            df_list.append(df)

        except Exception as e:
            print(f"⚠ Error reading {file}: {e}")

df_combined = pd.concat(df_list, ignore_index=True)
df_combined.to_csv(f"{OUTPUT_DIR}/cleaned_energy_data.csv", index=False)

print("✔ Data successfully merged and saved.")

print("\n[2/5] Performing daily, weekly and building-wise aggregations...")

daily_totals = calculate_daily_totals(df_combined)
weekly_totals = calculate_weekly_aggregates(df_combined)
summary = building_wise_summary(df_combined)

summary.to_csv(f"{OUTPUT_DIR}/building_summary.csv")

print("✔ Aggregations completed and summary saved.")

print("\n[3/5] Creating object-oriented building models...")

bm = BuildingManager()

for _, row in df_combined.iterrows():
    reading = MeterReading(row['timestamp'], row['energy_kwh'])
    bm.add_reading(row['building'], reading)

reports = bm.generate_all_reports()

print("✔ OOP Models successfully created.")

print("\n[4/5] Generating dashboard visualization...")

plt.figure(figsize=(13, 9))

plt.subplot(3, 1, 1)
plt.plot(daily_totals.index, daily_totals.values)
plt.title("Daily Energy Consumption")
plt.ylabel("kWh")

plt.subplot(3, 1, 2)
plt.bar(weekly_totals.index.astype(str), weekly_totals.values)
plt.title("Weekly Energy Usage Summary")
plt.ylabel("kWh")

plt.subplot(3, 1, 3)
plt.scatter(df_combined['timestamp'], df_combined['energy_kwh'], s=10)
plt.title("Peak Hour Consumption")
plt.xlabel("Timestamp")
plt.ylabel("kWh")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/dashboard.png")

print("✔ Dashboard exported as dashboard.png.")

print("\n[5/5] Generating final textual summary...")

total_consumption = df_combined['energy_kwh'].sum()
highest_building = summary['sum'].idxmax()
peak_load = df_combined.loc[df_combined['energy_kwh'].idxmax()]

with open(f"{OUTPUT_DIR}/summary.txt", "w") as f:
    f.write("CAMPUS ENERGY SUMMARY REPORT\n")
    f.write("-------------------------------------\n")
    f.write(f"Total Campus Consumption: {total_consumption} energy_kwh\n")
    f.write(f"Highest Consuming Building: {highest_building}\n")
    f.write(f"Peak Load Time: {peak_load['timestamp']} ({peak_load['energy_kwh']} kWh)\n")

print("✔ Summary report saved as summary.txt.")
print("\n🎉 PROJECT COMPLETED SUCCESSFULLY!")
