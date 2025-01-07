# WHAT IS DATA SCIENCE?

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
* **Hadoop** was developed by Doug Cutting at Yahoo, based on Google's big data architecture. It distributes data across a cluster of computers, processes it in parallel, and combines the results. This allows for linear scaling and handling massive datasets.
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

# Module 3: Applications and Careers in Data Science

## Data Science Application Domains

### How Should Companies Get Started in Data Science?
* **Measurement is crucial:** If companies can't measure something, they can't improve it. Start by capturing and recording data (e.g., costs, revenue, and customers, etc).
* **Data is valuable:** Archive data and don't overwrite it. Even old data can be relevant for analysis and insights.
* **Data consistency and documentation:** Ensure data is documented properly for future use and understanding.
* **Data quality matters:** Garbage in, garbage out. The value of data science depends on the quality of data collected.
* **Measure, then clean:** If data doesn't exist, start collecting it. If it exists, clean and analyze it.
* **Build a data science team:** A team of data scientists with diverse skills is key to success.
* **Foster interest and engagement:** Employees should be interested in and engaged with data science initiatives.

### Old Problems, New Data Science Solutions
* **Data science for problem solving:** Organizations use data science to find optimal solutions to existing problems.
* **Examples of data science solutions:**  
    * Uber optimizes driver allocation and pricing based on real-time data.
    * Toronto Transportation Commission reduced traffic congestion by analyzing streetcar operations, customer complaints, and traffic flow data.
    * Scientist use high-tech tools and algorithms to predict and address harmful cyanobacterial blooms in freswater lakes.
* **Developing effective data solutions:**  
    * Clearly identify the problem.
    * Gather and prepare relevant data.
    * Select appropriate tools and develop a data strategy.
    * Utilize case studies and machine learning models.

### Applications of Data Science
* **Data science impacts businesses:** It influences operations, financial analysis, and customer interactions.
* **Recommendation engines:** Companies like Amazon, Netflix, and Spotify use data science to personalize recommendations based on user preferences and behaviour.
* **Personalized experiences:** Personal assistants and Google services utilize data to provide tailored recommendations and answers.
* **Wearable devices** contribute to data generation by providing information about activity levels, sleep, heart rate, etc.
* **Data as a competitive advantage:** In 2011, McKinsey predicted data science would drive competition, productivity, and innovation.
* **Netflix Example:**  Netflix analyzes user data to predict show success before even filming. They also combine data on director, actor, and show preferences to make informed content investments.

### How Data Science is Saving Lives
* **Data science in healthcare:**  
    * Uses predictive analytics to recommend best treatment options for patients based on various factors.
    * Provides physicians with access to the latest disease information and treatment plans.
    * Improves patient outcomes by ensuring consistent access to knowledge and best practices.
    * Example: Identifying appropriate diagnostic tests based on gene markers and patient characteristics.
* **Electronic Medical Records (EMR):**  
    * Rich source of data for medical research.
    * Enables sophisticated data analysis and predictive insights.
* **Data science in disaster preparedness:**  
    * Predicts natural disasters (earthquakes, hurricanes, floods, etc.) using large datasets.
    * Social media data compliments scientific data to improve localized weather predictions.

### The Final Deliverable
* **Communication is key:** The purpose of analytics is to communicate findings effectively to stakeholders.
* **Deliverables in different contexts:**  
    * Academia: Essays and reports.
    * Consulting/Business: Documents of varying lengths, often with visualizations.
* **Effective deliverables:**  
    * Use data and analytics to build a compelling narrative.
    * Example: Deloitte's "United States Economic Forecast"
        * Presents a clear thesis statement
        * Uses visualization to illustrate trends
        * Connects economic data to broader social context
        * Establishes Deloitte's expertise
* **Narrative is crucial:** Simply presenting data without a narrative fails to communicate the intended message effectively.
* **Plan the deliverable:** Conceptualize the key message and scope before starting the analysis to ensure a cohesive and impactful final product.

## Careers and Recruiting in Data Science

### How Can Someone Become a Data Scientist?
Becoming a data scientist requires a combination of foundational knowledge, practical skills, continuous learning, and motivation.

