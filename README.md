# Rossmann Sales Prediction

![image](https://user-images.githubusercontent.com/67356304/139589757-67b447f4-9c56-4b5b-a8e9-02d8d21da292.png)


# 1. Business Problem
Planning to do a redevelopment on all Rossmann drug stores, the CFO of the company requested a sales prediction for each store for the next six weeks. The prediction model that was currently being used was not good enough, so a new and more robust model was requested in order to get a more accurate sales prediction.

# 2. Business Assumptions
* The days when stores were closed were removed from the analysis;
* Only stores with sales values bigger than 0 were considered;
* For stores which did not have Competition Distance information, it was considered that the distance should be the longest distance observed in the data set.

## 2.1 Attribute List

* Id - an Id that represents a (Store, Date) duple within the test set;
* Store - a unique Id for each store;
* Sales - the turnover for any given day (this is what you are predicting);
* Customers - the number of customers on a given day;
* Open - an indicator for whether the store was open: 0 = closed, 1 = open;
* StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None;
* SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools;
* StoreType - differentiates between 4 different store models: a, b, c, d;
* Assortment - describes an assortment level: a = basic, b = extra, c = extended;
* CompetitionDistance - distance in meters to the nearest competitor store;
* CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened;
* Promo - indicates whether a store is running a promo on that day;
* Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating;
* Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2;
* PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store;

# 3. Solution Strategy
To develop the sales prediction model it was used 10 steps. 
The plan is to develop a solution that can quickly be implemented, but can also be improved in the future, so to help with this it was used the CRISP-DM method.

Step 1 - Data Description: At this step the objective is to get more familiarized with the data and take a closer look on a myriad of information, such as number of rows and columns, data types, NAs, how to fill up NAs, and also statistical metrics as well, like, Min, Max, Range, Mean, Median, std, skew and kurtosis. 

Step 2 - Feature Engineering: The goal of this step is to obtain new attributes based on the original variables, in order to better describe the phenomenon to be modeled.

Step 3 - Data Filtering: The goal of this step is to filter rows and delete columns that are not relevant for the model or are not part of the business scope.

Step 4 - Exploratory Data Analysis (EDA): The goal of this step is to explore the data to find insights and better understand the impact of variables on model learning.

Step 5 - Data Preparation: The goal of this step is to prepare the data for application of the machine learning model.

Step 6 - Feature Selection: The goal of this step is to select the better attributes to train the model. The Boruta Algorithm was used to make the selection.

Step 7 - Machine Learning modeling: The goal of this step is to do the machine learning model training.

Step 8 - Hyperparameter Fine Tuning: The goal of this step is to choose the best values for each of the parameters of the model selected in the previous step.

Step 9 - Convert model performance to business values: The goal of this step is to convert model performance to a business result.

Step 10 - Deployment of Model: The goal of this step is to publish the model in a cloud environment so that other people or services can use the results to improve the business decision. The cloud application platform choosed was Heroku.

# 4. Top 3 Data Insights
**H1:** Stores with closer competitors should sell less.<br />
**FALSE** Stores with CLOSER COMPETITORS sells MORE.

![sells competition closer](https://user-images.githubusercontent.com/67356304/140009245-9659f820-f6a8-4b6e-b239-7367f3bee959.jpg)


# 5. Machine Learning Model Applied

# 6. Machine Learning Model Performance

# 7. Business Results

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve
