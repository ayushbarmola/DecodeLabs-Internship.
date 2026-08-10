# E-Commerce Data Analytics & Exploratory Data Analysis

## 📊 Project Overview

This project performs **Data Cleaning** and **Exploratory Data Analysis
(EDA)** on an e-commerce order dataset.

The objective is to identify patterns, trends, distributions, outliers,
and actionable business insights using Python and Excel.

## 🎯 Objectives

-   Clean and prepare the raw dataset
-   Calculate descriptive statistics: count, mean, median, minimum,
    maximum, and standard deviation
-   Analyze yearly sales trends
-   Compare product performance
-   Analyze payment methods
-   Analyze order-status distribution
-   Evaluate referral sources
-   Detect potential outliers using the IQR method
-   Generate an automated Excel analysis report
-   Summarize key business observations

## 🛠️ Technologies Used

  Technology   Purpose
  ------------ -----------------------------------------
  Python       Data analysis and automation
  Pandas       Data manipulation and analysis
  NumPy        Numerical operations
  OpenPyXL     Excel reporting, formatting, and charts
  Excel        Data storage and reporting
  Git/GitHub   Version control

## 📁 Project Structure

``` text
Data_Analytics/
│
├── DataCleaning/
│   ├── clean_data.py
│   ├── Dataset for Data Analytics.xlsx
│   └── Cleaned_Dataset.xlsx
│
├── Exploratory Data Analysis/
│   ├── EDA.py
│   ├── Cleaned_Dataset.xlsx
│   └── Dataset_Analysis_Report.xlsx
│
└── README.md
```

## 📋 Dataset

The dataset contains e-commerce order information.

### Main Columns

  Column              Description
  ------------------- -----------------------------
  `OrderID`           Unique order identifier
  `Date`              Order date
  `CustomerID`        Unique customer identifier
  `Product`           Product purchased
  `Quantity`          Number of units purchased
  `UnitPrice`         Price per unit
  `ShippingAddress`   Customer shipping address
  `PaymentMethod`     Payment method used
  `OrderStatus`       Current order status
  `TrackingNumber`    Shipment tracking number
  `ItemsInCart`       Number of items in cart
  `CouponCode`        Coupon or discount code
  `ReferralSource`    Customer acquisition source
  `TotalPrice`        Total order value

## 🧹 Data Cleaning

The data-cleaning stage prepares the raw dataset for analysis through
operations such as:

-   Handling missing values
-   Removing duplicate records
-   Correcting data types
-   Standardizing columns
-   Checking invalid values
-   Producing a cleaned dataset

## 🔎 Exploratory Data Analysis

The EDA script performs the following analysis.

### 1. Basic Statistics

For numerical variables:

-   Count
-   Mean
-   Median
-   Minimum
-   Maximum
-   Standard deviation

Variables include:

``` text
Quantity
UnitPrice
ItemsInCart
TotalPrice
```

### 2. Yearly Sales Trend

Calculates:

-   Orders per year
-   Total revenue per year
-   Average order value per year

### 3. Product Analysis

Compares products using:

-   Number of orders
-   Quantity sold
-   Revenue
-   Average order value

### 4. Payment Method Analysis

Analyzes:

-   Number of orders
-   Revenue
-   Average order value

### 5. Order Status Analysis

Analyzes the distribution of statuses such as:

``` text
Delivered
Shipped
Pending
Returned
Cancelled
```

### 6. Referral Source Analysis

Evaluates referral sources based on:

-   Number of orders
-   Revenue
-   Average order value

## 📈 Outlier Detection

Potential outliers are identified using the **Interquartile Range
(IQR)** method.

``` text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

Values outside these limits are flagged as potential outliers.

## 📊 Excel Report

The EDA script generates:

``` text
Dataset_Analysis_Report.xlsx
```

The workbook contains:

  Sheet                 Purpose
  --------------------- ----------------------------------
  `Cleaned Data`        Clean dataset
  `Basic Statistics`    Descriptive statistics
  `Yearly Trend`        Year-wise sales analysis
  `Product Analysis`    Product performance
  `Payment Analysis`    Payment analysis
  `Order Status`        Order-status distribution
  `Referral Analysis`   Referral-source analysis
  `Outlier Summary`     IQR outlier summary
  `Outlier Records`     Individual potential outliers
  `Key Observations`    Automatically generated insights

The report also includes Excel charts for yearly revenue, product
revenue, and order status.

## 💡 Business Questions Answered

The analysis helps answer:

-   What is the average order value?
-   What is the typical order size?
-   Which products generate the most revenue?
-   Which products perform poorly?
-   Which payment method is most popular?
-   Which referral source generates the most orders?
-   How are orders distributed across statuses?
-   Are there unusually high-value orders?
-   How does revenue change over time?
-   Is the order-value distribution skewed?

## ⚙️ Installation

Check Python:

``` bash
python --version
```

Install required libraries:

``` bash
pip install pandas numpy openpyxl
```

## ▶️ How to Run

From the project root:

``` bash
python "DataCleaning/clean_data.py"
```

Then run the EDA script:

``` bash
python "Exploratory Data Analysis/EDA.py"
```

The final report will be created at:

``` text
Exploratory Data Analysis/Dataset_Analysis_Report.xlsx
```

## 🔄 Analysis Workflow

``` text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Cleaned Dataset
     │
     ▼
Exploratory Data Analysis
     │
     ├── Descriptive Statistics
     ├── Trend Analysis
     ├── Product Analysis
     ├── Payment Analysis
     ├── Order Status Analysis
     ├── Referral Analysis
     └── Outlier Detection
     │
     ▼
Key Observations
     │
     ▼
Excel Analysis Report
```

## 🧠 Skills Demonstrated

-   Data Cleaning
-   Exploratory Data Analysis
-   Descriptive Statistics
-   Pandas GroupBy
-   Data Aggregation
-   Trend Analysis
-   Outlier Detection
-   Business Analysis
-   Analytical Thinking
-   Python Automation
-   Excel Reporting
-   Data Visualization

## 🚀 Future Improvements

-   Build an interactive Power BI dashboard
-   Add monthly and quarterly analysis
-   Perform customer segmentation
-   Analyze repeat purchases and retention
-   Calculate profit margins
-   Perform RFM analysis
-   Add correlation analysis
-   Build sales forecasting models
-   Create an interactive Streamlit dashboard

## 👨‍💻 Author

**Ayush Barmola**

MBA -- Business Analytics

**Skills:** Python \| Pandas \| NumPy \| SQL \| Excel \| Data Analysis
\| Data Visualization

## ⭐ Project Purpose

This project is a practical **Data Analytics / Exploratory Data Analysis
portfolio project** demonstrating the process of transforming an
e-commerce dataset into meaningful and actionable business insights.