* **Data scientist skills:**  
    * Strong foundation in programming, math (algebra, calculus), probability, statistics, and databases.
    * Understanding of relational databases and big data concepts.
    * Advanced data scientists often have PhDs and expertise in computer science theory and statistics.
* **Self-learning and hands-on experience:**  
    * Online learning platforms and tools like Jupyter notebooks provide opportunities for practival application.
    * Building and tinkering with projects enhances understanding.
    * Motivation is crucial for continous learning.
* **Data science in organizations:**  
    * Data science teams should ideally be aligned with research and development rather than IT.
    * High demand for PhD-level data scientists in research-driven industries (pharmaceuticals, finance, technology).

### Recruiting for Data Science
* **Hiring data scientists:**  
    * Avoid searching for "unicorns" with every skill imaginable.
    * Priotize passion for the business domain and cultural fit.
    * Technical skills can be taught, but curiosity and soft skills are essential.
* **Key traits to look for:**  
    * Curiosity about the world and the business.
    * Sense of humor and lighthearted approach.
    * Strong communication and storytelling skills.
    * Technical skill are important but can be developed.
* **Additional considerations:**  
    * Technical skills should align with the type of data and platform used.
    * Data scientists need to build relationships and work across departments.
    * Problem-solving and analytical thinking are crucial.
    * Consider the specific role and needs of the data science team.

### Careers in Data Science
* **Data science is a rapidly growing field:** Driven by the Internet of Things and advances in computing, leading to increased demand for data scientists.
* **High demand and promising career:**  Data science consistently ranks as a top career choice with significant growth predicted in the data science platform market.
* **Data science skills:**  
    * Aptitude for working with data.
    * Coding skills.
    * Math and statistical knowledge.
    * Strong communication and storytelling abilities.
* **Continious learning:** Data scientists need to continiously acquire new skills and stay updated on the latest tools and techniques.
* **Diversity in data science:** Initiatives like "Women in Data Science" promote inclusivity and support for underrepresented groups.
* **Tailor your skills:** Focus on developing skills relevant to your desired data science role and utilize online resources for training.

### Importance of Mathematics and Statistics for Data Science
* **Data science requires a foundation in math and statistics:** Programming, math, probability, and statistics are essential skills.
* **Hands-on experience is crucial:** Building and experimenting with data and systems helps solidify understanding and identify learning needs.
* **Cultivate curiosity:** Encourage exploration, problem-solving, and a "detective" mindset.
* **Data science is a valuable career path:** It's a highly sought-after profession with growing demand in various industries.
* **Connect math to real-world problems:** Applying math to relevant problems can make it more engaging and easier to understand.

### The Report Structure
Before starting the analysis, think about the structure of the report. Will it be a brief report of five or fewer pages, or will it be a longer document running more than 100 pages in length? The structure of the report depends on the length of the document.

* **A brief report** is more to the point and presents a summary of key findings.
* **A detailed report** incrementally builds the argument and contains details about other relevant works, research methodology, data sources, and intermediate findings along with the main results.

1. **Cover Page**  
At a minimum, the cover page should include the title of the report, names of authors, their affiliations, and contacts, the name of the institutional publisher (if any), and the date of publication.

2. **Table of Contents**  
The ToC with main headings and lists of tables and figures offers a glimpse of what lies ahead in the document. Never shy away from including a ToC, especially if your document, excluding cover page, table of contents, and references, is five or more pages in length.

3. **Executive Summary**  
Even for a short document, I recommend an "abstract" or an "executive summary". Nothing is more powerful than explaining the crux of your arguments in three paragraphs or less. Of course, for larger documents running a few hundred pages, the executive summary could be longer.

