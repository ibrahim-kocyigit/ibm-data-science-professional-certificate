# WHAT IS DATA SCIENCE

# Module 1: Defining Data Science and What Data Scientists Do

## Defining Data Science
Defining data science is not easy. A lot of experts in the field still have conflicting definitions. The definition we'll go with in this course (and for now) is the following:  

Data science is the art of uncovering the insights and trends hidden within data to understand the world around us. 

While data analysis itself isn't new, recent advancements in data access and computing power have revolutionized our ability to extract knowledge and drive innovation.

## What Do Data Scientists Do?
Similar to detectives uncovering secrets or scientists exploring the natural world, data scientists use a methodical approach to glean insights from data:

* Clarify the Problem: Define the question or problem you're trying to solve with data.
* Data Collection: Gather relevant data from various sources.
* Analysis: Apply statistical and computational techniques to analyze the data.
* Pattern Recognition: Identify patterns, trends, and anomalies in the data.
* Storytelling: Translate the data insights into a compelling narrative.
* Visualization: Create visual representations of the data and insights.

### Essential Skills for Data Scientists
Beyond technical expertise in statistics and programming, successful data scientists possess:

* Curiosity: To explore data and ask meaningful questions.
* Argumentation: To effectively communicate findings and persuade others.
* Judgment: To guide the analysis process and make informed decisions.

### The Evolving Role of the Data Scientist
Companies seek versatile data scientists with:

* Domain Expertise: Deep knowledge in a specific field.
* Analytical Skills: Proficiency in data analysis and programming.
* Communication Skills: Ability to clearly convey insights to both technical and non-technical audiences.

Data scientists often have diverse backgrounds in fields like economics, engineering, and medicine. 

As technology evolves, so too will the role of the data scientist. Continuous learning and adaptation are essential for success in this dynamic field.

# Module 2: Data Science Topics

## Big Data and Data Mining
In the 'Big Data and Data Mining' lesson, delve into the world of digital transformation driven by Big Data. Explore Cloud Computing's role, foundational Big Data concepts, tools like Hadoop and Spark, and gain insights into Data Mining techniques for informed decision-making.

### How Big Data is Driving Digital Transformation
* Digital transformation is driven by data science, especially Big Data, leading to fundamental changes in how organizations operate and deliver value.
* Big Data analysis provides a competitive advantage and has led to transformations across industries (e.g., Netflix, Houston Rockets, Lufthansa).
* Digital transformation involves in-depth analysis to improve processes, not just digitizing existing ones. 
* Organizations must adapt their approach to data, employees, and customers, leading to cultural shifts.
* Successful transformation requires support from top-level executives (CEO, CIO, CDO) and organization-wide buy-in.
* Digital transformation necessitates a new mindset and is crucial for success in the current and future business landscape.

### Introduction to Cloud
* **Cloud computing** delivers on-demand computing resources (servers, storage, etc.) over the internet on a pay-as-you-go basis.
* **Five essential characteristics of cloud computing** are:    
    * **On-demand self service:** Users can access resources as needed without requiring human interaction with the provider.
    * **Broad network access:** Resources are accessible over the network through various devices (phones, laptops, etc.).
    * **Resource pooling:** Provider's resources are pooled to serve multiple clients, offering cost efficiency.
    * **Rapid elasticity:** Resources can be scaled up or down quickly based on demand.
    * **Measured service:** Pay-as-you-go model where users are charged only for the resources they consume.
* **Three cloud deployment models** are:    
    * Public cloud (shared resources over the internet)
    * Private cloud (exclusive use by a single organization)
    * Hybrid cloud (mix of public and private)
* **Three cloud service models** are:  
    * **IaaS (Infrastructure as a Service):** Access to infrastructure (servers, storage) without managing it.
    * **PaaS (Platform as a Service):** Access to a platform for developing and deploying applications.
    * **SaaS (Software as a Service):** Access to software applications over the internet on a subscription basis.

### Cloud for Data Science
**Cloud computing for Data Science** allows for centralized data storage and access to advanced computing resources, bypassing local limitations.

**Benefits:**  
* Store and process large datasets.
* Access advanced algorithms and high-performance computing.
* Enables collaboration by allowing multiple users to work with the same data simultenaously.
* Provides access to open-source tools (like Apache Spark) without local installation.
* Offers access to the latest tools and libraries.
* Accessible from anywhere and anytime, faciliating collaboration.

### Foundations of Big Data
**Big Data** refers to the massive and diverse volumes of data generated by people, tools, and machines. It requires new technologies to process and extract meaningful insights.

**The 5 V's of Big Data**  
* **Velocity:** The speed at which data is generated and accumulates.
* **Volume:** The scale or amount of data.
* **Variety:** The different types and sources of data (structured and unstructured)
* **Veracity:** The quality, accuracy, and trustworthiness of data.
* **Value:** The ability to extract meaningful insights and benefits from data.

**Challenges of Big Data** is that it requires new tools and techniques to analyze due to its volume and variety.

**Tools for Big Data analysis** include Apache Spark, and Hadoop ecosystem.

**Benefits of Big Data**: Provides insights for organizations to connect with customers and improve services.

### Data Science and Big Data
* **Data science needs computational thinking:** Data scientists need programming skills and the ability to think computationally.
* **Demand for data science is increasing:** Data science and analytics are hot fields with growing demand from employers and students.
* **Big data** is data that is too large and complex to be handled by traditional database systems.
* **Origins of big data:** Google's need to store and process massive amounts of web data led to the development of new technologies and techniques.
* **Big data analysis:** New technical and statistical techniques are needed to handle massive datasets, including deep learning.

