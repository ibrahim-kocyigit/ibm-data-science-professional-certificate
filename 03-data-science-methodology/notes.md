# DATA SCIENCE METHODOLOGY

## Table of Contents
1. [Module 1: From Problem to Approach, and From Requirements to Collection](#module-1)
2. [Module 2: ](#module-2)
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

#### Case Study: Healthcare Budget Allocation
* **Problem:** How to allocate limited healthcare resources to maximize quality care.
* **Goal:** Reduce patient readmissions to minimize costs and improve patient outcomes.
* **Approach:** Use a desicion-tree model to analyze readmission patterns for patiens with congestive heart failure.
* **Key sponsor involvement:** The business sponsor played a crucial role in setting direction, providing guidance, and ensuring support throughout the project.
* **Business requirements:**  
    * Predict readmission outcomes.
    * Predict readmission risk.
    * Understand factors leading to readmission.
    * Apply an easy-to-understand process for assessing readmission risk.

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







---

* **Descriptive:**  
    * Current status
* **Diagnostic (Statistical analysis):**  
    * What happened?
    * Why is this happening?
* **Predictive (Forecasting):**  
    * What if these trends continue?
    * What will happen next?
* **Prescriptive:**  
    * How do we solve it?

**If the question is to determine the probabilities of an action**, use a predictive model.  
**If the question is to show relationships**, use a descriptive model.
**If the question requires a yes/no answer**, use a classification model.

