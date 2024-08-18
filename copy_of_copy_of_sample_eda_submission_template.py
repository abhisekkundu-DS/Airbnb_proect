# -*- coding: utf-8 -*-
"""Copy of copy_of_sample_eda_submission_template.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K7csJxdQ6xMpex4IvGo2TGOScl7Z-yHV

# **Project Name**    -

##### **Project Type**    - EDA/Regression/Classification/Unsupervised
##### **Contribution**    - Individual
##### **Team Member 1 -**Abhisek Kundu
##### **Team Member 2 -**
##### **Team Member 3 -**
##### **Team Member 4 -**

# **Project Summary -**

Project Summary: Airbnb Data Analysis

**Goals**:
  **Understand Airbnb Ecosystem**: Explore the dataset to gain insights into the Airbnb platform, including pricing trends, property types, and geographic patterns.

   **Enhance Business Decisions:**Leverage data to guide strategic decisions related to security, marketing initiatives, and additional services.
  **Optimize Customer Experience:** Analyze host and guest behavior to enhance user experience on the platform.
  
  **Business Insights:** Provide actionable insights for Airbnb hosts, property investors, and policymakers to optimize rental strategies, improve profitability, and enhance the overall Airbnb ecosystem in New York City.

**Approach:**

**Data Exploration:** bold text
Clean and preprocess the dataset.
Investigate relationships between variables.
Identify outliers and missing values.

**Visualizations:**
Utilize Matplotlib and Seaborn to create at least five different visual representations (e.g., histograms, barplots, boxplots, heatmaps).
Visualize property distribution, pricing patterns, and regional trends.

**Statistical Analysis:**
Perform univariate, bivariate, and multivariate statistical analyses.
Identify correlations and patterns.

**Business Insights:**
Extract actionable insights for business decisions.

Address security concerns, improve host performance, and enhance customer satisfaction.

**Expected Outcomes:**
Clear understanding of Airbnb data.

Insights to drive informed decisions.

Improved platform performance and user satisfaction.

# **GitHub Link -**

Provide your GitHub Link here.https://github.com/abhisekkundu-DS/abhisekkundu-DS/tree/main

# **General Guidelines** : -

1.   Well-structured, formatted, and commented code is required.
2.   Exception Handling, Production Grade Code & Deployment Ready Code will be a plus. Those students will be awarded some additional credits.
     
     The additional credits will have advantages over other students during Star Student selection.
       
             [ Note: - Deployment Ready Code is defined as, the whole .ipynb notebook should be executable in one go
                       without a single error logged. ]

3.   Each and every logic should have proper comments.
4. You may add as many number of charts you want. Make Sure for each and every chart the following format should be answered.
        

```
# Chart visualization code
```
            

*   Why did you pick the specific chart?
*   What is/are the insight(s) found from the chart?
* Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

5. You have to create at least 20 logical & meaningful charts having important insights.


[ Hints : - Do the Vizualization in  a structured way while following "UBM" Rule.

U - Univariate Analysis,

B - Bivariate Analysis (Numerical - Categorical, Numerical - Numerical, Categorical - Categorical)

M - Multivariate Analysis
 ]

# ***Let's Begin !***

## ***1. Know Your Data***

### Import Libraries
"""

# Import Libraries
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""### Dataset Loading"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File path in Google Drive
file_path = "/content/Airbnb NYC 2019 (1).csv"

# Read CSV file into DataFrame
df = pd.read_csv(file_path)

"""### Dataset First View"""

# Dataset First Look
df=pd.read_csv("Airbnb NYC 2019 (1).csv")
df.head()