### What is Hadoop?
* **Hadoop** was developed by Doug Cutting at Yahoo, based on Google's big data architecture. It distributes data across a cluster of computers, processes it in parallel, and combines the results. This allows for linear scaling and handling massive dahasets.
* **Data science components:** Combines established fields like probability, statistics, linear algebra, programming, and databases with newer techniques like machine learning.
* **Machine learning in data science** enables pattern identification in large datasets, moving beyond traditional testing: Now we're able to find patterns first, then infer hypothesises out of these patterns, then test our hypothesises.
* **Data science is a rapidly evolving field.** New techniques like deep learning and neural networks are constantly being added to the mix.

### Big Data Processing Tools: Hadoop, HDFS, Hive, and Spark
* **Hadoop:** Open-source framework for distributed storage and processing of large datasets.
    * Enables handling of various data formats (structured, unstructured, semi-structured)
    * Provides real-time, self-service access to data.
    * Cost-effective solution for storing and processing large datasets.
* **HDFS (Hadoop Distributed File System):** Storage system for big data.
    * Partitions files across multiple nodes for parallel access.
    * Replicates data for fault tolerance and high availability.
    * Benefits: Data locality, scalability, fast recovery.
* **Hive:** Data warehouse built on top of Hadoop for querying and analyzing data.
    * Suitable for ETL, reporting, and data analysis.
    * Less suitable for real-time applications and transaction processing.
* **Spark:** General-purpose data processing engine for large datasets.
    * Uses in-memory processing for fast computations.
    * Supports various programming languages (Java, Python, R, etc.) and data sources.
    * Key use case: Real-time stream processing and complex analytics.

### Data Mining
1. **Establish Clear Goals:** Define key questions, cost-benefit considerations, and desired accuracy levels.
2. **Select relevant data:** Identify and gather appropriate data from various sources, considering cost and quality.
3. **Preprocess data:** Clean and prepare data by handling errors, inconsistencies, and missing values.
4. **Transform data:** Reduce the number of attributes, aggregate or transform variables as needed.
5. **Mine data:** Apply data analysis methods, including visualization and machine learning algorithms.
6. **Evaluate results:** Assess the effectiveness of the data mining process, test predictive capabilities, and gather stakeholder feedback.

**Iterate and improve:** Refine the process based on evaluation and feedback to achieve better results.

## Deep Learning and Machine Learning

### Artificial Intelligence and Data Science
* **Big data:** Massive, rapidly growing, and diverse datasets that require specialized tools and techniques for analysis.
* **Data mining:** Process of discovering patterns and insights in data, involving preprocessing, transformation, and analysis.
* **Machine learning:** Subset of AI where algorithms learn from data to make decisions without explicit programming.
* **Deep learning:** Specialized machine learning using neural networks to simulate human decision-making and improve accuracy over time.
* **Neural networks:** Interconnected computing units (neurons) that learn from data to make decisions.
* **Data Science vs. AI:**
    * Data science extracts knowledge and insights from data using various techniques, including AI.
    * AI focuses on enabling computers to learn and make intelligent decisions.
    * One is not the subset of the other.
    * Both can involve big data.

### Generative AI and Data Science
* **Generative AI** creates new data (images, text, code, etc.) that resembles real data, going beyond just analyzing existing data.
* **How it works:** Uses deep learning models like GANs and VAEs to learn patterns from data and generate new instances.
* **Applications:** Natural language processing (chat bots), healthcare (creating sample x-rays for medical students for educational purposes), art, gaming, fashion, etc.
* **Generative AI in Data Science:**  
    * Creates synthetic data to augments datasets for model training and testing.
    * Automates code generation for building analytical models, freeing up data scientists for high-level tasks.
    * Generates insights and reports, uncovering hidden patterns and enhancing decision-making Example: IBM Cognos Analytics uses AI to generate insights from natural language queries.

### Neural Networks and Deep Learning
* **Neural networks:** Computing systems inspired by the human brain, consisting of interconnected nodes (neurons) that process and learn from the data.
* **Deep learning:** Neural networks with multiple layers, enabling more complex learning and improved accuracy on large datasets. Deep learning has revolutionized AI by enabling machines to learn and solve complex problems from vast amount of data.
* **Computational intensity:** Deep learning requires significan computing power, often utilizing GPUs (Graphic Processing Units).
* **Applications:** Speech recognition, image recognition and classification, natural language processing.

### Applications of Machine Learning
* **Machine learning applications are widespread:** They are used in various fields, including recommender systems, classification, cluster analysis, and predictive analysis.
* **Tools like R simplify machine learning:** Users can apply techniques without needing in-depth knowledge of the underlying algorithms, but they should understand the implications and trade-offs.
* **Machine learning in fintech:**
    * Recommendations: Suggest relevant investment ideas or financial products based on user behavior and preferences, similar to Netflix or Facebook recommendations.
    * Fraud detection: Identify fraudulent transaction in real-time by learning from historical data and building predictive models.

### Regression
* **Regression to the mean:** Taller parents tend to have tall children, but those children are not necessarily taller than their parents. This phenomenon is known as regression to the mean.
* **Regression models:** Statistical tools used to analyze relationships between variables and quantify their effects.They provide valuable insights by quantifying the relationships between variables, enabling better understanding and decision-making. They have broad applications in various fields, including medicine and business. 
* **Quantifying relationships:** Regression models go beyond simply identifying correlations; they determine the magnitude and direction of relationships between variables.
* **Example: Hedonic price models for housing:**  
    * Identify factors that influence housing prices (e.g., size, location, features)
    * Quantify the impact of each factor on price (e.g., an additional washroom adds more value than an extra bedroom)
    * Reveal non-linear relationships (e.g., proximity to shopping centers).

# Module 3: Data Science Application Domains