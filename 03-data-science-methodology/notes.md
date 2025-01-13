# DATA SCIENCE METHODOLOGY

## Table of Contents
1. [Module 1: From Problem to Approach, and From Requirements to Collection](#module-1)
2. [Module 2: From Understanding to Preparation, and From Modeling to Evaluation](#module-2)
3. [Module 3: ](#module-3)
4. [Module 4: ](#module-4)

# Module 1: From Problem to Approach, and From Requirements to Collection <a name="module-1"></a>

## Problem to Approach

### Data Science Methodology Overview
Methodology is a systematic approach or set of methods used to guide research or problem-solving in a particular field. It provides a framework for making decisions and ensuring that the process is efficient and effective.

**Data science methodology** is a structured approach to guide data scientists in solving complex problems and making data-driven decisions. It includes steps for data collection, preparation, analysis, and interpretation.

The data science methodology presented in the course is based on the work of **John Rollings**, an experienced data scientist at IBM.

#### 10 Stages of Data Science Methodology
1. **Business Understanding:** Define the problem: "What is the problem that I am trying to solve?"
2. **Analytic Approach:** Determine the appropriate analytical techniques: "How can I use data to answer the question?"
3. **Data Requirements:** Identify the necessary data: "What data do I need?"
4. **Data Collection:** Gather the data from relevant sources: "Where is the data located and how will I get it?"
5. **Data Understanding:** Explore and understand the data's characteristics: "Does the data represent the problem accurately?"
6. **Data Preparation:** Clean, transform, and prepare the data for analysis: "What additional work (preprocessing) is needed to manipulate and work with the data?"
7. **Modeling:** Build and train models to analyze the data: "When I apply data visualizations, do I see answers that address the business problem?"
8. **Evaluation:** Asses the model's performance and validity: "Does the model answer the business question or must I adjust the data?"
9. **Model Deployment:** Implement the model and integrate it into applications or systems: "Can I put the model into practice?"
10. **Feedback:** Gather feedback and iterate on the model based on real-world performance and stakeholder input: "Can I get constructive feedback from the data and the stakeholder to answer the business question?"

### Business Understanding
_What is the problem that I am trying to solve?_

The crucial first step in the data science methodology is **business understanding**, where you gain a deep understanding of the problem you're trying to solve. This involves clarifying the goals, objectives, and stakeholders involded.

**Importance of clear problem definition:** 
* A clearly defined problem directs the analytical approach and ensures you're solving the right problem.
* Avoid wasting effort on answering the wrong questions or addressing incorrect assumptions.

**Clarifying goals and objectives:**  
* Understand the underlying goal of the person asking the question.
* Break down the goal into specific, measurable objectives.
* Prioritize objectives to guide the analysis and decision-making.

**Stakeholder engagement:**  
* Involve relevant stakeholders in discussions to clarify requirements and ensure alignment.

### Analytic Approach
_How can you use data to answer the question?_

When choosing an analytical approach for a problem, the type of question you're trying to answer greatly influences the methodology. Here are five common types of questions and corresponding analytic approaches:

#### 1. Descriptive Questions: "What is the current status?"
**Approach: Descriptive Analytics**  

**Question:** "What is the current status of our sales?"  

**Techniques:** 
* Data aggregation: Combining data from various sources into a unified view.
* Data mining: Extracting useful information from large datasets.
* Data visualization: Using visual tools to present data in an easily understandable format.  

**Examples:**  
* Summarizing sales data
* Creating dashboards
* Generating reports

#### 2. Diagnostic Questions: "Why did it happen?"
**Approach: Diagnostic Analytics**  

**Question:** "Why did our sales decline in the last quarter?"  

**Techniques:**  
* Drill-down: Exploring detailed data to find underlying causes.
* Data discovery: Identifying patterns and relationships in data.
* Correlation analysis: Assessing the relationship between different variables.

**Examples:**  
* Identifying root causes for sales decline
* Analyzing customer complaints
* Understanding failure points in a process

#### 3. Predictive Questions: "What is likely to happen?"
**Approach: Predictive Analytics**  

**Question:** "What is our sales forecast for the next year?"  

**Techniques:** 
* Regression analysis: Predicting outcomes based on relationships between variables.
* Time series forecasting: Predicting future values based on past trends.
* Machine learning models: Using algorithms to predict future outcomes based on historical data.

**Examples:**  
* Forecasting sales
* Predicting customer churn
* Estimating future demand

#### 4. Prescriptive Questions: "What should we do?"
**Approach: Prescriptive Analytics**  

**Question:** "What should we do to increase website traffic?"

**Techniques:**  
* Optimization models: Finding the best solution from a set of alternatives.
* Simulation: Modeling scenarios to predict outcomes.
* Decision analysis: Evaluating and comparing different decisions.

**Examples:**  
* Recommending inventory levels
* Optimizing marketing campaigns
* Determining pricing strategies

#### 5. Classification Questions: "Which category does this belong to?"
**Approach: Classification (Supervised Learning)**  

**Question:** Which category does this data point belong to?"

**Techniques:**  
* Logistic regression: Predicting the probability of a categorical outcome.
* Decision trees: Splitting data into branches to classify it.
* Support vector machines: Finding the best boundary to separate categories.
* Neural networks: Using interconnected nodes to classify data.

**Examples:**  
* Email spam detection
* Image classification
* Disease diagnosis

## From Requirements to Collection

### Defining Data Requirements
_What data do I need?_

The third stage of the data science methodology is **data requirements**, where you identify and specify the data needed to solve the problem. This involves determining the type, format, sources, and content of the data.

**Importance of defining data requirements:**  
* Ensures you collect the right data to answer the question
* Guides the data collection and preparation process.
* Helps avoid collecting unnecessary or irrelevant data.

### Data Collection
_Where is the data located and how will I get it?_

**Data collection** is the fourth stage of the data methodology, where you gather the data identified in the data requirements stage. This stage may involve accessing various data sources, extracting data, and performing initial assessments of the data's quality and completeness.

**Iterative nature of data collection:**  
* Data collection may require revisiting the data requirements stage if certain data is unavailable or if gaps are identifies.
* It's an iterative process where you adjust your data collection strategy based on initial findings and assessments.

**Assessing data quality and completeness:**  
* Use descriptive statistics and visualizations to understand the data's characteristics, identify potential issues, and assess its suitability for analysis.
* Identify any missing data or inconsistencies that need to be addressed.

# Module 2: From Understanding to Preparation, and From Modeling to Evaluation <a name="module-2"></a>

## From Understanding to Preparation

### Data Understanding
_Is tha collected data representative of the problem to be solved?_

**Data understanding** is the fifth stage of the data science methodology, where you explore and analyze the collected data to gain a deeper understanding of its characteristics, quality, and relevance to the problem. It's often a **iterative process**, involving going back to previous states to redefine the data or address issues during analysis.

**Key question in data understanding** is this: "Is the data you collected representative of thr problem you're trying to solve?"

Data understanding stage usually involves the following and more:
* **Descriptive statistics:**  
    * Univariate analysis (mean, median, min, max, standard deviation) to understand individual variables.
    * Pairwise correlations to identify relationships between variables and potential redundancy.
* **Histograms** are used to visualize the distribution of variables and identify potential issues like outliers or skewed distributions.
* **Data quality assessment** involves identifying and addressing missing values, invalid entries, or inconsistencies in the data.
* **Refining data definition** is when the data understanding shows that the initial definition of some data needs refining. 

### Data Preparation Concepts
_What additional work (preprocessing) is needed to manipulate and work with the data?_

**Data preparation** is the sixth stage of the data science methodology, where you clean, transform, and prepare the data for analysis. This stage often involves handling missing values, correcting errors, and engineering new features.

**Time-consuming, but crucial:** Data preparation is typically the most time-consuming part of a data science project, often taking 70-90% of the total project time. However, automating some processes can significantly reduce this time.

**Key tasks in data preparation:**  
* Handling missing or invalid values.
* Removing duplicate records.
* Ensuring proper data formatting and consistency.
* Feature engineering.

**Feature engineering:**  
* Using domain knowledge to create new features that improve the performance of ML algorithms.
* Selecting and transforming relevant features to enhance model accuracy and interpretability.

**Text analysis:**  
* If working with text data, perform text analysis to extract meaningful information and prepare it for modeling.
* This may involve cleaning, tokenizing, and converting text into numerical representations. 

## From Modeling to Evaluation

### Modeling: Concepts

**Data modeling** is the stage where you build and train models to analyze and interpret the prepared data. This stage involves selecting appropriate algorithms, training the models, and evaluating their performance. 

**Purpose of data modeling:**  
* Develop descriptive models to understand relationships and patterns in the data.
* Develop predictive models to forecast future outcomes or classify data into categories.

![Purpose of data modeling](https://github.com/ibrahim-kocyigit/ibm-data-science-professional-certificate/blob/main/media/modeling-concepts.png)
