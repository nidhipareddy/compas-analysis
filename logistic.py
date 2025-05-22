import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

def merge_as_planned(db_path):
    conn = sqlite3.connect(db_path)

    query = """
        SELECT
            ca.charge_degree AS arrest_charge_degree,
            p.id AS person_id,
            p.is_recid,
            p.juv_fel_count,
            p.juv_misd_count,
            p.juv_other_count,
            jh.in_custody AS prison_in,
            jh.out_custody AS prison_out,
            -- prison duration in days
            JULIANDAY(jh.out_custody) - JULIANDAY(jh.in_custody) AS prison_duration_days,
            c.legal_status,
            c.marital_status,
            p.race,
            p.sex,
            p.age,
            p.priors_count,
            p.c_charge_degree,
            ch.filing_type,
            ch.filing_agency,
            ch.charge AS initial_charge,
            ch.statute AS initial_statute
        FROM casearrest ca
        LEFT JOIN people p ON ca.person_id = p.id
        LEFT JOIN prisonhistory pr ON ca.person_id = pr.person_id
        LEFT JOIN jailhistory jh ON ca.person_id = jh.person_id
        LEFT JOIN compas c ON ca.person_id = c.person_id
        LEFT JOIN charge ch ON ca.case_number = ch.case_number
    """

    df = pd.read_sql_query(query, conn)
    return df

# Load data
path = "compas-analysis-master/compas.db"
df = merge_as_planned(path)

# Drop rows where values are missing
df.dropna(inplace=True)
print(df.head(5))
print(f"Shape of df we are working with {df.shape}")


# Prepare features (X) and target (y)
X = df.drop(columns=['person_id', 'is_recid'])  # drop 'person_id' and 'is_recid' for features
y = df['is_recid']  # target variable is whether recidivist (binary: 0 or 1)

# Define categorical and numeric columns
categorical_columns = ['arrest_charge_degree', 'legal_status', 'marital_status', 'race', 'sex', 'c_charge_degree', 'filing_type', 'filing_agency', 'initial_charge', 'initial_statute']
numeric_columns = ['juv_fel_count', 'juv_misd_count', 'juv_other_count', 'prison_duration_days', 'age', 'priors_count']

# Define column transformer (preprocessing)
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_columns),  # scale numeric columns
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)  # one-hot encode categorical columns
    ])

# Build the pipeline: preprocessing + logistic regression
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(solver='liblinear'))
])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=99)

# Fit the model
pipeline.fit(X_train, y_train)

# Predict on test data
y_pred = pipeline.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
