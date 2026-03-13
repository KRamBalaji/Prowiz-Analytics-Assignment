# Prowiz-Analytics-Assignment (Python Technical Assessment)

A comprehensive collection of technical tasks demonstrating proficiency in Python automation, web scraping, backend development, data analysis, and SQL.


## Task Breakdown

This repository contains six distinct modules:

1. **API Integration**: Automated data fetching from JSONPlaceholder using `requests` with custom filtering and title analysis.
2. **Web Scraping**: A dual-approach HTML parser using both `BeautifulSoup` and a custom-built **recursive traversal algorithm** (no external libraries).
3. **FastAPI Backend**: A lightweight REST API featuring endpoints for mathematical operations and string manipulation with automatic Swagger documentation.
4. **Retail Data Analysis**: Large-scale analysis of 60,000+ sales records. Includes data cleaning for currency/dates and profit visualization using `Seaborn`.
5. **SQL Student Analytics**: Database schema design and advanced query logic using `DENSE_RANK()` and `OFFSET` to identify class toppers.
6. **Project Documentation**: Proper GitHub repository structure with README.md for documentation and `requirements.txt` for depencency management.


## Tech Stack

- **Language:** Python 3.12+
- **Data:** Pandas, Matplotlib, Seaborn
- **Web:** FastAPI, Uvicorn, BeautifulSoup4, Requests
- **Database:** SQL (MySQL/PostgreSQL compatible)


## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

## 🖥️ Usage
**Running the API**
To start the FastAPI server for Task 3:
```
uvicorn task3_fastapi:app --reload
```

## How to Test the API

Once the FastAPI server is running (`uvicorn task3_fastapi:app --reload`), you can test the endpoints using the following methods:

### 1. Interactive API Documentation (Swagger UI)
The easiest way to test is via the built-in interactive dashboard:
* **URL:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Action:** Click on an endpoint, select **"Try it out"**, enter your parameters, and click **"Execute"**.

### 2. Manual URL Testing
You can also test the endpoints directly in your browser:

| Feature | Example URL | Expected Output |
| :--- | :--- | :--- |
| **Sum Function** | `http://127.0.0.1:8000/sum?num1=10&num2=25` | `{"sum": 35.0}` |
| **Uppercase** | `http://127.0.0.1:8000/uppercase?text=hello` | `{"uppercase": "HELLO"}` |

### 3. Error Handling & Validation
The API includes built-in data validation. If you provide an invalid data type (e.g., a string instead of a number), the API will return a **422 Unprocessable Entity** error.

**Example Error Test:**
- **URL:** `http://127.0.0.1:8000/sum?num1=apple&num2=10`
- **Response:**
  ```json
  {
    "detail": [
      {
        "loc": ["query", "num1"],
        "msg": "value is not a valid float",
        "type": "type_error.float"
      }
    ]
  }

## 📊 Data Analysis Task: Global Electronics Retailer

This module focuses on processing and analyzing a large-scale retail dataset (60,000+ rows) to extract actionable business insights.

### 1. The Dataset
- **Source:** Maven Analytics Global Electronics Retailer dataset.
- **Scope:** Includes tables for `Sales`, `Products`, `Customers`, and `Stores`.
- **Key Columns:** Order Date, Delivery Date, Unit Price, Unit Cost, and Quantity.

### 2. Data Cleaning & Preprocessing
To ensure accuracy, the following cleaning steps were implemented using **Pandas**:
- **Currency Conversion:** Stripped symbols ($) and commas from `Unit Price` and `Unit Cost` to convert them from strings to numeric floats.
- **Datetime Parsing:** Converted date columns into Python `datetime` objects to allow for time-series calculations.
- **Handling Errors:** Addressed data entry issues where delivery dates preceded order dates.

### 3. Key Business Metrics (KPIs)
The analysis provides the following metrics:
- **Total Profit:** Calculated as `(Unit Price - Unit Cost) * Quantity`.
- **Shipping Efficiency:** Calculated the average number of days between the order date and the delivery date.
- **Brand Performance:** Aggregated total profit by Brand to identify top-performing manufacturers.

### 4. Visualizations
Using **Matplotlib** and **Seaborn**, the project generates:
- **Profit by Brand:** A bar chart showing which brands drive the most revenue.
- **Sales Trends:** A line graph tracking order volume over time.