"""It looks like you've loaded the Airbnb NYC 2019 dataset into a pandas DataFrame and displayed the first five rows. Here's a summary of the columns in your dataset:

- **id**: Unique identifier for the listing.
- **name**: Name of the listing.
- **host_id**: Unique identifier for the host.
- **host_name**: Name of the host.
- **neighbourhood_group**: Larger area groupings within NYC (e.g., Manhattan, Brooklyn).
- **neighbourhood**: Specific neighborhood within the larger group.
- **latitude**: Latitude of the listing.
- **longitude**: Longitude of the listing.
- **room_type**: Type of room (e.g., Private room, Entire home/apt).
- **price**: Price per night in USD.
- **minimum_nights**: Minimum number of nights required to book.
- **number_of_reviews**: Number of reviews the listing has received.
- **last_review**: Date of the last review.
- **reviews_per_month**: Number of reviews per month.
- **calculated_host_listings_count**: Number of listings by the same host.
- **availability_365**: Number of days the listing is available in a year.

### Dataset Rows & Columns count
"""

# Dataset Rows & Columns count
(48895, 16)

"""It seems like you've printed the shape of your dataset twice, which shows that it has:

- **48,895 rows**: Each row represents a unique Airbnb listing.
- **16 columns**: Each column represents a different attribute of the listing, as summarized earlier.

This confirms that your dataset is quite large, with almost 49,000 listings in total. If you need help with any specific analysis or tasks on this dataset, let me know!

### Dataset Information
"""

# Dataset Info
print("Data Information:")
print(df.info())

"""The output provides detailed information about the structure and content of the DataFrame created from your dataset. Here's a step-by-step explanation:

### 1. **Class Type**:
   - The line `<class 'pandas.core.frame.DataFrame'>` indicates that the data is stored in a pandas DataFrame, a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure in Python.

### 2. **Range Index**:
   - `RangeIndex: 48895 entries, 0 to 48894` shows that the DataFrame contains **48,895 rows**, starting from index `0` to `48,894`.

### 3. **Data Columns (Total 16 Columns)**:
   - The output lists all the columns in the DataFrame, their index numbers, names, the number of non-null values in each column, and their data types.

### 4. **Column Details**:
   - **Column Index (`#`)**: The position of the column in the DataFrame (starting from 0).
   - **Column Name (`Column`)**: The name of the column.
   - **Non-Null Count**: The number of non-missing (non-null) values in the column.
   - **Data Type (`Dtype`)**: The type of data stored in the column.

   Here’s what each column represents:

   - **id (Index 0)**: 48,895 non-null values, data type `int64`. This column contains unique identifiers for each listing.
   - **name (Index 1)**: 48,879 non-null values, data type `object`. The name of each listing, with 16 missing values.
   - **host_id (Index 2)**: 48,895 non-null values, data type `int64`. Unique identifiers for each host.
   - **host_name (Index 3)**: 48,874 non-null values, data type `object`. The name of each host, with 21 missing values.
   - **neighbourhood_group (Index 4)**: 48,895 non-null values, data type `object`. The broad neighborhood group within NYC (e.g., Manhattan, Brooklyn).
   - **neighbourhood (Index 5)**: 48,895 non-null values, data type `object`. The specific neighborhood within the group.
   - **latitude (Index 6)**: 48,895 non-null values, data type `float64`. The latitude coordinate of the listing.
   - **longitude (Index 7)**: 48,895 non-null values, data type `float64`. The longitude coordinate of the listing.
   - **room_type (Index 8)**: 48,895 non-null values, data type `object`. The type of room available (e.g., Private room, Entire home/apt).
   - **price (Index 9)**: 48,895 non-null values, data type `int64`. The price per night in USD.
   - **minimum_nights (Index 10)**: 48,895 non-null values, data type `int64`. The minimum number of nights required for booking.
   - **number_of_reviews (Index 11)**: 48,895 non-null values, data type `int64`. The number of reviews the listing has received.
   - **last_review (Index 12)**: 38,843 non-null values, data type `object`. The date of the last review, with 10,052 missing values.
   - **reviews_per_month (Index 13)**: 38,843 non-null values, data type `float64`. The average number of reviews per month, also with 10,052 missing values.
   - **calculated_host_listings_count (Index 14)**: 48,895 non-null values, data type `int64`. The number of listings the host has.
   - **availability_365 (Index 15)**: 48,895 non-null values, data type `int64`. The number of days the listing is available per year.

### 5. **Data Types**:
   - The data types listed (`int64`, `float64`, `object`) tell us how the data in each column is stored:
     - `int64` for integers.
     - `float64` for floating-point numbers (decimals).
     - `object` for strings or mixed types.

### 6. **Memory Usage**:
   - `memory usage: 6.0+ MB` indicates that the DataFrame takes up about 6.0 MB of memory in your system.

### 7. **Summary of Observations**:
   - **Non-Null Counts**: Most columns have complete data, but some columns like `name`, `host_name`, `last_review`, and `reviews_per_month` have missing values that you may need to handle before analysis.
   - **Data Types**: Understanding the data types helps in selecting appropriate operations for each column.

This output is essential for understanding the basic structure of your dataset and identifying any data cleaning or preprocessing steps needed before conducting further analysis.

#### Missing Values/Null Values
"""

