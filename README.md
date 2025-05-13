# Customer Segmentation Analysis

## Overview
This project analyzes customer data from a shopping mall to identify distinct customer segments using clustering techniques. The analysis helps understand customer behavior patterns and enables targeted marketing strategies.

## Dataset
The dataset contains information about 200 customers, including:
- Customer ID
- Gender
- Age
- Annual Income (in thousands of dollars)
- Spending Score (1-100)

## Key Findings

### 1. Customer Demographics
- **Age Distribution**: 
  - Average age: 38.85 years
  - Range: 18-70 years
  - Most customers are in their 30s and 40s

- **Gender Distribution**:
  - Female customers: 56%
  - Male customers: 44%

### 2. Income and Spending Patterns
- **Annual Income**:
  - Average: $60,560
  - Range: $15,000 - $137,000
  - Median: $61,500

- **Spending Score**:
  - Average: 50.20
  - Range: 1-99
  - Median: 50.00

### 3. Customer Segments
The analysis identified 5 distinct customer segments:

1. **High-Value Customers** (Cluster 1)
   - High income ($86,540)
   - High spending score (82.13)
   - Average age: 32.69
   - Marketing Strategy: Premium products, loyalty programs

2. **Moderate Spenders** (Cluster 0)
   - Moderate income ($55,300)
   - Moderate spending score (49.52)
   - Average age: 42.72
   - Marketing Strategy: Balanced product mix, regular promotions

3. **Young Spenders** (Cluster 2)
   - Lower income ($25,730)
   - High spending score (79.36)
   - Average age: 25.27
   - Marketing Strategy: Trendy products, social media campaigns

4. **High-Income Conservative Spenders** (Cluster 3)
   - High income ($88,200)
   - Low spending score (17.11)
   - Average age: 41.11
   - Marketing Strategy: Quality-focused products, exclusive deals

5. **Low-Value Customers** (Cluster 4)
   - Lower income ($26,300)
   - Low spending score (20.91)
   - Average age: 45.22
   - Marketing Strategy: Budget-friendly options, value deals

### 4. Statistical Insights
- Strong correlation between income and spending score for high-value customers
- Gender differences in spending patterns are statistically significant
- Age shows moderate correlation with spending behavior

## Visualizations
The project includes several visualizations to better understand the data:

1. **Basic Analysis** (`visualizations/detailed_analysis.png`)
   - Age distribution by gender
   - Income distribution by gender
   - Spending score distribution by gender
   - Correlation heatmap

2. **Interactive Analysis** (`visualizations/interactive_analysis.html`)
   - Interactive histograms for age, income, and spending score
   - Scatter plot of income vs. spending score
   - Zoom and hover capabilities for detailed exploration

3. **3D Segmentation** (`visualizations/3d_segmentation.html`)
   - 3D visualization of customer segments
   - Interactive rotation and zoom
   - Color-coded by gender

4. **Cluster Analysis** (`visualizations/customer_segmentation.png`)
   - 2D visualization of customer segments
   - Cluster centers marked
   - Clear separation between different customer groups

## Technical Details

### Methodology
1. **Data Preprocessing**
   - Standardization of numerical features
   - Handling of categorical variables

2. **Clustering**
   - K-means algorithm
   - Optimal number of clusters determined using the elbow method
   - Feature selection: Annual Income and Spending Score

3. **Analysis Tools**
   - Python 3.9
   - Key libraries: pandas, numpy, scikit-learn, plotly
   - Statistical testing using scipy

### Project Structure
```
customer_segmentation/
├── data/
│   └── Mall_Customers.csv
├── visualizations/
│   ├── detailed_analysis.png
│   ├── interactive_analysis.html
│   ├── 3d_segmentation.html
│   ├── customer_segmentation.png
│   ├── basic_statistics.csv
│   ├── gender_distribution.csv
│   ├── cluster_centers.csv
│   └── detailed_cluster_analysis.csv
├── customer_segmentation.py
├── requirements.txt
└── README.md
```

## Business Implications

### Marketing Strategies
1. **High-Value Customers**
   - Focus on premium products and services
   - Implement VIP loyalty programs
   - Personalized shopping experiences

2. **Moderate Spenders**
   - Balanced product mix
   - Regular promotions and discounts
   - Focus on value for money

3. **Young Spenders**
   - Trendy and fashionable products
   - Social media marketing
   - Student discounts and promotions

4. **High-Income Conservative Spenders**
   - Quality-focused products
   - Exclusive deals and early access
   - Emphasis on product durability

5. **Low-Value Customers**
   - Budget-friendly options
   - Clearance sales and discounts
   - Basic product offerings

### Recommendations
1. **Targeted Marketing**
   - Develop segment-specific marketing campaigns
   - Customize product offerings for each segment
   - Implement personalized communication strategies

2. **Store Layout**
   - Optimize store layout based on segment preferences
   - Place premium products in high-traffic areas
   - Create dedicated sections for different segments

3. **Customer Service**
   - Train staff to identify and serve different segments
   - Implement segment-specific service protocols
   - Develop customized loyalty programs

## Future Work
1. **Additional Analysis**
   - Seasonal spending patterns
   - Product category preferences
   - Customer lifetime value analysis

2. **Model Improvements**
   - Incorporate more features
   - Try different clustering algorithms
   - Implement real-time segmentation

3. **Business Integration**
   - Develop automated segmentation system
   - Create dashboard for monitoring
   - Implement A/B testing for marketing strategies

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Required packages (see requirements.txt)

### Installation
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the analysis:
```bash
python customer_segmentation.py
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Dataset source: [Mall Customer Segmentation Data](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- Special thanks to the open-source community for the tools and libraries used in this project. 