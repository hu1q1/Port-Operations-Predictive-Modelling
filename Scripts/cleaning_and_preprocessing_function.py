import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def clean_n_preprocess(df):
    # --- 1. Handle missing data: Imputation ---

    median_gang_size = df['Gang_Size_per_Crane'].median()
    df.fillna({'Gang_Size_per_Crane': round(median_gang_size)}, inplace=True)
    mean_wind_speed = df['Average_Wind_Speed'].mean()
    df.fillna({'Average_Wind_Speed': mean_wind_speed}, inplace=True)

    # --- 2. Change to correct data types ---
    df['Arrival_Date'] = pd.to_datetime(df['Arrival_Date'])
    categorical_cols_to_convert = ['Day_of_Week_Arrival', 'Vessel_Type', 'Berth_Used', 'Precipitation']
    for col in categorical_cols_to_convert:
        df[col] = df[col].astype('category')
    df['Gang_Size_per_Crane'] = df['Gang_Size_per_Crane'].astype(int) #in case the median result in decimals

    # print("\n --------------------- DataFrame info before encoding and scaling: ---------------------")
    # df.info()

    # --- 3. Drop some columns and split into X & Y features ---

    # Exclude Vessel_ID as it's an identifier and Arrival_Date as we'd typically engineer features from it first
    # If Arrival_Date was to be used, feature engineering (extracting month, day, etc.) would happen *before* this step.
    # Let's assume for now Arrival_Date is not directly used in this encoding/scaling step but other features are.
    X = df.drop(columns=['Actual_Operation_Duration_Hours', 'Vessel_ID', 'Arrival_Date']) #13 colums currently
    y = df['Actual_Operation_Duration_Hours']

    # print("\n --------------------- Features (X) head: ---------------------")
    # print(X.head())

    # --- 4. Handle preprocessing of categorical & numerical features separately ---

    categorical_features = X.select_dtypes(include=['category', 'object']).columns.tolist()
    # Ensure Vessel_Type is treated as categorical even if it only has one value in our generated data
    if 'Vessel_Type' not in categorical_features and 'Vessel_Type' in X.columns:
        categorical_features.append('Vessel_Type')

    numerical_features = X.select_dtypes(include=np.number).columns.tolist()

    # If any numerical features were unintentionally captured as object/category,
    # or vice-versa, they should be corrected here or earlier.
    # For example, if 'Time_of_Day_Arrival' was object, convert to int.

    # print(f"\nCategorical features identified: {categorical_features}")
    # print(f"Numerical features identified: {numerical_features}")

    # Preprocessing for numerical data: StandardScaler
    numerical_transformer = StandardScaler()

    # Preprocessing for categorical data: OneHotEncoder
    # handle_unknown='ignore' will prevent errors if new categories appear in test data
    # drop='first' can be used to avoid multicollinearity if desired, especially for linear models
    categorical_transformer = OneHotEncoder(handle_unknown='ignore', sparse_output=False, drop=None)


    # --- 5. Combine Transformers using ColumnTransformer ---
    # This applies the specified transformers to the correct columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ],
        remainder='passthrough' # Use 'drop' if want to drop columns not specified
                            # 'passthrough' keeps them as is. For well-defined X, 'drop' is safer. ####################################### POTENTIAL FOR IMPROVEMENT: more meaningful preprocessing & feature engineering ##################################
                            # use 'drop' to ensure only processed features remain.
        # remainder='drop' # For this exercise, it's better to ensure only transformed features are used
    )

    # --- 6. Apply the Preprocessing ---

    # Fit and transform the data
    return preprocessor.fit_transform(X)