# Missing Values/Null Values Count
# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

"""Here's a brief analysis of the missing values in your dataset:

### Overview:
- **Total Columns**: 16
- **Total Rows**: 48,895

### Missing Values Summary:
- **Minor Missing Values**:
  - **name**: 16 missing values (~0.03% of the total rows).
  - **host_name**: 21 missing values (~0.04% of the total rows).
  
- **Significant Missing Values**:
  - **last_review**: 10,052 missing values (~20.6% of the total rows).
  - **reviews_per_month**: 10,052 missing values (~20.6% of the total rows).

### Interpretation:
- **name and host_name**: The missing values here are minimal and unlikely to affect most analyses. Simple imputation (e.g., filling with "Unknown") or dropping these rows would be sufficient.
  
- **last_review and reviews_per_month**: These columns have a substantial number of missing values, likely corresponding to listings that haven't received any reviews. This could indicate that the property is either new or unpopular.

### Potential Actions:
- **For `name` and `host_name`**: Impute with a placeholder value or drop rows if necessary.
- **For `last_review` and `reviews_per_month`**: Consider filling `reviews_per_month` with `0` and `last_review` with a placeholder like `NaT` (Not a Time) or leave as NaN depending on the analysis needs.

"""

# Visualizing the missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

"""### What did you know about your dataset?

Missing values were filled with NaN to maintain data integrity and avoid potential bias in subsequent analysis.That's why it shows 20141 missing values

## ***2. Understanding Your Variables***
"""

# Dataset Columns
print("Columns:")
print(df.columns)

"""The dataset contains the following columns:

- **id**, **name**, **host_id**, **host_name**
- **neighbourhood_group**, **neighbourhood**
- **latitude**, **longitude**
- **room_type**, **price**, **minimum_nights**
- **number_of_reviews**, **last_review**, **reviews_per_month**
- **calculated_host_listings_count**, **availability_365**

These columns cover listing IDs, host details, location, room type, pricing, and review information.
"""

# Dataset Describe
df.describe()

"""### Variables Description

Here's a brief analysis of the dataset's numerical columns:

- **Price**: Ranges from \$0 to \$10,000, with an average price of \$152.72.
- **Minimum Nights**: Varies from 1 to 1,250 nights, with an average of 7.03 nights.
- **Number of Reviews**: Average is 23.27, with a maximum of 629 reviews, indicating a wide range in listing popularity.
- **Availability**: Listings are available on average for 112.78 days a year, with some available year-round and others for just a few days.Answer Here

### Check Unique Values for each variable.
"""

# Check Unique Values for each variable.
df.nunique()

"""## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***

#### Chart - 1
"""

# Chart - 1 visualization code
# Define price ranges
price_ranges = {
    '0-50': df[(df['price'] >= 0) & (df['price'] <= 50)].shape[0],
    '51-100': df[(df['price'] > 50) & (df['price'] <= 100)].shape[0],
    '101-150': df[(df['price'] > 100) & (df['price'] <= 150)].shape[0],
    '151-200': df[(df['price'] > 150) & (df['price'] <= 200)].shape[0],
    '201+': df[df['price'] > 200].shape[0]
}

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(price_ranges.values(), labels=price_ranges.keys(), autopct='%1.1f%%', explode=[0,0.1,0,0,0],colors=['RED', 'yellow', 'green', 'pink', 'blue'], startangle=140 ,shadow=True)
plt.title('Market Share of Different Price Ranges',fontsize=20,color="RED")
plt.axis('equal')
plt.show()