4. **Detailed Contents**  
* **Introductory:** section is always helpful in setting up the problem for the reader who might be new to the topic and who might need to be gently introduced to the subject matter before being immersed in intricate details. 
* **Review:** A review of available relevant research on the subject matter. The length of the literature review section depends upon how contested the subject matter is. In instances where the vast majority of researchers have concluded in one direction, the literature review could be brief with citations for only the most influential authors on the subject. On the other hand, if the arguments are more nuanced with caveats aplenty, then you must cite the relevant research to offer adequate context before you embark on your analysis. You might use the literature review to highlight gaps in the existing knowledge, which your analysis will try to fill. This is where you formally introduce your research questions and hypothesis.
* **Methodology:** Introduce the research methods and data sources you used for the analysis. If you have collected new data, explain the data collection exercise in some detail. You will refer to the literature review to bolster your choice for variables, data, and methods and how they will help you answer your research questions.
* **Results:** Where you present your empirical findings. Starting with descriptive statistics and illustrative graphics, you will move toward formally testing your hypothesis. Note that many reports in the business sector present results in a more palatable fashion by holding back the statistical details and relying on illustrative graphics to summarize the results.
* **Discussion:** Craft your main arguments by building on the results you have presented earlier. This section is where you rely on the power of narrative to enable numbers to communicate your thesis to your readers. You refer the reader to the research question and the knowledge gaps you identified earlier. You highlight how your findings provide the ultimate missing piece to the puzzle. Of course, not all analytics return a smoking gun. At times, more frequently than I would like to acknowledge, the results provide only a partial answer to the question and that, too, with a long list of caveats.
* **Conclusion:** Generalize your specific findings and take on a rather marketing approach to promote your findings so that the reader does not remain stuck in the caveats that you have voluntarily outlined earlier. You might also identify future possible developments in research and applications that could result from your research.

5. **Acknowledgments**  
Acknowledging the support of those who have enabled your work is always good.

6. **References**  
A list of references.

7. **Appendices (if needed)**  
If you have any appendices, list them here.

#### Checklists
* Have you told readers, at the outset, what they might gain by reading your paper?
* Have you made the aim of your work clear?
* Have you explained the significance of your contribution?
* Have you set your work in the appropriate context by giving sufficient background (including a complete set of relevant references) to your work?
* Have you addressed the question of practicality and usefulness?
* Have you identified future developments that might result from your work?
* Have you structured your paper in a clear and logical fashion?

A clearly organized and logical report should communicate the following to the reader:

* What they gain by reading the report
* Clearly defined goals
* The significance of your contribution
* Appropriate context by giving sufficient background 
* Why this work is practical and useful
* Conjecture plausible future developments that might result from your work  

### A Roadmap to Your Data Science Journey
#### Personality Characteristics
* Be curious
* Make sound arguments
* Use good judgment
* Familiarize with analytics platforms
* Be a good storyteller
* Know your area of interests (such as healtcare or IT)

#### Many Paths
* Diverse educational and career backgrounds
* Exposure to data challenges sparked interest
* Data science is adaptable across professions

#### Data Literacy
* Analyze both structured and unstructured data
* Understand file formats
* Database and SQL skills
* Big Data, Cloud

#### Tools & Techniques
* Programming with Python and R
* Hadoop
* Python libraries: NumPy, Pandas, Scikit-learn
* Data visualization tools
* Machine learning algorithms
* Data preprocessing techniques

#### Foundational Skills
* Statistical knowledge
* Mathematics, calculus, linear algebra
* Exploratory data analysis
* Select, train, and test models
* Communication and presentation skills

#### Range of Tasks
* Build recommendation engines
* Predictive modeling
* Data analysis and problem solving
* Identify patterns
* Utilize external data sources
* Communication of findings

# Module 4: Data Literacy for Data Science (Optional)

## Understanding Data

### What is Data?
Data is unorganized information that is processed to become meaningful.

#### Types of Data:
* **Structured data:** Organized, adheres to a schema, and can be stored in relational databases (e.g., SQL databases, online transaction processing, spreadsheets, online forms, sensors GPS and RFID, network and web server logs)
* **Semi-structured data:** Has some organizational properties but lacks a rigid schema (e.g., emails, XML and other markup languages, binary executables, TCP/IP packets, zipped files, integration of data)
* **Unstructured data:** Lacks a predefined structure and doesn't fit neatly into traditional databases (e.g., web pages, social media feeds, images in varied file formats, video and audio files, documents and PDF files, PowerPoint presentations, media logs, surveys)

