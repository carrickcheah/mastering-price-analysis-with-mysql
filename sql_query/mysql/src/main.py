# These SQL queries cover a wide range of analyses, including moving averages,
# volume spikes, price differences, and other key indicators for the dataset.


# -- 1. Retrieve the first 100 rows of the dataset
# SELECT * FROM bitcoin_data LIMIT 100;

# -- 2. Calculate the average closing price for the entire dataset
# SELECT AVG(Close) AS avg_closing_price FROM bitcoin_data;

# -- 3. Retrieve all records where the closing price was above $50,000
# SELECT * FROM bitcoin_data WHERE Close > 50000;

# -- 4. Find the maximum and minimum prices in the dataset
# SELECT MAX(High) AS max_price, MIN(Low) AS min_price FROM bitcoin_data;

# -- 5. Count the number of trading days in the dataset
# SELECT COUNT(Date) AS total_trading_days FROM bitcoin_data;

# -- 6. Calculate the 7-day moving average of the closing price
# SELECT Date, Close,
#        AVG(Close) OVER (ORDER BY Date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_average_7d
# FROM bitcoin_data;

# -- 7. Identify the top 5 days with the highest trading volume
# SELECT Date, Volume
# FROM bitcoin_data
# ORDER BY Volume DESC
# LIMIT 5;

# -- 8. Calculate the daily percentage change in the closing price
# SELECT Date, Close,
#        LAG(Close) OVER (ORDER BY Date) AS prev_close,
#        ((Close - LAG(Close) OVER (ORDER BY Date)) / LAG(Close) OVER (ORDER BY Date)) * 100 AS daily_pct_change
# FROM bitcoin_data;

# -- 9. Retrieve records where the closing price was higher than the 30-day moving average
# WITH moving_avg AS (
#     SELECT Date, Close,
#            AVG(Close) OVER (ORDER BY Date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS moving_average_30d
#     FROM bitcoin_data
# )
# SELECT * FROM moving_avg WHERE Close > moving_average_30d;

# -- 10. Find the longest streak of consecutive days with rising closing prices
# SELECT Date, Close,
#        SUM(CASE WHEN Close > LAG(Close) OVER (ORDER BY Date) THEN 1 ELSE 0 END) OVER (ORDER BY Date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS rising_streak
# FROM bitcoin_data;

# -- 11. Calculate the highest daily price difference (high - low)
# SELECT Date, (High - Low) AS daily_price_diff
# FROM bitcoin_data
# ORDER BY daily_price_diff DESC
# LIMIT 1;

# -- 12. Retrieve all records where trading volume was greater than 1.5 times the 7-day average volume
# WITH vol_avg AS (
#     SELECT Date, Volume,
#            AVG(Volume) OVER (ORDER BY Date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS vol_average_7d
#     FROM bitcoin_data
# )
# SELECT * FROM vol_avg WHERE Volume > 1.5 * vol_average_7d;

# -- 13. Find the days where the closing price was below the 5-day moving average
# WITH moving_avg AS (
#     SELECT Date, Close,
#            AVG(Close) OVER (ORDER BY Date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS moving_average_5d
#     FROM bitcoin_data
# )
# SELECT * FROM moving_avg WHERE Close < moving_average_5d;

# -- 14. Calculate the total trading volume for each month
# SELECT strftime('%Y-%m', Date) AS month, SUM(Volume) AS total_volume
# FROM bitcoin_data
# GROUP BY month;

# -- 15. Retrieve the highest closing price for each month
# SELECT strftime('%Y-%m', Date) AS month, MAX(Close) AS max_closing_price
# FROM bitcoin_data
# GROUP BY month;

# -- 16. Identify days with both opening and closing prices above $60,000
# SELECT * FROM bitcoin_data WHERE Open > 60000 AND Close > 60000;

# -- 17. Calculate the average trading volume for each day of the week
# SELECT strftime('%w', Date) AS weekday, AVG(Volume) AS avg_volume
# FROM bitcoin_data
# GROUP BY weekday;

# -- 18. Find the day with the lowest trading volume
# SELECT Date, Volume
# FROM bitcoin_data
# ORDER BY Volume ASC
# LIMIT 1;

# -- 19. Retrieve all records where the high price exceeded $70,000
# SELECT * FROM bitcoin_data WHERE High > 70000;

# -- 20. Calculate the cumulative trading volume over time
# SELECT Date, Volume,
#        SUM(Volume) OVER (ORDER BY Date) AS cumulative_volume
# FROM bitcoin_data;