"""##### 1. Why did you pick the specific chart?

The analysis provides insights into the distribution of Airbnb listings across various price ranges. Here's a breakdown of the market share for each price range:

0-50: -- Approximately 13.4% -- Budget Conscious , Affordable Accommodations Travelers

51-100: -- Largest segment 31.5% -- Listings in this range are moderately priced and appeal to a wide range of travelers, including budget-conscious individuals and those willing to pay slightly more for added amenities or convenience.

101-150: -- 20.5%. Typically offer more amenities, comfort, and possibly better locations compared to lower-priced options.

151-200: Accounting for 13.4% of the market, this price range caters to travelers seeking higher-end accommodations with premium features.

200+: Representing 17.1% of the market, this price range encompasses the highest-priced listings available. These accommodations often provide luxury amenities, exclusive locations, or exceptional experiences tailored to discerning travelers willing to pay a premium for top-tier accommodations.

Analysis and Implications:

Price Sensitivity: 51-100 price range, indicating a high level of price sensitivity among Airbnb users. Hosts should consider pricing strategies carefully to remain competitive within this segment.

Market Segmentation: The diverse distribution across various price ranges reflects the segmented nature of the Airbnb market, catering to travelers with varying budgets, preferences, and expectations. Hosts can leverage this segmentation to tailor their offerings and target specific traveler segments effectively.

Demand Dynamics: The distribution of listings across different price ranges provides insights into demand dynamics within the Airbnb market. Understanding which price ranges attract the most significant share of listings can help hosts optimize their pricing strategies to maximize occupancy and revenue.

Competitive Landscape: The analysis sheds light on the competitive landscape within each price range. Hosts operating within specific price segments should assess market trends, competitor offerings, and traveler preferences to position themselves effectively and attract bookings.

Opportunities for Growth: Hosts and investors can identify opportunities for growth and expansion by analyzing market share trends across different price ranges. Exploring underserved or emerging segments of the market can uncover new opportunities for property investments or niche market positioning.

**In conclusion, the analysis of market share across different price ranges provides valuable insights for hosts, investors, and stakeholders in the Airbnb ecosystem. By understanding the distribution of listings and the dynamics within each price segment, stakeholders can make informed decisions to optimize their offerings, attract guests, and drive business growth.**

#### Chart - 2
"""

# Chart - 2 visualization code
plt.figure(figsize=(10, 6))
sns.countplot(x='neighbourhood_group', data=df, palette='Set1')
plt.title('Distribution of Listings by Neighbourhood Group')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Count')
plt.show()

"""##### 1. Why did you pick the specific chart?"""

# Chart - 4 visualization code
plt.figure(figsize=(10, 6))
sns.barplot(x='neighbourhood_group', y='price', hue='room_type', data=df, palette='Set3')
plt.title('Average Price by Neighbourhood Group and Room Type')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Average Price')
plt.show()

"""Analysis of Distribution of listings across neighborhoods by room type

The analysis provides insights into the distribution of listings across neighborhoods by room type:

Manhattan: Manhattan exhibits a higher number of entire homes/apartments compared to private rooms. This could be due to the high demand for complete spaces in this bustling borough. Like Brooklyn, shared rooms are also minimal here, suggesting that they are less popular among hosts and guests.

Brooklyn: This neighborhood has a balanced distribution of private rooms and entire homes/apartments listed on Airbnb. The number of shared rooms is significantly lower, indicating that hosts in Brooklyn prefer to list entire spaces or private rooms.

Queens: In Queens, there are more private rooms than entire homes/apartments. This could be due to the residential nature of this borough, where hosts might prefer to rent out spare rooms. The proportion of shared rooms is even smaller, following the trend observed in the other neighborhoods.

Staten Island: Staten Island has fewer listings overall but follows a similar pattern as Queens with more private rooms followed by entire homes/apartments. The number of shared rooms is very low, indicating that they are not a popular choice in this borough.

Bronx: The Bronx also follows this pattern but has the least number of listings among all neighborhoods. This could be due to various factors such as demand, property availability, or local regulations.

In summary, the distribution of Airbnb listings across these neighborhoods shows that entire homes/apartments and private rooms are the most popular room types, while shared rooms are less common. Each neighborhood has its unique characteristics, which are reflected in the types of listings available. This analysis provides valuable insights for both hosts and guests using Airbnb in New York City.Answer Here.

#### Chart - 6
"""

