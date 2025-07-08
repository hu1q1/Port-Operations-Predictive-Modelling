# Maritime Port Operation Predictive Modeling for Vessel Loading/Unloading Duration

### Problem Context

Maritime port operations encompass a wide range of activities involved in managing the movement of ships, cargo, and passengers through a port. This includes vessel traffic management, loading and unloading cargo, customs clearance, storage, and logistics coordination. 

Efficient and well-managed port operations are crucial for reducing turnaround times, improving supply chain efficiency, and facilitating international trade. 

### Problem Statement

Vessel loading & unloading duration is a key factor to consider when deciding how to schedule vessels to ensure smooth operations.

If vessel scheduling relies on inaccurate estimates, it would lead to either under-utilization of resources (if overestimated) or delays and bottlenecks (if underestimated).

Therefore, the accurate prediction of port operation durations can help facilitate decision-making in resource allocation to ensure a smooth and efficient flow of movement within the port. An ML model can learn from historical data to provide more precise estimates, allowing for proactive adjustments and identifying factors that significantly impact duration.

### Project Goal 

To build a ML model using Scikit-learn to accurately predict the time required for cargo operations (loading and unloading containers) for arriving vessels. 

Predicting the exact duration of a vessel's stay for cargo operations is complex. In this project, we will limit the scope to these factors: the size and type of the vessel, the total amount of cargo (measured in TEU - Twenty-foot Equivalent Units), the mix of cargo types (standard, reefer, hazardous), the number and type of cranes assigned, labor availability (gang size), weather conditions, and even congestion at other points in the terminal.

This prediction can help the port optimize resource allocation (cranes, labor, internal transport), improve scheduling, reduce vessel waiting times, and ultimately enhance operational efficiency.


### Workflow

1. Data Generation (using Pandas & NumPy)
Real-world port operational data is typically proprietary and collected from various internal systems. Therefore, this project shall be based on fictitious data generated with plausible values based on credible sources.
1a. {WIP} EDA (also to verify data generation)

2. Data Cleaning & Preprocessing (using Pandas & Scikit-learn Preprocessing modules)
Transformation of raw data into a format suitable for ML algorithms and removal of noisy data.

3. Data Splitting (using Scikit-learn Model Selection module)
Ensures the model's performance is evaluated on unseen data to prevent overfitting.

4. Model Selection & Training (using Scikit-learn Estimators module)
Use of various regression algorithms for prediction.

5. Hyperparameter Tuning & Model Evaluation (using Scikit-learn Metrics)
To quantify our models' performances for comparison.

6. Interpretation & Identifying Opportunities for Efficiency Improvements
Gain actionable insights from the model.

Note: as the analysis is based on fictitious data, the conclusions derived from it are not indicative of what is happening in actual ports. However, once the fictitious datasets are replaced with actual ones, the workflow can be easily re-run and re-interpreted to obtain high business impact insights for port operation efficiency improvements.
