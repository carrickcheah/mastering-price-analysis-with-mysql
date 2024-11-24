# Predict Bitcoin Price

## Overview

This project demonstrates the effective utilization of SQL for managing and analyzing large-scale Bitcoin trading data. The dataset, comprising daily metrics and calculated indicators over a year, provides a foundation for mastering SQL skills essential for handling big data. Emphasis is placed on extracting meaningful insights, such as daily trading trends and volume analysis, while ensuring efficiency and accuracy in data retrieval. By automating repetitive tasks and correcting historical inconsistencies, SQL serves as a powerful tool for streamlining workflows. This approach underscores the critical role of SQL in empowering businesses to harness the potential of big data for operational excellence.

### **Dataset Columns:**

- **Date**: The date for each record.  
- **Product_Id**: The BTC/USD currency pair identifier.  
- **Timestamp_MS**: Unix timestamp in milliseconds, representing the precise time for each data entry.  
- **Open, High, Low, Close**: Daily price points of Bitcoin, giving a full view of each day's price range.  
- **Volume**: The trading volume in USD for each day, showing the level of market activity.  
- **Vol_Average5**: The 5-day moving average of the trading volume, which smooths short-term volume fluctuations.  
- **Moving_Average5 and Moving_Average30**: The 5-day and 30-day moving averages of the closing price, providing short-term and medium-term trend indicators.  

---

## Purpose of Selecting this Dataset

This dataset was chosen to showcase SQL's power in managing and analyzing large-scale Bitcoin trading data. Its extensive daily metrics over a year provide a platform for mastering SQL's capabilities in handling big data, extracting insights, and streamlining workflows with efficiency and accuracy.

---

## Plan for Working on the Dataset

Utilize SQL to efficiently manage and analyze the large-scale Bitcoin dataset, focusing on data extraction, trend analysis, anomaly detection, and workflow automation to handle big data challenges effectively.

---

## Data Characteristics

The dataset is quantitative, consisting of numerical values such as prices, volume, and moving averages, which are essential for statistical and predictive modeling. The dataset contains 365 rows of daily trading data over one year, with a total file size of 41 KB. This scope provides a comprehensive view of Bitcoin's trading activity, capturing both short-term volatility and seasonal patterns.

---

## Table of Contents

1. [Overview](#overview)  
2. [Purpose of Selecting this Dataset](#purpose-of-selecting-this-dataset)  
3. [Plan for Working on the Dataset](#plan-for-working-on-the-dataset)  
4. [Data Characteristics](#data-characteristics)  
5. [Elaboration of SQL and Results](#elaboration-of-sql-and-results)  
6. [Summary](#summary)  

---

## Elaboration of SQL and Results

### Dataframe of BTC

![Image 1](images/001.jpg)

The dataset is quantitative in nature. It good for detailed time-series forecasting and market trend analysis. It captures both short-term volatility and seasonal patterns.

---

&nbsp;
&nbsp;

![Image 3](images/003.png)
Elaboration SQL:  
The schema organizes data into columns like `Timestamp_MS`, `Open_price`, and `Close_price`, optimized for time-series analysis by making `Timestamp_MS` the primary key.
Explanation Results:  
It detects trends, anomalies, and supports time-specific analysis for informed trading and decision-making strategies.

&nbsp;
&nbsp;

![Image 4](images/004.png)
Elaboration SQL:  
Retrieves records where Open_price > 73000 and Close_price < 90000.  Sorted with Timestamp_MS descending.
Explain Results:  
Identifies days with specific price conditions. It really help spot trading .

&nbsp;
&nbsp;

![Image 5](images/005.png)
Elaboration:  
Calculates the average Close_price over 5, 20, and 30 days from the most recent data.
Results:  
Provides short-term and long-term price trends. Assist in trend analysis for trading strategies.

&nbsp;
&nbsp;

![Image 6](images/006.png)
Elaboration SQL:  
Summary statistics such as total entries, min/max/average prices, and total trading volume.
Explain Results:  
Helps analyse overall market performance and key price.

&nbsp;
&nbsp;

![Image 7](images/007.png)
Elaboration SQL:  
Retrieves the top 5 days with the highest price fluctuations by calculate the difference between High_price and Low_price.
Explain Results:  
Find the most volatile trading days. To help assess market instability and potential opportunities.

&nbsp;
&nbsp;

![Image 8](images/008.png)
Elaboration SQL:  
To get 7-day moving average of Close_price using a window function.
Explain Results:  
Shows smoothed price trends, reduce daily volatility to help identify consistent patterns.

&nbsp;
&nbsp;

![Image 9](images/009.png)
Elaboration SQL:  
Calculates daily percentage changes in closing price and compare each day with the previous day's close.
Explain Results:  
Help in get significant market fluctuations for investment decisions.

&nbsp;
&nbsp;

![Image 10](images/010.png)
Elaboration SQL:  
Calculates the longest consecutive days with rising closing prices using window functions.
Explain Results:  
Identifies the maximum streak of price increases (197 days). Discover trend analysis.

&nbsp;
&nbsp;

![Image 11](images/011.png)
Elaboration SQL:  
Selects records where the closing price exceeds the 30-day moving average, sorted by date.
Explain Results:  
Highlights dates when prices outperformed the 30-day trend. It supports analysis of upward price momentum.

&nbsp;
&nbsp;

![Image 12](images/012.png)
Elaboration SQL:  
Identifies days with trading volume spikes exceeding 1.5 times the 7-day moving average, show about percentage increase.
Explain Results:  
Highlights significant volume surges. Purpose for spotting unusual market activity.

&nbsp;
&nbsp;

![Image 13](images/013.png)
Elaboration SQL:  
Calculates the highest daily profit opportunity based on the difference between high and low prices.
Explain Results:  
Identifies the day with the maximum trading profit potential. It would help strategic decision-making for traders.

&nbsp;
&nbsp;

## Summary

This comprehensive Bitcoin trading dataset, encompassing daily metrics and calculated indicators, underscores the mastery of SQL for efficient data management, enabling the retrieval of insights such as daily trends and trading volumes. By leveraging SQL's capabilities, the analysis enhances anomaly detection, automates repetitive tasks for improved accuracy, and supports strategic decision-making, providing actionable insights into price trends and market behavior over the past year.

&nbsp;
&nbsp;