# Chart - 6 visualization code
plt.figure(figsize=(10, 6))
# sns.histplot(df['number_of_reviews'], bins=20, kde=True, color='skyblue')
sns.scatterplot(x='number_of_reviews', y='price', data=df, alpha=0.5,color="RED")
plt.title('Distribution of Number of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Frequency')
plt.show()

"""Analysis of Price VS Number of Reviews

From the scatter plot, we can make several observations:

Concentration of listings: There is a high concentration of listings with lower prices and a varying number of reviews. This suggests that more affordable listings tend to receive more reviews.

Outliers: There are a few listings with very high prices and a low number of reviews. These could be luxury listings or listings in high-demand locations that are rented less frequently due to their price.

Trend: As the price increases, the number of reviews decreases. This could indicate that guests are less likely to review more expensive listings, or it could suggest that more expensive listings are rented less frequently.

Correlation: There doesn’t appear to be a strong correlation between price and the number of reviews. This suggests that other factors may be more influential in determining the number of reviews a listing receives.

In conclusion, the scatter plot provides a useful way to visualize and understand the relationship between the price of a listing and the number of reviews it has received in the Airbnb dataset. It helps identify trends and patterns in the data, which can be useful for hosts when setting prices or for guests when choosing a place to stay. However, it’s important to remember that correlation does not imply causation, and further analysis would be needed to draw definitive conclusions

Average Reviews per Month by Neighbourhood Group :
The bar chart is used to compare the average reviews per month by neighbourhood group in the Airbnb dataset.The reason for using a bar chart for this comparison is that it allows us to see the differences between categories clearly. Each bar represents a different neighbourhood group, with its height indicating the average reviews per month. This makes it easy to compare the average reviews across different neighbourhood groups.
"""

# Chart - 8 visualization code
# Select numerical columns for correlation analysis
numeric_columns = df.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(10, 6))

sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

"""Analysis of Correlation Heatmap

In the context of the Airbnb dataset, the correlation heatmap helps us understand the relationship between different variables. Here’s an analysis based on the heatmap:

   **‘id’ and ‘host_id’:** A positive correlation of 0.59
suggests that listings from hosts with higher IDs tend to have higher listing IDs. This could be because newer hosts (with higher IDs) would create newer listings (also with higher IDs).

**‘latitude’ and ‘longitude’:** These have low correlations with most other variables, indicating that the geographical location of the listings (as represented by these coordinates) does not have much linear relationship with other numerical features in the dataset.

**‘number_of_reviews’ and ‘reviews_per_month’:** A moderate positive correlation of 0.55 suggests that listings with more reviews tend to have more reviews per month. This could indicate popular listings that consistently receive reviews.

**‘price’ and ‘minimum_nights’:** A negative correlation of -0.15 indicates that listings requiring fewer minimum nights tend to be priced higher. This could be because listings with fewer minimum nights might be in higher demand, allowing for higher prices.

This heatmap is instrumental in understanding how different factors relate to each other within the Airbnb dataset. It can guide further analysis or model building by highlighting significant relationships. For example, if we were to predict the price of a listing, knowing that it has a negative correlation with minimum nights could be very useful. Similarly, understanding that the number of reviews and reviews per month are positively correlated could help in designing a review system or understanding user behavior.

Please note that correlation does not imply causation, and further investigation would be needed to draw definitive conclusions. Also, this analysis is based on the assumption that the data is accurate and reliable. Any inaccuracies in the data could affect the results of the analysis.

Comparison between Price vs Number of Reviews :
The scatter plot is used to compare the price and the number of reviews of listings in the Airbnb dataset. The reason for using a scatter plot for this comparison is that it allows us to see patterns in the data. Each point on the plot represents a listing, with its position on the horizontal axis showing its price and its position on the vertical axis showing the number of reviews it has received. This makes it easy to see at a glance how these two variables relate to each other for the different listings.

#### Chart - 10
"""

