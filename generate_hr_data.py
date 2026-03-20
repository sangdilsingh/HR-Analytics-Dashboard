import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker('en_IN')
np.random.seed(42)
random.seed(42)

NUM_EMPLOYEES = 100000

departments = ['HR', 'Finance', 'IT', 'Sales', 'Marketing', 'Operations', 'Legal', 'R&D']
job_roles = {
    'HR': ['HR Executive', 'HR Manager', 'Recruiter', 'HR Analyst', 'HRBP'],
    'Finance': ['Accountant', 'Finance Analyst', 'Finance Manager', 'CFO', 'Tax Analyst'],
    'IT': ['Software Engineer', 'Data Analyst', 'IT Manager', 'System Admin', 'DevOps Engineer', 'MIS Analyst'],
    'Sales': ['Sales Executive', 'Sales Manager', 'BDM', 'Regional Head', 'Key Account Manager'],
    'Marketing': ['Marketing Executive', 'Content Writer', 'SEO Analyst', 'Brand Manager', 'Growth Hacker'],
    'Operations': ['Operations Executive', 'Operations Manager', 'Logistics Head', 'MIS Analyst', 'Process Analyst'],
    'Legal': ['Legal Executive', 'Compliance Officer', 'Legal Manager', 'Contract Analyst'],
    'R&D': ['Research Analyst', 'Data Scientist', 'ML Engineer', 'Research Head', 'AI Engineer']
}
education_levels = ['High School', 'Diploma', 'Bachelor', 'Master', 'PhD']
gender_options = ['Male', 'Female', 'Non-Binary']
marital_status_options = ['Single', 'Married', 'Divorced']
locations = ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Pune', 'Chennai', 'Kolkata', 'Dehradun', 'Noida', 'Gurgaon', 'Ahmedabad', 'Jaipur']
hire_years = list(range(2010, 2025))
companies = ['TechCorp India', 'FinEdge Solutions', 'DataMinds Pvt Ltd', 'RetailMax', 'HR First', 'OptiLogix', 'LegalEase', 'Innovate R&D']

print('Generating 1,00,000 rows... please wait')

records = []
for i in range(NUM_EMPLOYEES):
    dept = random.choice(departments)
    role = random.choice(job_roles[dept])
    gender = random.choices(gender_options, weights=[55, 40, 5])[0]
    age = random.randint(21, 60)
    experience = random.randint(0, min(age - 20, 25))
    education = random.choices(education_levels, weights=[5, 15, 50, 25, 5])[0]
    marital = random.choice(marital_status_options)
    location = random.choice(locations)
    hire_year = random.choice(hire_years)
    company = random.choice(companies)

    base_salary = {
        'HR': 35000, 'Finance': 50000, 'IT': 65000, 'Sales': 40000,
        'Marketing': 42000, 'Operations': 38000, 'Legal': 55000, 'R&D': 70000
    }[dept]
    salary = int(base_salary + (experience * 3500) + random.randint(-8000, 15000))
    salary = max(18000, salary)

    performance = random.choices([1, 2, 3, 4, 5], weights=[5, 10, 35, 35, 15])[0]
    overtime = random.choices(['Yes', 'No'], weights=[35, 65])[0]
    wlb = random.choices([1, 2, 3, 4], weights=[10, 25, 40, 25])[0]
    job_sat = random.choices([1, 2, 3, 4], weights=[10, 20, 40, 30])[0]
    training_hours = random.randint(0, 100)
    leaves_taken = random.randint(0, 30)
    promotions = random.randint(0, min(experience // 2 + 1, 5))

    attrition_score = 0
    if performance <= 2: attrition_score += 2
    if overtime == 'Yes': attrition_score += 1
    if wlb <= 2: attrition_score += 2
    if job_sat <= 2: attrition_score += 2
    if salary < 30000: attrition_score += 1
    if experience < 2: attrition_score += 1
    if leaves_taken > 20: attrition_score += 1
    attrition_prob = min(0.05 + attrition_score * 0.055, 0.75)
    attrition = 'Yes' if random.random() < attrition_prob else 'No'

    records.append({
        'EmployeeID': f'EMP{100001 + i}',
        'Age': age,
        'Gender': gender,
        'MaritalStatus': marital,
        'Education': education,
        'Department': dept,
        'JobRole': role,
        'Company': company,
        'Location': location,
        'HireYear': hire_year,
        'YearsAtCompany': 2025 - hire_year,
        'ExperienceYears': experience,
        'MonthlySalary': salary,
        'PerformanceRating': performance,
        'JobSatisfaction': job_sat,
        'WorkLifeBalance': wlb,
        'OverTime': overtime,
        'TrainingHoursPerYear': training_hours,
        'LeavesTaken': leaves_taken,
        'Promotions': promotions,
        'Attrition': attrition
    })

    if (i+1) % 10000 == 0:
        print(f'  {i+1:,} rows done...')

df = pd.DataFrame(records)
df.to_csv('hr_dataset_100k.csv', index=False)

print(f'\nDataset ready: {len(df):,} rows | {len(df.columns)} columns')
print(f'Attrition Rate: {df["Attrition"].value_counts(normalize=True)["Yes"]*100:.1f}%')
print(f'Avg Salary: Rs {df["MonthlySalary"].mean():,.0f}')