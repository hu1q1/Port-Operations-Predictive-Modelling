Synthetic Dataset Description:

Vessel_ID: Unique identifier for each vessel call.
Data Type: String/Categorical (many unique values)
Example Values: 'V_0001', 'V_0002', ...
Source Basis: Internal port system identifiers. (No public source for specific IDs, just the concept of unique tracking).

Arrival_Date: Date of vessel arrival.
Data Type: Datetime
Example Values: '2022-01-05', '2022-03-18', ... (covering a period like 1-2 years)
Source Basis: Standard date format. Port historical logs cover time periods.

Time_of_Day_Arrival: Hour of arrival (0-23).
Data Type: Integer
Range: 0 to 23
Source Basis: Port operational data is recorded 24/7.

Day_of_Week_Arrival: Day of the week.
Data Type: Categorical
Example Values: 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'
Source Basis: Standard calendar days. Useful for checking weekend/weekday patterns.

Vessel_Type: Type of vessel.
Data Type: Categorical
Example Values: 'Container Ship' (Focusing on this for the project scope). In a real port, this could also include Bulk Carrier, Tanker, Ro-Ro, etc.
Source Basis: Maritime industry classification of vessels (e.g., Lloyd's Register, vessel databases like MarineTraffic).

Vessel_Size_GT: Gross Tonnage (a measure of vessel internal volume, proxy for size).
Data Type: Numerical (Integer/Float)
Plausible Range: 20,000 GT to 150,000 GT. (Covers a range from smaller feeder vessels to large Post-Panamax/early Neo-Panamax ships, common in many ports). Ultra-Large Container Vessels (ULCVs) can exceed 220,000 GT, but may not call at all ports.
Source Basis: Maritime databases (e.g., MarineTraffic, Clarkson Research), classification society data, industry reports on fleet size distribution.

Total_TEU_Planned: Total Twenty-foot Equivalent Units planned for handling (loading + unloading).
Data Type: Numerical (Integer)
Plausible Range: 500 TEU to 15,000 TEU. (Represents calls ranging from partial load/unload for smaller vessels to significant exchanges for large vessels). Note: This is the number of moves at this port call, not necessarily the vessel's total capacity.
Source Basis: Port throughput statistics (often reported in total TEU handled annually/monthly), container shipping line schedules and typical port calls, industry benchmarks on container handling volumes per vessel type.

Reefer_TEU_Planned: Number of refrigerated containers planned.
Data Type: Numerical (Integer)
Plausible Range: 0 to 1,500 TEU (Typically a percentage of total TEU). Can be 0 if no reefer cargo.
Source Basis: Global trade reports on reefer cargo volumes, specialized reefer shipping lines. Reefer cargo requires specific infrastructure and handling, potentially impacting duration.

Hazmat_TEU_Planned: Number of hazardous material containers planned.
Data Type: Numerical (Integer)
Plausible Range: 0 to 500 TEU (Typically a small percentage of total TEU due to regulations). Can be 0.
Source Basis: International Maritime Dangerous Goods (IMDG) code regulations, port safety reports. Handling hazmat requires specific procedures, potentially impacting duration.

Berth_Used: Identifier for the specific berth used by the vessel.
Data Type: Categorical
Example Values: 'Berth_A', 'Berth_B', 'Berth_C', 'Berth_D' (Assuming a terminal with a few berths).
Source Basis: Port infrastructure layout, terminal operator descriptions. Different berths may have different crane capacities, yard proximity, etc.

Num_Cranes_Assigned: Number of Ship-to-Shore (STS) cranes assigned to the vessel operation.
Data Type: Numerical (Integer)
Plausible Range: 2 to 6. (Common range for concurrent crane operations on a single vessel at a typical large berth). Very large vessels at mega-ports might use 7 or 8.
Source Basis: Port operator websites listing berth specifications, academic studies on terminal operations efficiency, industry benchmarks on crane intensity.

Gang_Size_per_Crane: Average size of the labor gang supporting each crane.
Data Type: Numerical (Integer)
Plausible Range: 18 to 25. (Typical range for a container handling gang including foremen, clerks, lashers, etc.).
Source Basis: Port labor union agreements (often public or discussed in news), descriptions of terminal operational roles.

Average_Wind_Speed: Average wind speed during the operation.
Data Type: Numerical (Float)
Plausible Range: 0.0 to 30.0 knots. (Higher speeds, e.g., >25 knots, can force a stop to crane operations).
Source Basis: Meteorological data for coastal port locations. Wind is a critical factor impacting crane productivity and safety.

Precipitation: Whether significant precipitation occurred during the operation.
Data Type: Categorical (Binary)
Example Values: 'Yes', 'No'
Source Basis: Meteorological data. Rain can slow down or stop operations.

Waiting_Time_Before_Berth: Time spent waiting at anchorage before berthing, in hours.
Data Type: Numerical (Float)
Plausible Range: 0.0 to 48.0 hours. (Highly variable depending on port congestion, weather, vessel schedule adherence). Can be 0 if the berth is immediately available.
Source Basis: Port congestion reports from shipping agents/logistics news, academic studies on port delays. Significant waiting time can sometimes impact subsequent operational efficiency or scheduling pressure.

Actual_Operation_Duration_Hours: The total time the vessel spent at berth for cargo operations (excluding idle time unrelated to cargo).
Data Type: Numerical (Float)
Plausible Range: 6.0 to 72.0 hours. (Derived realistically based on TEU, number of cranes, and a plausible crane productivity rate, plus added variability from other factors). Calculation basis: Duration ≈ Total_TEU_Planned / (Num_Cranes_Assigned * Average_Moves_per_Crane_per_Hour). Average Moves per Crane per Hour typically ranges from 20-35 depending on the port, equipment, and gang performance.
Source Basis: Industry benchmarks for container handling rates (moves/hour/crane) - e.g., reports from terminal operators, academic papers on port efficiency. The actual duration is the outcome variable recorded by the port.

Points to note about the generation of this dataset:
1. Values fall within the researched ranges.
2. Realistic relationships exist between features (e.g., larger TEU calls generally take longer, more cranes reduce time but with diminishing returns, high wind increases time). This might involve defining a base formula for Actual_Operation_Duration_Hours based on TEU and cranes, and then adding noise and adjustments based on other factors like weather, waiting time, and vessel size.
3. Introduce realistic levels of missing data for some columns (e.g., weather data or specific cargo details might occasionally be missing).
4. Include categorical data with reasonable distributions.
