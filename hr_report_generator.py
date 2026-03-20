import pandas as pd
from fpdf import FPDF
import sqlite3

# Data load
conn = sqlite3.connect(r"C:\Users\dell\OneDrive\Documents\Raw_Data\hr_database.db")

# SQL se insights nikalenge
attrition = pd.read_sql("SELECT Department, COUNT(*) as Attrited FROM hr_data WHERE Attrition='Yes' GROUP BY Department ORDER BY Attrited DESC", conn)
salary = pd.read_sql("SELECT Department, ROUND(AVG(MonthlySalary),0) as Avg_Salary FROM hr_data GROUP BY Department ORDER BY Avg_Salary DESC", conn)
overtime = pd.read_sql("SELECT OverTime, ROUND(COUNT(*)*100.0/SUM(COUNT(*)) OVER(),1) as Percentage FROM hr_data GROUP BY OverTime", conn)
conn.close()

# PDF banana
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 20)
pdf.set_fill_color(33, 97, 140)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 15, "HR Analytics Report", fill=True, ln=True, align="C")
pdf.ln(5)

# Section 1 - Attrition
pdf.set_font("Arial", "B", 14)
pdf.set_text_color(33, 97, 140)
pdf.cell(0, 10, "1. Attrition by Department", ln=True)
pdf.set_font("Arial", "", 11)
pdf.set_text_color(0, 0, 0)
for _, row in attrition.iterrows():
    pdf.cell(0, 8, f"  {row['Department']}: {int(row['Attrited'])} employees left", ln=True)
pdf.ln(5)

# Section 2 - Salary
pdf.set_font("Arial", "B", 14)
pdf.set_text_color(33, 97, 140)
pdf.cell(0, 10, "2. Average Salary by Department", ln=True)
pdf.set_font("Arial", "", 11)
pdf.set_text_color(0, 0, 0)
for _, row in salary.iterrows():
    pdf.cell(0, 8, f"  {row['Department']}: Rs {int(row['Avg_Salary']):,}/month", ln=True)
pdf.ln(5)

# Section 3 - Overtime
pdf.set_font("Arial", "B", 14)
pdf.set_text_color(33, 97, 140)
pdf.cell(0, 10, "3. Overtime Distribution", ln=True)
pdf.set_font("Arial", "", 11)
pdf.set_text_color(0, 0, 0)
for _, row in overtime.iterrows():
    pdf.cell(0, 8, f"  Overtime {row['OverTime']}: {row['Percentage']}%", ln=True)
pdf.ln(5)

# Key Insights
pdf.set_font("Arial", "B", 14)
pdf.set_text_color(33, 97, 140)
pdf.cell(0, 10, "4. Key Insights", ln=True)
pdf.set_font("Arial", "", 11)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 8, "  * HR department has highest attrition", ln=True)
pdf.cell(0, 8, "  * R&D has highest average salary", ln=True)
pdf.cell(0, 8, "  * Overtime employees show 22.1% attrition vs 16.4%", ln=True)
pdf.cell(0, 8, "  * Salary is #1 predictor of attrition (ML Model)", ln=True)

# Save
pdf.output(r"C:\Users\dell\OneDrive\Documents\Raw_Data\HR_Analytics_Report.pdf")
print("PDF Report generated successfully!")
print("Location: Check your Raw_Data folder!")