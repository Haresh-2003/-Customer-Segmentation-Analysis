# Sales Data Analysis & Customer Segmentation

## Project Overview
This project focuses on analyzing sales data to extract meaningful insights, track performance trends, and support data-driven decision-making. It includes data cleaning, exploratory data analysis (EDA), visualization, and customer segmentation using machine learning techniques.

This project is developed as part of an internship at SVCode Tech Company.

## Features
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Sales Performance Analysis
- Revenue Trends & Forecasting
- Customer Segmentation using K-Means Clustering
- Data Visualization using Matplotlib and Seaborn
- Principal Component Analysis (PCA) for Dimensionality Reduction

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sales-data-analysis.git
   cd sales-data-analysis
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place the sales dataset (`Online Retail.xlsx`) in the `data/` directory.
2. Run the main analysis script:
   ```bash
   python customer_segmentation.py
   ```
3. View the generated reports and visualizations in the `output/` directory.

## Data Sources
The dataset should include columns such as:
- `InvoiceNo`: Invoice number of the transaction.
- `StockCode`: Unique code for each product.
- `Description`: Product description.
- `Quantity`: Number of units sold.
- `InvoiceDate`: Date of the transaction.
- `UnitPrice`: Price per unit.
- `CustomerID`: Unique ID for each customer.
- `Country`: Country of the customer.

## Expected Outputs
- Sales trends over time (daily, monthly, yearly)
- Top-performing products and regions
- Customer purchase behavior insights
- Forecasted sales for upcoming periods
- Customer segmentation using K-Means clustering
- PCA visualization of customer segments

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## Contact
For any inquiries, please contact [HARESH] at [hareshp.s1066@gmail.com].
