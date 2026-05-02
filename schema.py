SCHEMA = """
Table: customers
Columns:
- customerID: text, unique customer identifier
- gender: text, values: Male, Female
- SeniorCitizen: bigint, values: 0 (not senior), 1 (senior)
- Partner: text, values: Yes, No
- Dependents: text, values: Yes, No
- tenure: bigint,description: number of months customer has been with company
- PhoneService: text, values: Yes, No
- MultipleLines: text, values: Yes, No , No phone service
- InternetService: text, values: DSL, Fiber optic, No
- OnlineSecurity: text, values: Yes, No, No internet service
- OnlineBackup: text,  values: Yes, No, No internet service
- DeviceProtection: text, values: Yes, No, No internet service
- TechSupport: text, values: Yes, No, No internet service
- StreamingTV: text, values: Yes, No, No internet service
- StreamingMovies: text, values: Yes, No,No internet service
- Contract: text, values: Month-to-Month,One year,Two year
- PaperlessBilling: text, values: Yes, No
- PaymentMethod: text,values: Electronic check,Mailed check,Bank transfer(automatic),Credit card(automatic)
- MonthlyCharges: double precision,description:monthly bill amount
- TotalCharges: double precision,description:total amount charged to customer
- Churn: bigint,values: 0 (not churned), 1 (churned)
"""