### Data Sources
* **Data sources are diverse:** Ranging from internal databases to external APIs and web scraping.
* **Common data sources:**  
    * **Relational databases:** Store structural data within organizations (e.g., SQL Server, Oracle)
    * **Flat files and XML datasets:** Publicly or privately available data in various formats (e.g., CSV, spreadsheets, XML)
    * **APIs and web services:** Provide access to data from various platforms and applications (e.g., Twitter API, stock market APIs)
    * **Web scraping:** Extracts data from websites for analysis and comparison.
    * **Data streams and feeds:** Real-time data from various sources (e.g., stock stickers, sensor data, social media feeds)

### Viewpoints: Working with Varied Data Sources and Types
* **Data variety:** Data comes in various formats and from diverse sources, requiring flexibility in handling and processing.
* **Challenges with relational databases:** While widely used, relational databases may not be suitable for all situations, particularly write-intensive applications like IoT and social media.
* **Rise of NoSQL and Big Data:** NoSQL databases (e.g., Cassandra, Hbase) address limitations of relational databases for specific use cases.ü
* **Data formats and their evolution:** Data professionals need to be familiar with various formats like CSV, JSON, XML, and understand their strengths and weaknesses.
    * Log data requires custom parsing due to its unstructured nature.
    * XML, while popular, can be resource-intensive.
    * JSON offers efficiency and is widely used in RESTful APIs.
    * Newer formats like Apache Avro are gaining popularity.
* **Data migration challenges:** Moving data between different database systems (e.g., Db2 to SQL Server) can present challenges due to data formatting, special characters, and differing import/export mechanisms.

### Metadata and Metadata Management
* **Metadata** is data that provides information about other data.
* **Types of metadata:**  
    * **Technical metadata:** Defines data structures in data repositories (e.g., table names, columns, data types).
    * **Process metadata:** Describes processes within systems (e.g., process start/end times, disk usage).
    * **Business metadata:** Provides business context for data (e.g. data acquisition, meaning ,connection to other sources).
* **Metadata management:** Involves policies and processes to ensure metadata is accessible, integrated, and shared effectively.
* **Data catalog:** A core component of metadata management, serving as an inventory and organizational tool for data assets.
* **Importance of metadata management:**  
    * Enhances data discovery and understanding.
    * Improves data governance by providing data lineage and context.
    * Facilitates data quality, integrity, and security.

## Data Literacy

### Data Collection and Organization
* **Data repository:** A centralized location for storing and organizing data for various purposes (e.g., operations, analysis).
* **Databases:** Collections of data designed for efficient storage, retrieval, and modification.
* **Database Management Systems (DBMS):** Software that manages and controls access to a database (e.g., creating, querying, modifying data). 
* **Types of databases:**  
    * **Relational databases (RDBMS):** Organize data in tables with rows and columns, using SQL for querying (e.g., SQL Server, Oracle).
    * **Non-relational databases (NoSQL):** Offer flexibility and scalability for handling diverse data types, often used for Big Data (e.g., Cassandra, MongoDB).
* **Data warehouse:** A central repository that consolidates data from various sources for analytics and business intelligence.
* **ETL process:** Extracts, transforms, and loads data into a data warehouse.
* **Big bata stores:** Distributed systems for storing and processing massive datasets. 

### Relational Database Management Systems
* **Relational databases:** Organize data in tables with rows (records) and columns (attributes), linked by common fields.
* **Key features:**  
    * Relationships between tables enable efficient querying and analysis.
    * SQL (structured query language) is used for data manipulation and retrieval.
    * Optimized for large data volumes and complex queries.
    * Minimizes data redundancy and ensures data integrity.
    * Provides controlled access and security for data governance.
* **Advantages:**  
    * Flexibility for schema changes.
    * Reduced data redundancy.
    * Easy backup and disaster recovery.
    * ACID (Atomicity, consistency, isolation, durability) compliance for data consistency and reliability.
* **Use cases:**  
    * Online Transaction Processing (OLTP)
    * Data warehousing
    * IoT solutions