# Chart - 10 visualization code
# Bar Plot: Average Reviews per Month by Neighbourhood Group
plt.figure(figsize=(12, 6))
avg_reviews_neighbourhood = df.groupby('neighbourhood_group')['reviews_per_month'].mean().sort_values(ascending=False)
sns.barplot(x=avg_reviews_neighbourhood.index, y=avg_reviews_neighbourhood.values, palette='viridis')
plt.title('Average Reviews per Month by Neighbourhood Group')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Average Reviews per Month')
plt.xticks(rotation=45)
plt.show()

"""**Analysis of Price VS Number of Reviews**

From the bar chart, we can make several observations:

**Queens:** Queens has the highest average reviews per month, indicating that listings in Queens tend to receive more feedback on average each month.

**Staten Island and Bronx:** Staten Island and Bronx have similar average reviews per month, suggesting that listings in these neighbourhood groups receive a similar amount of feedback on average.

**Brooklyn:** Brooklyn has fewer average reviews per month compared to Queens, Staten Island, and Bronx, indicating that listings in Brooklyn may receive less feedback on average.

**Manhattan:** Manhattan has the least average reviews per month, suggesting that listings in Manhattan receive the least feedback on average.

In conclusion, the bar chart provides a useful way to visualize and understand the average reviews per month by neighbourhood group in the Airbnb dataset. It helps identify trends and patterns in the data, which can be useful for hosts when managing their listings or for guests when choosing a place to stay. However, it’s important to remember that these are average values and individual listings may vary.

# **Conclusion**

Final Summary and Conclusion:
The analysis of the Airbnb NYC 2019 dataset has provided valuable insights into various aspects of the Airbnb market, including pricing trends, property types, neighborhood distributions, and market segmentation. Here's a summary of key findings and conclusions derived from the analysis:

Understanding Market Trends:

Pricing Variation: The market analysis revealed a diverse range of pricing options catering to travelers with varying budgets, from budget-conscious options to luxury accommodations.

Property Types: Entire homes/apartments and private rooms are the most popular property types, with shared rooms being less common across neighborhoods.

Factors Influencing Prices and Occupancy Rates:

Correlation Analysis: The correlation heatmap highlighted potential relationships between various factors such as price, number of reviews, and minimum nights.

Price vs. Number of Reviews: The scatter plot revealed a trend where more affordable listings tend to receive more reviews, suggesting price sensitivity among guests.

Neighborhood Analysis:

Distribution of Listings: Different neighborhoods exhibit varying distributions of property types, reflecting their unique characteristics and appeal to different traveler segments.

Popularity by Neighborhood: Queens emerged as the neighborhood with the highest average reviews per month, while Manhattan had the lowest, indicating differences in guest satisfaction levels.

Market Share Analysis:

Price Segmentation: The market share analysis identified distinct price ranges catering to different traveler preferences, from budget-conscious options to luxury accommodations.

Competitive Landscape: Hosts should carefully consider pricing strategies and market positioning within their respective price segments to remain competitive and attract bookings.

**Conclusion:**

The Airbnb NYC 2019 dataset analysis has provided valuable insights for both hosts and guests using the platform. Hosts can leverage these insights to optimize their pricing strategies, enhance property listings, and target specific traveler segments effectively. Additionally, guests can use this information to make informed decisions when choosing accommodations that align with their preferences and budget.

Overall, the findings from this analysis can inform strategic decision-making and drive improvements in the Airbnb ecosystem, ultimately enhancing the experience for both hosts and guests.

### ***Hurrah! You have successfully completed your EDA Capstone Project !!!***
"""