-- ============================================
-- HR Analytics Project — SQL Queries
-- Database: hr_database.db (SQLite)
-- Table: hr_data
-- Total Rows: 1,00,000
-- ============================================


-- ─────────────────────────────────────────────
-- QUERY 1: Attrition by Department
-- Insight: HR department mein sabse zyada attrition (2,380)
-- ─────────────────────────────────────────────
SELECT 
    Department, 
    COUNT(*) as Attrited_Employees
FROM hr_data
WHERE Attrition = 'Yes'
GROUP BY Department
ORDER BY Attrited_Employees DESC;


-- ─────────────────────────────────────────────
-- QUERY 2: Average Salary by Department
-- Insight: R&D sabse zyada (Rs.1,04,051), HR sabse kam (Rs.69,163)
-- ─────────────────────────────────────────────
SELECT 
    Department, 
    ROUND(AVG(MonthlySalary), 0) as Avg_Salary
FROM hr_data
GROUP BY Department
ORDER BY Avg_Salary DESC;


-- ─────────────────────────────────────────────
-- QUERY 3: Age Group wise Attrition
-- Insight: 30-40 age group mein sabse zyada attrition (27.1%)
-- ─────────────────────────────────────────────
SELECT 
    CASE 
        WHEN Age < 30 THEN 'Under 30'
        WHEN Age BETWEEN 30 AND 40 THEN '30-40'
        WHEN Age BETWEEN 41 AND 50 THEN '41-50'
        ELSE 'Above 50'
    END as Age_Group,
    COUNT(*) as Attrited,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) as Percentage
FROM hr_data
WHERE Attrition = 'Yes'
GROUP BY Age_Group
ORDER BY Attrited DESC;


-- ─────────────────────────────────────────────
-- QUERY 4: Performance Rating by Department
-- Insight: Sabhi departments almost same (3.43 - 3.46)
-- ─────────────────────────────────────────────
SELECT 
    Department,
    ROUND(AVG(PerformanceRating), 2) as Avg_Performance
FROM hr_data
GROUP BY Department
ORDER BY Avg_Performance DESC;


-- ─────────────────────────────────────────────
-- QUERY 5: Gender Diversity by Department
-- Insight: Male ~55%, Female ~40%, Non-Binary ~5% — consistent
-- ─────────────────────────────────────────────
SELECT 
    Department, 
    Gender,
    COUNT(*) as Count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(PARTITION BY Department), 1) as Percentage
FROM hr_data
GROUP BY Department, Gender
ORDER BY Department, Percentage DESC;


-- ─────────────────────────────────────────────
-- QUERY 6: Overtime vs Attrition Rate
-- Insight: Overtime = 22.1% attrition, No Overtime = 16.4%
-- ─────────────────────────────────────────────
SELECT 
    OverTime,
    COUNT(*) as Total,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrited,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as Attrition_Rate
FROM hr_data
GROUP BY OverTime;


-- ─────────────────────────────────────────────
-- BONUS: Total Employees Count
-- ─────────────────────────────────────────────
SELECT COUNT(*) as Total_Employees FROM hr_data;


-- ─────────────────────────────────────────────
-- BONUS: Overall Attrition Rate
-- ─────────────────────────────────────────────
SELECT 
    COUNT(*) as Total,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) as Attrited,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as Attrition_Rate
FROM hr_data;
