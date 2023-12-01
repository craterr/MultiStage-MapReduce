# MultiStage-MapReduce : E-commerce Data Analysis with Hadoop MapReduce
Multi-stage Hadoop MapReduce job to join, filter, and aggregate the data and give the desired output

# Problem Statement:

For a leading e-commerce platform,your team is tasked with analyzing a massive dataset in the form of a text file. 
This dataset contains two tables, one after the other, and contains crucial information about customer orders and product reviews.


## Table 1: Customer Orders
Each line in this table represents a customer order.
Fields: Order ID, Customer ID, Product ID, Quantity, Price per Unit.


## Table 2: Product Reviews
Each line in this table represents a product review submitted by customers.
Fields: Review ID, Product ID, Customer ID, Rating (1-5 stars), Review Text.


# Objective:

To aim valuable insights from this dataset. We want to understand the relationship between product reviews and the number of items sold for each product. 

We plan to use a multi-stage Hadoop MapReduce job to **join, filter, and aggregate** the data to 
leverage Hadoop MapReduce to perform a join operation between customer order data and product review data,
filter out low-rated reviews (ratings less than 3), and aggregate the results to identify products with the most negative reviews and the quantity of those products sold.

## Example:

**Input Text File (`input.txt`):**
The file is a text file with Tab-Separated Values (TSV).
Column 1 represents the type of record, i.e., whether it belongs to the Customer Orders Table (“order”) or the Product Reviews Table (“review”).

```tsv
order  1  C101  P001  2  20.00
order  2  C102  P002  3  25.00
order  3  C103  P001  1  20.00
order  4  C104  P003  2  30.00
review  101  P001  C101  4  "Great product, very satisfied."
review  102  P002  C102  2  "Not happy with the quality."
review  103  P003  C104  2  "Average product, could be better."
review  104  P001  C103  1  "Terrible, wouldn't recommend."
```


**Expected Output (`output.txt`):**

```tsv
# Products with Negative Reviews and Quantity Sold - DO NOT PRINT
# Product ID,  Quantity Sold - DO NOT PRINT
P002  3
P001  1
P003  2
```

**Explanation:**

In the expected output, we have identified products with negative reviews (ratings less than 3) and calculated the quantity of those products sold. In this example, “P002” had the lowest product rating (2), and it was sold in a quantity of 3. “P001” also had negative reviews (with one rating of 1 and one of 4) and was sold in a quantity of 3. “P003” had a rating of 2 (considered average) and was sold in a quantity of 2.

This output is the result of the Hadoop MapReduce job, which involved joining the customer order and product review data, filtering out low-rated reviews, and aggregating the quantity sold for each product with negative reviews.


#### For each (Product ID, Customer ID) pair, there exists only one unique quantity in the orders table, and at most one rating in the reviews table.



## Mapper 1 [`mapper1.py`](mapper1.py):
- Input: Reads each line from the input file.
- Output: Emits key-value pairs in the format of ProductID,CustomerID,TableType as the key and Quantity as the value for orders, and ProductID,CustomerID,TableType as the key and Rating as the value for reviews.

## Mapper 2 [`mapper2.py`](mapper2.py):
- Input: Takes the output of Mapper 1.
- Output: Emits key-value pairs with the ProductID as the key and Quantity as the value for orders.

## Mapper 3 [`mapper3.py`](mapper3.py):
- Input: Takes the output of Mapper 2.
- Output: Emits key-value pairs with the ProductID,CustomerID as the key and Rating as the value for reviews.

## Reducer 1 [`reducer1.py`](reducer1.py):
- Input: Takes the output of Mapper 1.
- Output: Filters out low-rated reviews (ratings less than 3) and prints the product, table type, and the corresponding rating or quantity.

## Reducer 2 [`reducer2.py`](reducer2.py):
- Input: Takes the output of Mapper 3.
- Output: Prints the product, rating, and the quantity of the previous product if it's a review.

## Reducer 3 [`reducer3.py`](reducer3.py):
- Input: Takes the output of Reducer 2.
- Output: Aggregates the results by summing up the quantities for each product.

## Workflow Explanation:

- Mapper 1: Extracts relevant information from each line and categorizes it based on whether it belongs to the order or review table.
- Mapper 2: Extracts quantities from orders.
- Mapper 3: Extracts ratings from reviews.
- Reducer 1: Filters out low-rated reviews and prints relevant information.
- Reducer 2: Combines ratings with previous values and prints.
- Reducer 3: Aggregates the results by summing up the quantities for each product.








# Usage

## **1. Create HDFS directory**

```bash
hdfs dfs -mkdir /cust_prod
```
## **2. Upload data to HDFS**

```bash
hdfs dfs -put dataset_sample.txt /cust_prod
```
## **3. Execute Hadoop MapReduce script**

```bash
./script.sh
```

### Make the required changes in the script file [`script.sh`](script.sh)

- Changing the hdfs input and output path directory
- ![image](https://github.com/craterr/MultiStage-MapReduce/assets/106965125/ea40fe17-5692-444b-8a4f-c69751a78d88)
  
## 4. Get the output contents 

```bash
hdfs dfs -cat /task2/output/part-00000
```

