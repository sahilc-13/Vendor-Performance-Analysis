# Vendor Performance Analysis using Python and Power BI

## Overview
This project focuses on analyzing vendor performance based on sales data. It involves data ingestion, cleaning, exploratory data analysis (EDA), automation of summary generation, and dashboard development using Power BI. The project concludes with a comprehensive report containing actionable insights.

## Workflow
1. Ingest Data
   Load CSVs into SQLite using Python. Handles large files and logs each step.
2. Clean + Analyze
   Use SQL and Pandas to explore, join, and clean the data.
3. Generate Insights
   Detailed Exploratory Data Analysis (EDA) to identify trends and patterns and Calculate KPIs like margins, sales, stuck inventory, and vendor-level performance.
4. Visualize
   Build a Power BI dashboard that’s easy to read and ready for business users.
5. Report
   Finalized insights compiled in a PDF report

## Business Problem
Effective inventory and sales management is critical in the retail/wholesale industry.  
Companies often face challenges like inefficient pricing, poor inventory turnover, and vendor dependency.  
This project addresses these by:  
- Identifying underperforming brands that need promotional or pricing adjustments  
- Highlighting top vendors driving sales and profitability  
- Assessing the impact of bulk purchasing on unit costs  
- Evaluating inventory turnover to reduce holding costs  
- Comparing profitability models of high vs. low-performing vendors  

## Key Insights
- Certain brands show high profit margins but low sales volumes → need targeted promotions  
- Heavy reliance on a few top vendors introduces supply chain risks → diversification needed  
- Bulk purchases significantly reduce unit costs → bulk buying strategies can improve margins  
- Slow-moving inventory ties up millions in unsold stock → optimize purchase and storage strategy  
- Low-performing vendors often have higher margins but weaker sales → pricing and distribution need improvement  

## Files

| File                               | Purpose                                              |
|------------------------------------|------------------------------------------------------|
| `Ingestion_db.py`                  | Loads CSVs into SQLite with logging and error handling |
| `EDA.ipynb`                        | Cleans and explores data using Pandas and SQL        |
| `Vendor_Performance_Analysis.ipynb`| Analyzes vendor/brand-level performance              |
| `vendor_sales_summary.csv`         | Merged and cleaned (summarized) data for insights    |
| `Workflow.png`                     | Project flow diagram                                 |
| `Dashboard.pbix`                   | Interactive Power BI dashboard                       |

## Deliverables
- Vendor performance summary CSV
- Power BI Dashboard
- Final insights report(Doc)