* **Limitaitions:**  
    * Not ideal for semi-structured or unstructured data.
    * Data migration can be challenging.
    * Limitations on data field lengths.

### NoSQL Databases
* **NoSQL:** Stands for "not only SQL", a non-relational database approach offering flexible schemas for diverse data types.
* **Popularity:** Driven by the rise of cloud computing, big data, and high-volume applications.
* **Key characteristics:** 
    * Schema-less or free-form data storage.
    * Handles structured, semi-structured, and unstructured data.
    * Doesn't always rely on SQL for querying.
* **Types of NoSQL databases:**  
    * **Key-value stores:** Store data as key-value pairs (e.g., Redis, Memcached).
    * **Document-based:** Store data in flexible documents (e.g., MongoDB, CouchDB).
    * **Columnd-based (Columnar):** Organize data in columns instead of rows (e.g., Cassandra, HBase).
    * **Graph:** Represent data as nodes and relationships (e.g., Neo4j, CosmosDB).
* **Advantages of NoSQL:** 
    * Handles large volumes of diverse data.
    * Scalability and performance in distributed systems.
    * Cost-effective and flexible architecture. 
* **Key differences from relational databases:**  
    * Flexible schemas vs. rigid schemas.
    * Cost-effective vs. expensive.
    * ACID compliance is not always supported in NoSQL.

### Data Marts, Data Lakes, ETL, and Data Pipelines
* **Data warehouse:** A central repository for structured, analysis-ready data, serving as a single source of truth for reporting and analysis.
* **Data mart:** A subset of data warehouse focused on a specific business function or user group.
* **Data lake:** A repository for storing raw, structured, semi-structured, and unstructured data in their native format, often used for advanced analytics and machine learning.
* **ETL (Extract, Transform, Load) process:**  
    * **Extract:** Gathers data from various sources.
    * **Transform:** Cleans, standardizes, and transforms data into a usable format.
    * **Load:** Loads processed data into a target repository (data warehourse, data lake, etc.)
* **Data pipelines:** Broader concept encompassing the entire data journey, including ETL, and can handle both batch and streaming data.

### Viewpoints: Considerations for Choice of Data Repository
* **Consider the use case:** Determine the purpose of the data repository (e.g., storing structured, semi-structured, or unstructured data).
* **Performance requirements:** Evaluate the needs for data at rest, streaming data, or data in motion, and any performance requirements.
* **Security and encryption:** Assess security needs and encryption requirements.
* **Data volume:** Determine the scale of data and if a big data system is necessary.
* **Storage and access patterns:** Consider storage requirements, update frequency, and access patterns (e.g., short intervals, long-running queries).
* **Compatibility:** Ensure compatibility with existing systems, programming languages, and tools.
* **Scalability:** Evaluate the ability of the repository to scale with the organization's needs.
* **Organizational standards:** Adhere to any organizational preferences or restrictions on data repositories.
* **Skills and cost:** Consider in-house expertise and the costs associated with different solutions.
* **Hosting platform:** Evaluate cloud-based options and their features.
* **Data structure and ingestion volume:** The type and structure of data, as well as the ingestion volume, influence the choice of repository.

### Data Integration Platforms
* **Data integration:** Combines data from various sources into a unified view for analysis and use.
* **Key aspects of data integration in data science:**  
    * Data access and extraction.
    * Data transformation and merging.
    * Data quality and governance.
    * Data delivery for analytics.
* **Relationship to ETL and data pipelines:**  
    * Data pipelines encompass the entire data movement process.
    * Data integration is a step within the data pipeline.
    * ETL is a process within data integration.
* **Capabilities of modern data integration platforms:**  
    * Pre-built connectors for various data sources.
    * Open-source architecture for flexibility.
    * Support for batch and streaming processing.
    * Big data integration.
    * Data quality, governance, and security features.
    * Portability for cloud and hybrid environments.
* **Data integration tools and platforms:**  
    * Commercial offerings from IBM, Talend, SAP, Oracle, etc.
    * Open-source frameworks like Dell Boomi and Jitterbit.
    * Cloud-based iPaaS (Integration Platform as a Service) solutions.

