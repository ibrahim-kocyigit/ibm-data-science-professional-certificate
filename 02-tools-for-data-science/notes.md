# TOOLS FOR DATA SCIENCE

## Table of Contents
1. [Module 1: Overview of Data Science Tools](#module-1)
2. [Module 2: Languages of Data Science](#module-2)
3. [Module 3: Packages, APIs, Data Sets, and Models](#module-3)
<br>

# Module 1: Overview of Data Science Tools <a name="module-1"></a>

## Data Science Tools

### Categories of Data Science Tools

#### Data Science Tasks:
* **Data Management:** This is like being a librarian for data. You need to know how to collect data from various data sources (databases, APIs, websites, etc.), store it safely and efficiently (in databases or other systems), and make sure you can access it quickly when needed. Think of it as organizing and maintaining a massive library of information.
* **Data Integration and Transformation:** This is where you take data from different sources and make it all work together. Imagine having puzzle pieces from different puzzles - you need to trim them, reshape them, and make sure they fit together to form a complete picture. This involves cleaning the data, converting it into a consistent format, and combining it in meaningful ways.
* **Data Visualization:** This is where you create charts, graphs, and other visuals to help people understand the data. Think of it as translating raw numbers into pictures that tell a story. A good visualization can reveal patterns and insights that would be difficult to see in a table of numbers.
* **Model Building:** This is where you use machine learning algorithms to find patterns in the data and make predictions. It's like teaching a computer to recognize patterns and make decisions based on what it learns. You might build a model to predict customer churn, detect fraud, or recommend products.
* **Model Deployment:** Once you've built a model, you need to make it available for others to use. This might involve creating an API (Application Programming Interface) that allows other applications to access your model and get predictions. It's like setting up a service that others can use to benefit from your model's capabilities.
* **Model Monitoring and Assessment:** After deploymen, you need to keep an eye on your model to make sure it's performing well. This involves tracking its accuracy, fairness, and robustness over time. You might need to retrain your model with new data or adjust its parameters to maintain its performance.

#### Tools for Data Science
* **Code Asset Management:** This is like using a special notebook for your code where you can track changes, collaborate with others, and revert to earlier versions if needed. Tools like Git and GitHub help you manage your code and work effectively in teams.
* **Data Asset Management:** This is about organizing and managing your data files (images, videos, text, etc.) in a central location. You might use a DAM (Digital Asset Management) platform to store, version, and share your data securely.
* **Development Environments:** These are like workshops for your code. They provide you with the tools and resources you need to write, test, and debug your code. Popular IDEs (Integrated Development Environments) include VS Code, PyCharm, and RStudio.
* **Execution Environments:** This is where your code actuall runs. It could be your local computer, a server, or a cloud-based platform. Cloud platforms like AWS, Azure, and GCP offer scalable execution environments for running data science workloads.

**Integrated tools:** Platforms like IBM Watson Studio provide a one-stop shop for many data science tasks. The combine data management, code management, development environments, and execution environments into a single platform.

### Open Source Tools for Data Science (Part 1)
* **Data management tools** are MySQL, PostgreSQL, MongoDB, Apache CouchDB, Apache Cassandra, Hadoop File System, Ceph, and elastic search.
* **Data integration and transformation tools** are Apache AirFlow, KubeFlow, Apache Kafka, Apache Nifi, Apache SparkSQL, and NodeRED. 
* **Data visualization tools** are Pixie Dust, Hue, Kibana, and Apache Superset.
* **Model development tools** are TensorFlow, PyTorch, Scikit-learn, XGBoost, LightGBM, MLflow, Kubeflow.
* **Model deployment tools** are Apache PredictionIO, Seldon, Kubernetes, Redhat OpenShift, Mleap, TensorFlow service, TensorFlow lite, and TensorFlow dot JS.
* **Model monitoring tools** are ModelDB, Prometheus, IBM AI Fairness 360, IBM Adversarial Robustness 360 Toolbox, and IBM AI Explainability 360.
* **Code asset management tools** are Git, GitHub, GitLab, and Bitbucket. 
* **Data asset management tools** are Apache Atlas, ODPi Egeria, and Kylo.

### Open Source Tools for Data Science (Part 2)
By understanding the strengths and weaknesses of the open-source tools, data scientists can choose the most suitable ones for their specific tasks and projects, enabling them to effectively analyze data, build models, and derive valuable insights.

* **Jupyter Notebooks and JupyterLab:**  
    * Jupyter Notebooks are popular for interactive programming, supporting many languages.
    * They combine code, output, visualization, and documentation in a single document.
    * JupyterLab is the next-generation version, offering a more modern and modular interface with enhanced file management capabilities.
* **Apache Zeppelin:**  
    * Similar to Jupyter Notebooks but with integrated plotting capabilities that don't require coding.
    * Can be extended with additional libraries for more advanced functionalities.
* **RStudio:**  
    * A dedicated IDE for R, providing a comprehensive environment for programming, execution, debugging, data access, exloration, and visualization.
    * While focused on R, it also allows Python development and integrates well with Jupyter.
* **Spyder:**  
    * A Python-focused IDE inspired by RStudio, offering a similar interface and features.
    * While not as feature-rich as RStudio, it's a viable alternative for data scientists who prefer Python.
* **Cluster Execution Environments:**  
    * **Apache Spark:** A powerful engine for distributed data processing, known for its linear scalability and ability to handle large datasets. Primarily a batch processing engine, but also supports stream processing.
    * **Apache Flink:** A stream processing engine designed for real-time data analysis, but also supports batch processing.
    * **Ray:** Focuses on large-scale deep learning model training and distributed computing.
* **Visual Data Science Tools:**  
    * **KNIME:** A visual platform for data integration, transformation, visualization, and model building with drag-and-drop functionality and extensibility through R and Python.
    * **Orange:** User-friendly visual tool with a focus on ease of use, offering data mining and machine learning capabilities.

### Commercial Tools for Data Science
* Commercial tools support the most common tasks in data science.
* **Data management tools** are Oracle Database, Microsoft SQL Server, and IBM Db2.
* **Data integration tools** are mainly provided by Informatica PowerCenter, IBM InfoSphere DataStage. These are followed by products from SAP, Oracle, SAS, Talend, Microsoft, and Watson Studio Desktop,.
* **Model building tools** are SPSS Modeler, and SAS enterprise miner. SPSS Modeler is also available in Watson Studio Desktop.
* **Dataset management tools** are provided by Informatica and IBM.
* For **model monitoring** and **code asset management** open-source tools are used.

### Cloud Based Tools for Data Science
* Watson Studio, together with Watson Open Scale is a fully integrated tool covering the data science life cycle.
* In data management, with some exceptions, there exist a software-as-a-service (SaaS) version of existing open source and commercial tools
* Two commercial data integration tools widely used are Informatica Cloud Data Integration and IBM's Data Refinery
* An example of a cloud-based data visualization tool is Datameer and IBM's Congos Business intelligence suit.
* Model building can be done using a service such as Watson Machine Learning.
* Amazon SageMaker Model Monitor is an example of a cloud tool to monitor deployed machine learning and deep learning models continuously.

# Module 2: Languages of Data Science <a name="module-2"></a>

## Languages of Data Science

### Languages of Data Science
* You should select a language to learn depending on your needs, the problems you are trying to solve, and who you are solving them for.
* The problems you need to solve can be related to your company, role, and age of the existing application.
* The popular languages in data science are Python, R, SQL, Scala, Java, C++
* JavaScript, PHP, Go, Ruby, and Visual Basic all have their own unique use cases as well.

### Introduction to Python

#### Python's popularity:
Python is the most widely used language in data science, with the majority of data scientist using it regularly and a large percentage of data science job descriptions requiring it.

##### Benefits of using Python:
* **Clear and readable syntax:** Makes it easy to learn and understand, even for beginners.
* **Extensive libraries:** Provides a wide range of tools for various tasks, including data science, AI, web development, and IoT.
* **Large and supportive community:** Offers sample resources, documentation, and support for learners and users.
* **Versatility:** Can be used for a wide range of applications, from data analysis and machine learning to web development and scripting.

#### Python for data science:
* **Scientific computing libraries:** Pandas (data manipulation), NumPy (numerical computation), SciPy (scientific computing), and Matplotlib (data visualization) are essential tools for data scientists.
* **AI and machine learning libraries:** TensorFlow, PyTorch, Keras, and scikit-learn provide powerful frameworks for building and training machine learning models.
* **Natural Language Processing (NLP):** NLTK (Natural Language Learning Toolkit) enables text analysis and natural language understanding.

#### Diversity and inclusion:
* The Python community is known for its strong emphasis on diversity and inclusion.
* The Python Software Foundation has a code of conduct to ensure safe and inclusive online and in-person communities.
* Groups like PyLadies promote the participation of women in the Python open-source community.

### Introduction to R Language

#### Open source vs. Free software
* **Similarities:** Both are free to use, often use the same licences (e.g., GNU), and support collaboration.
* **Differences:** Open source is championed by the Open Source Initiative (OSI) and is more business focused, while free software is defined by the Free Software Foundation (FSF) and emphasizes user freedom and ethical values.

#### Why use R?
* **Free software:** Allows for private, commercial, and collaborative use, promoting freedom and flexibility.
* **Widely used in academia and industry:** Popular among statisticians, mathematicians, and data miners for statistical software development, graphing, and data analysis.
* **Array-oriented syntax:** Makes it easier to translate mathematical concepts into code, especially for those with limited programming experience.
* **Extensive package repository:** Offers over 15,000 packages for various statistical and data analysis tasks.
* **Integration with other languages:** Can be integrated with C++, Java, Python, and others.
* Strong object-oriented programming:** Provides advanced object-oriented programming capabilities compared to other statistical computing languages.

### Introduction to SQL
**SQL (Structured Query Language)** is a non-procedural language specifically designed for managing and querying data in relational databases. It's not a full-fledged data science language like Python or R, but it's an essential tool for data scientists.

#### Key characteristics of SQL:
* Focuses on data management and retrieval.
* Used for working with structured data in relational databases (organized in tables with rows and columns).
* Can also be used with some NoSQL and big data repositories through SQL-like interface.

#### SQL elements:
* **Clauses:** Part of a query that specify conditions or actions (e.g., `WHERE`, `ORDER_BY`).
* **Expressions:** Combinations of values, operators, and functions that result in a single value.
* **Predicates:** Expressions that evaluate to true or false, used in conditions.
* **Queries:** Requests for data retrieval from a database.
* **Statements:** Complete instructions that perform actions on the database (e.g., `SELECT`, `INSERT`,  `UPDATE`, `DELETE`)

#### Benefits of using SQL:
* Essential for data science roles involving data analysis, data engineering, and working with databases.
* Enables direct data access, improving workflow efficiency.
* Acts as an intermediary between the user and the database.
* ANSI standard, making it transferable across different database systems.

**Popular SQL databases** are MySQL, IBM DB2, PostgreSQL, SQLite, Oracle, Microsoft SQL Server.

### Other Languages for Data Science
By understanding the applications and strengths of these languages, data scientists can expand their toolkit and choose the most suitable language for specific tasks and projects, ranging from building high-performance applications to developing web-based data science tools.

#### Java:
* A mature, object-oriented language widely used in enterprise applications.
* Known for its speed and scalability.
* Used in data science tools like Weka (data mining), Java-ML (machine learning), Apache MLlib (scalable machine learning), and Deeplearning4j (deep learning).
* Also used to build big data platforms like Hadoop.

#### Scala
* A general purpose language that combines object-oriented and functional programming paradigms.
* Designed to address some limitations of Java while remaining interoperable with it.
* Known for its sxalability and expressiveness.
* Widely used in data science for building distributed systems like Apache Spark (a fast and general purpose cluster computing system).

#### C++
* A high-performance language often used for developing core components of data science applications where speed and control are crucial.
* Used to build tools like TensorFlow (deep learning), MongoDB (NoSQL database), and Caffe (deep learning framework).

#### JavaScript
* Primarily know for web development, but also used in data science through libraries like TensorFlow.js (brings machine learning to the browser and Node.js).
* Other JavaScript based data science tools include brain.js and machinelearn.js
* R-js is a project that aims to bring O's functionalities to the JavaScript ecosystem.

#### Julia 
* A high-performance language specifically designed for numerical and scientific computing.
* Offers a balance of development speed and execution speed.
* Can call libraires from other languages (C, Python, R, etc.)
* Used in data science for tools like JuliaDB (for working with large datasets.)

# Module 3: Packages, APIs, Data Sets, and Models <a name="module-3"></a>