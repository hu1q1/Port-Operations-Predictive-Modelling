import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- Parameters for Data Generation ---
n_samples = 5000 # Number of vessel calls
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

# Plausible ranges/values based on research
vessel_gt_range = (20000, 150000)
total_teu_range = (500, 15000)
reefer_hazmat_pct_range = (0, 0.1) # Up to 10% reefer/hazmat
berths = ['Berth_A', 'Berth_B', 'Berth_C', 'Berth_D']
crane_range = (2, 6)
gang_size_range = (18, 25)
wind_speed_range = (0, 30) # knots
waiting_time_range = (0, 48) # hours

# Basis for duration calculation: TEU / (Cranes * Avg_Moves_per_Hour)
# Let's assume a base productivity rate and add variability
base_moves_per_crane_per_hour = 25
productivity_noise = 0.2 # +/- 20% variability

# --- Generate Data ---
data = {}
data['Vessel_ID'] = [f'V_{i+1:04d}' for i in range(n_samples)]

# Generate random dates and times
dates = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(n_samples)]
data['Arrival_Date'] = dates
data['Time_of_Day_Arrival'] = np.random.randint(0, 24, n_samples)
data['Day_of_Week_Arrival'] = [d.strftime('%a') for d in dates] # e.g., 'Mon'

data['Vessel_Type'] = ['Container Ship'] * n_samples # Simplify for this project. as of now all container ship vessel type
data['Vessel_Size_GT'] = np.random.uniform(vessel_gt_range[0], vessel_gt_range[1], n_samples)
data['Total_TEU_Planned'] = np.random.randint(total_teu_range[0], total_teu_range[1] + 1, n_samples)

# Generate Reefer and Hazmat as a percentage of Total TEU
data['Reefer_TEU_Planned'] = (data['Total_TEU_Planned'] * np.random.uniform(reefer_hazmat_pct_range[0], reefer_hazmat_pct_range[1], n_samples)).astype(int)
data['Hazmat_TEU_Planned'] = (data['Total_TEU_Planned'] * np.random.uniform(reefer_hazmat_pct_range[0], reefer_hazmat_pct_range[1], n_samples)).astype(int)

data['Berth_Used'] = np.random.choice(berths, n_samples)
data['Num_Cranes_Assigned'] = np.random.randint(crane_range[0], crane_range[1] + 1, n_samples)
data['Gang_Size_per_Crane'] = np.random.randint(gang_size_range[0], gang_size_range[1] + 1, n_samples) # Could add slight variation per crane/gang in reality

data['Average_Wind_Speed'] = np.random.uniform(wind_speed_range[0], wind_speed_range[1], n_samples)

# Introduce precipitation (e.g., 15% of days have precipitation)
data['Precipitation'] = np.random.choice(['No', 'Yes'], n_samples, p=[0.85, 0.15])

data['Waiting_Time_Before_Berth'] = np.random.uniform(waiting_time_range[0], waiting_time_range[1], n_samples)
# More likely to have shorter waits: Skew the distribution? use power low for illustration
data['Waiting_Time_Before_Berth'] = np.random.power(a=0.5, size=n_samples) * waiting_time_range[1] # Skew towards 0

# Calculate realistic Duration with noise and factor in wind/precipitation/waiting
# Basic formula: Duration = TEU / (Cranes * Avg_Moves_per_Hour)
# Add noise and impact of other factors
base_duration = data['Total_TEU_Planned'] / (data['Num_Cranes_Assigned'] * base_moves_per_crane_per_hour)

# Add noise relative to base duration
duration_noise = base_duration * np.random.uniform(-productivity_noise, productivity_noise, n_samples)

# Add impact of Wind (e.g., penalty for high wind)
wind_penalty = np.maximum(0, data['Average_Wind_Speed'] - 25) * 0.5 # Add 0.5 hours for every knot above 25

# Add impact of Precipitation (e.g., fixed penalty)
precipitation_penalty = np.where(data['Precipitation'] == 'Yes', 2.0, 0.0) # Add 2 hours if raining

# Add small impact for Hazmat/Reefer (e.g., slight overhead per container type)
hazmat_penalty = data['Hazmat_TEU_Planned'] * 0.01 # 0.01 hours per hazmat TEU
reefer_penalty = data['Reefer_TEU_Planned'] * 0.005 # 0.005 hours per reefer TEU

# Add small impact for waiting time (e.g., slight inefficiency after long wait)
waiting_impact = data['Waiting_Time_Before_Berth'] * 0.05 # 5% of waiting time adds to ops time

data['Actual_Operation_Duration_Hours'] = base_duration + duration_noise + wind_penalty + precipitation_penalty + hazmat_penalty + reefer_penalty + waiting_impact
# Ensure duration is not negative and has a minimum plausible value
data['Actual_Operation_Duration_Hours'] = np.maximum(data['Actual_Operation_Duration_Hours'], 6.0) # Minimum 6 hours

df = pd.DataFrame(data)

# Introduce some missing values (e.g., 5% missing wind data, 2% missing gang size)
for col in ['Average_Wind_Speed', 'Gang_Size_per_Crane']:
    mask = np.random.choice([True, False], size=len(df), p=[0.05, 0.95])
    df.loc[mask, col] = np.nan

# Save the generated dataset
df.to_csv("port_operations_log.csv", index=False)

print("Fictitious dataset 'port_operations_log.csv' generated.")
print(df.head())
print("\nMissing values:\n", df.isnull().sum())
print("\nDescribe target variable:\n", df['Actual_Operation_Duration_Hours'].describe())