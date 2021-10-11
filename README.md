![Image](https://github.com/JulianTrufero/Claims-Frequency-Predicitons/blob/main/Images/Screenshot%20from%202021-10-11%2013-22-40.png)

- How can we estimate future claims (losses) from a car insurance portfolio?. In this project we aim to model 
the frequency distribution of claim counts for a third-party motor insurance portfolio from the french market, in order to
estimate the expected value of the claim count.
- We chose this subject as is key modelling task in non-life insurance companies for pricing contracts, calculate reserves and pricing of reinsurance contracts.

## The Data Set and Libraries

- It's a 678k insurance policies portfolio data set from [Kaggle](https://www.kaggle.com/floser/french-motor-claims-datasets-fremtpl2freq), with corresponding claim counts and exposures, and 9 variables characterizing the insured drivers, namely:
    Area: Area code
    BonusMalus: A score for the driver
    Density: Population density
    VehAge: Car’s age
    DrivAge: Driver’s age
    VehGas: Gas type (regular or diesel)
    VehPower: Car’s power
    VehBrand: Car’s brand
    Region: France region
    
- In order to perform the Exploratory and Visual Analysis, and the Statistical Modelling, we used these libraries: 

[Json](https://www.json.org/json-en.html), [Folium](http://python-visualization.github.io/folium/), [Matplotlib](https://matplotlib.org/stable/contents.html), [Numpy](https://numpy.org/doc/), [Pandas](https://pandas.pydata.org/docs), [Scikit-learn](https://scikit-learn.org/stable/), [Seaborn](https://seaborn.pydata.org/),
[Statsmodels](https://www.statsmodels.org/stable/index.html)

## Exploratory and Visual Data Analysis

- We first deep dive into our data set, analyzing our target variable (Claims Counts), the Exposure, which accounts for the duration of contracts. And then, all feature components to observe how they relate to our target variable. 

## The Models

- We chose two frameworks: Generalized Linear Models and Decision Trees. For the first one, a Poisson Regression, Negative Binomial Regression and Zero Inflated Poisson Regression. For the second one, Decision Tree Regression with Poisson deviance.
- The choice was thought to show how GLM provides us with explainability but lesser preditctive power then DecisionTree Regression.

## Future Objectives

- Keep the explainability of the regression structure of the GLM but enhancing it's predictive power by combining it with unsupervised classification algorithms over the features.
- Using a Generalized Additive Linear Model to capture some of the non-linear structure of the features. 
