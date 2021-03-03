### Capstone: Market Basket Analysis
Anel Akiyanova

Capstone Project at The General Assembly

March, 2021

---

#### Table of Contents

- Problem Statement
- Executive Summary
- Background Research
- Data Cleaning and Organizing
- Exploratory Data Analysis
- Model Details
- Key Findings and Recommendations
    - Promotions and Cross-selling
    - Store Layout
- Streamlit App    
- File Directory
- Data Dictionary
- Citations

#### Problem Statement

Perform Market Basket Analysis on Instacart data and identify products that are frequently purchased together. Provide recommendations based on the results of the analysis. 

#### Executive Summary

In this work, I analyzed Instacart 2017 data employing FP-Growth algorithm to identify relationships between items in customer orders. Instacart is an online grocery delivery service from retailers including Costco, Target, Wegmans, and Aldi. Market Basket Analysis is used extensively in retail for product placement, store shelf arrangement, running cross - promotions, and customer retention. While exploring the data I looked at metrics such as busiest and slowest days of week, hours of day, top selling products and aisles, customer reorder cycle, and number of products per order. For modeling purposes, association rule mining was conducted on 5%, 30%, 50%. Due to the size of the order data, it made sense to test the algorithm on a portion of the data and model on a larger size after the concept has been proven. Support level of 1000 transactions and a confidence level of 10% was used in this work. Results of the analysis revealed that bananas and bag of organic bananas are top selling products and most common antecedent. Based on the outcome, I formulated suggested store layout and recommended running cross-sales, cross-promotions on items frequently purchased together. 

#### Background Research

Instacart is an online grocery delivery service from stores such as Mariano’s, Jewel-Osco, Target, Costco, and many more. The company’s business model is based on connecting four sides of a trade: Customers, Product Advertisers, Shoppers, and Retailers. Instacart Revenue comes from delivery fees, often annual memberships, partnerships from companies like Procter & Gamble (30% of all purchases made on the Instacart platform comes from advertisement), and some stores are willing to pay if the delivery service can increase store visits. It is known for its easy-to-use UI, where users have an option to choose the delivery window. Please refer to EDA folder/EDA.ipynb for details on order placement details, including peak and slow hours. 

90% of Instacart’s customers are returning customers, while express customers spend on average USD500 a month. The company allocates substantial resources to estimate customer demand, including building probabilistic models on potential customer demand given 100% supply availability. Weather is an important factor in demand estimation for the company as more customers tend to order groceries online if it is cold, snowing, or raining and the opposite if the weather is warm and sunny. Another important piece that Instacart forecasts is order fulfillment time - the company uses in-house route algorithm, rather than using Google Maps and employs gradient boosting decision trees model as it encounters a lot of variation and this model is prone to overfitting. 

In 4Q2020, Instacart raised USD200 million doubling the company valuation since the beginning of 2020 increasing to USD17.7 billion. The company benefited from surged demand in online grocery deliveries as a result of coronavirus pandemic. In the 1H2020, Instacart increased number of shoppers from under 100,000 to 400,000 and expected company Revenue to hit USD35 billion. 

#### Data Cleaning and Organizing

This work is based on Instacart 2017 data sourced from kaggle.com (https://www.kaggle.com/c/instacart-market-basket-analysis). The data consisted of 6 datasets: aisles, departments, order_products__prior, order_products__train, orders, products. Reading in the data, I quickly realized that the data, specifically, order data requires extensive memory use as it contains 3.4 million unique orders and 34 million rows of combined prior and train orders. Due to the size of the data, I decided to read in only 5% of the customer order data to preserve memory use and accelerate calculations. During the data cleaning process, rows with missing values were dropped, product names were converted to lowercase, and commas taken out of the product names. Taking out commas in the product name column allows us to correctly identify separate products from one another (please see cleaning folder for more details).

For a full picture of the data, I decided to merge datasets in this order and saved resulting dataframes into clean .csv files:

- merged products and order_products__train
- merged products and order_products__prior
- concatenated resulting prior and train orders
- filtered orders to separate test orders
- added quantity column representing number of products purchased to orders dataframes 
- merged aisles, department, and orders dataframes

#### Exploratory Data Analysis

To understand the data, I first wanted to look at what days were busiest and slowest for the online grocery delivery service. Sunday is by far the busiest day with ~21% of all orders placed on this day, while Thursday is the slowest day, representing approximately 12% of all orders. Most orders were placed between 11am and 3pm. Looking at orders split by transaction time on the busiest day, it seems that orders peak at 2pm and 4pm. Comparing top selling aisles on busiest and slowest days, they are mostly similar outside of refrigerated products bought on Thursdays. Based on the research, customers tend to purchase ice cream in the evening and bread in the daytime. 

The analysis revealed that produce is the most purchased and reordered item category. Among fresh vegetables and fruits, bananas, bag of organic bananas, organic strawberries, organic hass avocado, organic baby spinach represent top five selling products. Most customers reorder products in 7 and 30 days implying that orders for this grocery delivery are cyclical. Over 60% of all orders consist of one item and over 80% of all orders contain two items. Cookies cakes, granola bars, and pancake mix were among the last products to be added to cart (please see EDA for more details).

#### Model Details

After researching different algorithms employed in Market Basket Analysis, including Apriori and Eclat, I decided to move forward with FP-Growth (Frequent Pattern) Algorithm. It is a significantly more efficient algorithm compared to Apriori as the dataset does not need to be scanned over and over again and no candidate generation is required. It scans the dataset and counts frequencies of each item in a dataset, sorting them in descending order and leaving items that are at or above a state support level. The algorithm then loops through the remaining itemsets to build FP-tree of nodes starting from the root - the most frequent occurring item - then the next until it reaches the least represented item in a dataset. When items are not part of the branch, a new branch will be created. The algorithm employs a recursive divide-and-conquer approach to identify frequent itemsets traversing the FP-tree. 

Having done these two steps of data sorting, the algorithm scans for itemsets with support level at least the specified level (e.g. 1000). The FP-trees are built in a way that the root of a tree is conditional upon an item and recursively counts the frequency of the item spotted in an itemset. It works based on a notion that If an item occurs frequently, then a subset(s) of that item should also occur frequently. 

I modeled on 5% of the data in jupyter lab, used AWS Sagemaker for modeling on 30% and 50% of the data (please see model folder for details). Support level of 1000 transactions and a confidence level of 10% was chosen for this analysis. High support indicates that the product has high presence in the dataset. High confidence implies that the results have high precision whenever the results appear.

**Visual Representation of the FP-Growth Algorithm**

<img src=assets/FP_tree.jpg style="width:800px;height:450px"/>

#### Key Findings and Recommendations

**Promotions and Cross-selling**

I noted that ‘bananas’ and ‘organic bananas’ are the most frequently purchased items and represent 82% of all antecedents to products that are usually priced higher (please see results folder for more details). Based on the Frequent Item Analysis performed in this work, I would recommend cross-selling and running cross - promotions on items that are frequently purchased together. A bunch of organic bananas is priced between USD1.50 - USD2.50 depending on the retailer (quote source: instacart.com), while some of the consequent items are priced at:

- Bag of clementines USD6.99
- 100% whole-wheat bread USD3.09 - USD6.30
- Red vine tomatoes 4ct USD4.09
- Hass avocados USD3.29 - USD6.79
- seedless grapes, 1lb USD4.89

I would consider offering discounts on bananas, organic bananas to engage customers to start shopping. As customer starts a shopping cart, they likely would be interested in exploring other products even if these products are priced higher. The dataset is from an online grocery delivery service and the business has an opportunity to offer online recommendations suggesting product(s) that were often purchased together by other customers in the past. Compared to the Recommendation algorithm using collaborative filtering, association rules does not capture individual preferences and rather looks for relationships between items within each distinct transaction. It provides avenues to making product suggestions based on customer searches and, if executed diligently, improves customers experience and an increase in sales for retailers. 

**Example of cross-selling**

<img src=assets/itemset.JPG style="width:400px;height:300px"/>

**Store Layout example**

I created Tableau dashboards to illustrate relationships between store aisles and store departments. Details of the two dashboards can be found at this link (https://tabsoft.co/3b0xoCq). Based on the FP-Growth Algorithm and Tableau dashboard results,, I recommend the following store layout to maximize customer shopping experience. Please note that layout excludes certain departments as they did not prove to  indicate strong association rules patterns. It is a simplified illustration of the patterns identified in this research. 


<img src=assets/scheme.jpg style="width:800px;height:380px"/>

#### Streamlit App

Based on association rule mining, I built a streamlit app that produces items frequently purchased together when user chooses a product from the drop-down menu. I have also included an interactive dashboard allowing users to explore the data in the app (please see streamlit folder for details).

#### File Directory

- README.MD

- sources.md: list of sources used in this work

- assets: images referenced in this work  

- results/
    - rules.csv: Association rule mining results modeling on 5% of the data
    - rules_30_percent.csv: Association rule mining results modeling on 30% of the data
    - rules_50_percent.csv: Association rule mining results modeling on 50% of the data

- cleaning/
    - reading_cleaning_data.ipynb: data reading, cleaning and organizing dataframes
    - orders_split_by_hour.ipynb: filtering and organizing morning, daytime, and evening orders

- EDA/
    - EDA.ipynb: exploratory data analysis on the data
    - charts: saved charts from the EDA.ipynb
    
- model/
    - fp_model_5_percent_data.ipynb: FP-Growth algorithm model on 5% percent of the data
    - fp_model_30_percent_data.ipynb: FP-Growth algorithm model on 30% percent of the data (downloaded from AWS)
    - fp_model_50_percent_data.ipynb: FP-Growth algorithm model on 50% percent of the data (downloaded from AWS)

- streamlit/
    - app_preprocessing.ipynb: prepare results file for feeding into the streamlit app
    - stramlit_app.py: streamlit app, predicting frequent itemsets, interactive dashboard 

#### Data Dictionary

aisles.csv 

| Column name | Description |           
|-------------|-------------|
| aisle_id | Store Aisle ID |
| aisle | Store Aisle Name |

departments.csv 


| Column name | Description |
|-------------|-------------|
| department_id | Store Department ID |
| department | Store Department Name |

order_products__.csv 

| Column name | Description |
|-------------|-------------|
| order_id | Order ID |
| product_id | Product ID |
| add_to_cart_order | Order in which product was added to cart |
| reordered | 1 = reordered, 0 = not reordered |

orders.csv

| Column name | Description |
|-------------|-------------|
| order_id | Order ID |
| user_id | User ID |
| eval_set | related to test, train, prior orders |
| order_number | Order number |
| order_dow | Day of week of the order |
| order_hour_of_day | Hour of day when order was placed |
| days_since_prior_order | Number of days since prior order |

products.csv

| Column name | Description |
|-------------|-------------|
| product_id | Product ID |
| product_name | Product Name |
| aisle_id | Store Aisle ID |
| department_id | Store Department ID |

See the link for full data details (https://www.kaggle.com/c/instacart-market-basket-analysis/data). 

#### Citations
See sources.md