# TOOLS FOR DATA SCIENCE

## Table of Contents
1. [Module 1: Overview of Data Science Tools](#module-1)
2. [Module 2: Languages of Data Science](#module-2)
3. [Module 3: Packages, APIs, Data Sets, and Models](#module-3)
4. [Module 4: Jupyter Notebooks and JupyterLab](#module-4)
5. [Module 5: RStudio and GitHub](#module-5)



# Module 1: Overview of Data Science Tools <a name="module-1"></a>

## Data Science Tools

### Categories of Data Science Tools

#### Data Science Tasks:
* **Data Management:** This is like being a librarian for data. You need to know how to collect data from various data sources (databases, APIs, websites, etc.), store it safely and efficiently (in databases or other systems), and make sure you can access it quickly when needed. Think of it as organizing and maintaining a massive library of information.
* **Data Integration and Transformation:** This is where you take data from different sources and make it all work together. Imagine having puzzle pieces from different puzzles - you need to trim them, reshape them, and make sure they fit together to form a complete picture. This involves cleaning the data, converting it into a consistent format, and combining it in meaningful ways.
* **Data Visualization:** This is where you create charts, graphs, and other visuals to help people understand the data. Think of it as translating raw numbers into pictures that tell a story. A good visualization can reveal patterns and insights that would be difficult to see in a table of numbers.
* **Model Building:** This is where you use machine learning algorithms to find patterns in the data and make predictions. It's like teaching a computer to recognize patterns and make decisions based on what it learns. You might build a model to predict customer churn, detect fraud, or recommend products.
* **Model Deployment:** Once you've built a model, you need to make it available for others to use. This might involve creating an API (Application Programming Interface) that allows other applications to access your model and get predictions. It's like setting up a service that others can use to benefit from your model's capabilities.
* **Model Monitoring and Assessment:** After deployment, you need to keep an eye on your model to make sure it's performing well. This involves tracking its accuracy, fairness, and robustness over time. You might need to retrain your model with new data or adjust its parameters to maintain its performance.

#### Tools for Data Science
* **Code Asset Management:** This is like using a special notebook for your code where you can track changes, collaborate with others, and revert to earlier versions if needed. Tools like Git and GitHub help you manage your code and work effectively in teams.
* **Data Asset Management:** This is about organizing and managing your data files (images, videos, text, etc.) in a central location. You might use a DAM (Digital Asset Management) platform to store, version, and share your data securely.
* **Development Environments:** These are like workshops for your code. They provide you with the tools and resources you need to write, test, and debug your code. Popular IDEs (Integrated Development Environments) include VS Code, PyCharm, and RStudio.
* **Execution Environments:** This is where your code actual runs. It could be your local computer, a server, or a cloud-based platform. Cloud platforms like AWS, Azure, and GCP offer scalable execution environments for running data science workloads.

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
    * A dedicated IDE for R, providing a comprehensive environment for programming, execution, debugging, data access, exploration, and visualization.
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
* **Similarities:** Both are free to use, often use the same licenses (e.g., GNU), and support collaboration.
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
* Known for its scalability and expressiveness.
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
* Can call libraries from other languages (C, Python, R, etc.)
* Used in data science for tools like JuliaDB (for working with large datasets.)

# Module 3: Packages, APIs, Data Sets, and Models <a name="module-3"></a>

## Libraries, APIs, Datasets and Models

### Libraries for Data Science
By understanding the capabilities of these libraries, data scientists can leverage pre-built functions and tools to efficiently perform various tasks, from data cleaning and manipulation to building and deploying complex machine learning models.

#### Scientific Computing Libraries in Python
* **Pandas:** Provides data structures (like DataFrames) and tools for data manipulation, cleaning, and analysis. It's essential for working with structured data in Python.
* **NumPy:** The foundation for numerical computing in Python. It provides tools for working with arrays and matrices, enabling efficient mathematical operations.

#### Visualization Libraries in Python
* **Matplotlib:** A versatile library for creating various types of plots and charts. It's highly customizable and widely used for data visualization in Python.
* **Seaborn:** Built on top of Matplotlib, Seaborn provides a higher-level interface for creating statistically informative and visually appealing plots like heat maps, time series, and violin pilots.

#### Machine Learning and Deep Learning Libraries in Python
* **Scikit-learn:** A comprehensive library for various machine learning tasks, including classification, regression, clustering, dimensionality reduction, and model selection. It's user-friendly and widely used for building and evaluating models.
* **Keras:** A high-level API for building and training deep learning models. It's know for its simplicity and ease of use, making it suitable for beginners.
* **TensorFlow:** A powerful and versatile library for numerical computation, particularly well-suited for large-scale machine learning and deep learning. It's often used for production and deployment of models.
* **PyTorch:** Another popular deep learning framework known for its dynamic computation graph and flexibility. It's favored by researchers for its ease of use and intuitive interface. 

#### Other Languages and Libraries
* **Apache Spark:** A distributed computing framework that provides libraries for data manipulation, machine learning, and graph processing. It supports Python, R, Scala, and SQL.
* **Scala libraries:** Vegas (for data visualization) and Big DL (for deep learning) are example of Scala libraries in data science.
* **R Libraries:** ggpolot2 (for data visualization) is a popular R library. R also has interfaces to Keras and TensorFlow for deep learning.

### Application Programming Interfaces (APIs)
An **Application Programming Interface (API)** is a way for different software applications to communicate with each other. Think of it as a waiter in the restaurant. You tell the waiter what you want (the request), they communicate that to the kitchen (the back-end), and then bring you your food (the response). You don't need to know how the kitchen works, just how to interact with the waiter.

#### API libraries
* **Pandas API:** Allows you to work with data structures and perform data manipulation tasks in Python without needing to know the underlying implementation details.
* **TensorFlow API:** Provides interfaces for various programming languages (Python, JavaScript, C++, R, etc.) to interact with the TensorFlow library for machine learning.

#### REST APIs (Representational State Transfer)
A type of API that uses the internet to communicate between a client (your program) and a web service (the resource).

**Key concepts:** 
* **Client:** The program making the request.
* **Resource:** The web service providing data or functionality.
* **Endpoint:** The specific URL used to access the resource.
* **Request:** The input sent to the resource.
* **Response:** The output received from the resource.

**HTTP Methods:** Rest APIs use HTTP methods like `GET`, `POST`, `PUT`, and `DELETE` to perform actions on the resource.

**JSON (JavaScript Object Notation):** Often used to structure data in requests and responses.

**Example of REST APIs:**
* **Watson Speech-to-Text API:** Converts spoken audio into written text.
* **Watson Language Translator API:** Translates text from one language to another.

### Datasets: Powering Data Science
A **dataset** is a structured collection of data, which can be tabular (like a spreadsheet), hierarchical, network-based or even raw files (images, audio, video).

By understanding the concepts of datasets, data ownership, and licensing, data scientists can effectively utilize open data for research, analysis, and model building while adhering to ethical and legal considerations.

#### Data ownership:
* **Private datasets:** Contain sensitive or proprietary information and are not publicly shared. 
* **Open data:** Publicly available datasets from various sources (governments, organization, companies) that can be freely used and analyzed. Open data is crucial for the growth and development of data science. Open datasets may not always be suitable for enterprise use due to potential business implications.

#### Sources of open data
* Governmental and intergovernmental organizations (UN, EU, etc.)
* Data portals (e.g., Open Knowledge Foundations's datacatalogs.org)
* Online communities (e.g., Kagge)
* Search engines (e.g., Google Dataset Search)

#### Community Data License Agreement (CDLA)
* Created by the Linux Foundation to address licensing issues specific to datasets. The CDLA makes it easier to share and use open data while respecting creator's rights.
* **CDLA-Sharing:** Allows use and modification of data, but requires sharing modified versions under the same license.
* **CDLA-Permissive:** Allow use and modification without requiring sharing of changes.
* **Important note:** Neither license restricts the sharing or licensing the results derived from the data (e.g., machine learning models).

### Additional Sources of Datasets
#### Government Data:
* https://www.data.gov/
* https://www.census.gov/data.html
* https://data.gov.uk/
* https://www.opendatanetwork.com/
* https://data.un.org/

#### Financial Data Sources:
* https://data.worldbank.org/
* https://www.globalfinancialdata.com/
* https://comtrade.un.org/
* https://www.nber.org/
* https://fred.stlouisfed.org/

#### Crime Data:
* https://www.fbi.gov/services/cjis/ucr
* https://www.icpsr.umich.edu/icpsrweb/content/NACJD/index.html
* https://www.drugabuse.gov/related-topics/trends-statistics
* https://www.unodc.org/unodc/en/data-and-analysis/

#### Health Data:
* https://www.who.int/gho/database/en/
* https://www.fda.gov/Food/default.htm
* https://seer.cancer.gov/faststats/selections.php?series=cancer
* https://www.opensciencedatacloud.org/
* https://pds.nasa.gov/
* https://earthdata.nasa.gov/
* https://www.sgim.org/communities/research/dataset-compendium/public-datasets-topic-grid

#### Academic and Business Data:
* https://scholar.google.com/
* https://nces.ed.gov/
* https://www.glassdoor.com/research/
* https://www.yelp.com/dataset

#### Other General Data:
* https://datacatalogs.org/
* https://datasetsearch.research.google.com/
* https://www.kaggle.com/datasets
* https://www.reddit.com/r/datasets/

#### Dataset licenses
When you select a dataset, it is necessary to look into the license. A license explains whether you can use that dataset or not; or explains if you have to accept certain guidelines to use that dataset. The different license types are listed below.

1. **PUBLIC DOMAIN MARK - PUBLIC DOMAIN**  
When a dataset has a Public Domain license, all the rights to use, access, modify and share the dataset are open to everyone. Here there is technically no license.

2. **OPEN DATA COMMONS PUBLIC DOMAIN DEDICATION AND LICENSE – PDDL**  
Open Data Commons license has the same features as the Public Domain license, but the difference is the PDDL license uses a licensing mechanism to give the rights to the dataset.

3. **CREATIVE COMMONS ATTRIBUTION 4.0 INTERNATIONAL CC-BY** 
This license allows users to share and modify a dataset, but only if they give credit to the creator(s) of the dataset.

4. **COMMUNITY DATA LICENSE AGREEMENT – CDLA PERMISSIVE-2.0**  
Like most open-source licenses, this license allows users to use, modify, adapt, and share the dataset, but only if a disclaimer of warranties and liability is also included.

5. **OPEN DATA COMMONS ATTRIBUTION LICENSE - ODC-BY**  
This license allows users to share and adapt a dataset, but only if they give credit to the creator(s) of the dataset.

6. **CREATIVE COMMONS ATTRIBUTION-SHAREALIKE 4.0 INTERNATIONAL - CC-BY-SA**  
This license allows users to use, share, and adapt a dataset, but only if they give credit to the dataset and show any changes or transformations, they made to the dataset. Users might not want to use this license because they have to share the work they did on the dataset.

7. **COMMUNITY DATA LICENSE AGREEMENT – CDLA-SHARING-1.0**  
This license uses the principle of ‘copyleft’: users can use, modify, and adapt a dataset, but only if they don’t add license restrictions on the new work(s) they create with the dataset.

8. **OPEN DATA COMMONS OPEN DATABASE LICENSE - ODC-ODBL**  
This license allows users to use, share, and adapt a dataset but only if they give credit to the dataset and show any changes or transformations they make to the dataset. Users might not want to use this license because they have to share the work they did on the dataset.

9. **CREATIVE COMMONS ATTRIBUTION-NONCOMMERCIAL 4.0 INTERNATIONAL - CC BY-NC**  
This license is a restrictive license. Users can share and adapt a dataset, provided they give credit to its creator(s) and ensure that the dataset is not used for any commercial purpose.

10. **CREATIVE COMMONS ATTRIBUTION-NO DERIVATIVES 4.0 INTERNATIONAL - CC BY-ND**  
This license is also a restrictive license. Users can share a dataset if they give credit to its creator(s). This license does not allow additions, transformations, or changes to the dataset.

11. **CREATIVE COMMONS ATTRIBUTION-NONCOMMERCIAL-SHAREALIKE 4.0 INTERNATIONAL - CC BY-NC-SA**  
This license allows users to share a dataset only if they give credit to its creator(s). Users can share additions, transformations, or changes to the dataset, but they cannot use the dataset for commercial purposes.

12. **CREATIVE COMMONS ATTRIBUTION-NONCOMMERCIAL-NODERIVATIVES 4.0 INTERNATIONAL - CC BY-NC-ND**  
This license allows users to share a dataset only if they give credit to its creator(s). Users are not allowed to modify the dataset and are not allowed to use it for commercial purposes.

### Sharing Enterprise Data - Data Asset eXchange
**IBM Data Asset Exchange (DAX)** is a curated repository of open datasets provided by IBM, offering high quality data with clear licensing terms (CDLA): https://developer.ibm.com/feeds/data-asset-exchange/data/

Notebooks from DAX can be downloaded, but also can be easily loaded and executed in Watson Studio. Users can perform data analysis, build models, and create visualizations within Watson Studio.

#### Benefits of using DAX
* **Access to unique datasets:** Provides access to a variety of datasets, including images, video, text, and audio, from IBM Research and trusted third-party sources.
* **Enterprise-ready data:** Datasets are curated and prepared for use in enterprise applications.
* **Tutorial notebooks:** Includes notebooks that guide users through data cleaning, preprocessing, and exploratory analysis.
* **Advanced notebooks:** Some datasets have notebooks demonstrating more complex tasks like machine learning, deep learning integration, and statistical analysis.
* **Simplified access:** Offers a single platform to access and explore diverse datasets.

### Machine Learning Models - Learning from Models to Make Predictions
By understanding the different types of machine learning models and the steps involved in building and deploying them, data scientists can effectively leverage these powerful tools to solve a wide range of real-world problems.

**Machine Learning Model** is an algorithm that learns patterns from data to make predictions or decisions. It's like a student who learns from examples and then applies that knowledge to solve new problems.

**Model Training** is the process of "teaching" the model by feeding it data and letting it learn the patterns.

#### Types of machine learning
* **Supervised Learning:** The model learns from labeled data (input-output pairs), like a student learning with a teacher and answer key.
    * **Regression:** Predicts a numerical value (e.g., house price).
    * **Classification:** Predicts a category or class (e.g., spam or not spam)
* **Unsupervised Learning:** The model learns from unlabeled data, finding patterns and structures on its own, like a detective analyzing clues to solve a case.
    * **Clustering:** Groups similar data points together (e.g., customer segmentation).
    * **Anomaly detection:** Identifies unusual or outlier data points (e.g., fraud detection)
* **Reinforcement Learning:** The model learns through trial and error, receiving rewards for correct actions and penalties for incorrect ones, like a mouse learning to navigate a maze.

#### Deep Learning
**Deep learning** is a specialized type of machine learning that uses artificial neural networks to simulate human-like learning. 

* Is used for complex tasks like image recognition, natural language processing, and time series forecasting.
* Requires large datasets and significant computing power.
* Can be built from scratch or using pre-trained models from model zoos (e.g., TensorFlow, PyTorch)

#### Building a machine learning model example
1. **Collect and prepare data:** Gather and label the data (e.g., images with objects labeled).
2. **Choose or build a model:** Select a pre-trained model or create a new one.
3. **Train the model:** Feed the labeled data to the model and let it learn.
4. **Analyze and refine:** Evaluate the model's performance and repeat steps 3 and 4 until satisfactory.
5. **Deploy the model:** Make the trained model available for use in applications.

### The Model Asset eXchange
The **Model Asset eXchange (MAX)** is a free, open-source repository provided by IBM that offers pre-trained and customizable deep learning models as microservices.

#### Benefits of using MAX
* **Reduced time to value:** Leveraging pre-trained models eliminates the need to train models from scratch, saving significant time and resources.
* **Ready-to-use microservices:** Models are packaged as microservices with pre- and post-processing code and a standardized API for easy integration into applications.
* **Open-source licenses:** Models are available under permissive licenses, allowing for personal and commercial use.
* **Diverse model domains:** Covers various domains, including object detection, image classification, natural language processing, and more.

#### Components of a model-serving microservice
* Pre-trained deep learning model
* Input pre-processing code
* Output post-processing code
* Standardized API for application access

#### Deployment and Customization
* Microservices are distributed as Docker images, making them easy to deploy and manage.
* Docker image source code is available on GitHub for customization.
* Kubernetes (and platforms like Red Hat OpenShift) can be used to automate deployment, scaling, and management of the microservices.

# Module 4: Jupyter Notebooks and JupyterLab <a name='module-4'></a>

## Jupyter Notebooks and Jupyter Lab
By understanding the capabilities and usage of Jupyter Notebooks and JupyterLab, data scientists can effectively document their work, experiment with code, visualize results, and collaborate with others, making it an essential tool for data science projects.

### Introduction to Jupyter Notebooks
**Jupyter Notebook** is an interactive, browser-based tool that allows you to combine code, visualizations, equations, and narrative text in a single document. It's like a digital lab notebook for scientists, where they can experiment, document their work, and share their findings.

#### Key features of Jupyter notebooks:
* Combines code, output, and descriptive text in one file.
* Supports various programming languages (Python, R, Julia, etc.)
* Allows for interactive execution of code and visualization results.
* Facilitates sharing and collaboration.

**JupyterLab** is the next-generation user interface for Jupyter notebooks, offering a more flexible and extensible environment.

#### Key features of JupyterLab
* Work with multiple notebooks, code files, and data files simultaneously.
* Integrates with various tools and extensions.
* Supports different file formats (CSV, JSON, PDF, etc.)
* Provides a more modern and user-friendly interface.

#### Using Jupyter notebooks:
* **Cloud-based services:** Platforms like IBM Watson Studio and Google Colab offer hosted Jupyter Notebook environments, eliminating the need for local installation.
* **Local installation:** Jupyter Notebooks can be installed locally using pip or Anaconda.
* **Skills Network Labs:** Provides a hosted JupyterLab environment for this course, allowing you to complete hands-on labs without local installation.

### Getting Started with Jupyter
By mastering these basic operations in Jupyter Notebooks, you can efficiently write and execute code, organize your work, create presentations, and manage your notebook sessions, making your data science workflow smoother and more productive.

#### Running Code
* You can run individual code cells by selecting the cell and clicking the "Run" button or using the shortcut `Shift + Enter`.
* To run all cells in the notebook, use the "Run All Cells" option in the "Run" menu.

#### Inserting and Deleting Cells:
* Insert new cells by clicking the "+" button in the toolbar.
* Delete cells by selecting the cell and clicking "Edit" -> "Delete Cells" or pressing the "D" key twice.

#### Working with Multiple Notebooks:
* Open new notebooks by clicking the "+" button and selecting the desired file or using the "File" menu.
* Arrange notebooks side-by-side or in tabs for easier comparison and interaction.

#### Presenting Notebooks:
* Use Markdown cells to add headings, text descriptions, and structure to your notebook.
* Create presentations by converting code cells and their outputs into slides and sub-slides.
* This allows you to effectively communicate your code, visualizations, and findings.

#### Shutting Down Notebooks:
* Click the "stop" icon (square icon) in the sidebar to shut down a notebook's kernel (its computational engine).
* This releases resources and ensures the notebook is no longer active.
* You can shut down individual notebooks or terminate all sessions at once.

### Jupyter Kernels
**Kernel** is the computational engine that executes the code within a Jupyter Notebook. Think of it as the "brain" of the notebook that understands and runs your code.

**Language Support:** Jupyter supports various programming languages through kernels. This means you can use languages like Python, R, Julia, and others within the same Jupyter environment.

**Kernel Startup** When you open a Jupyter Notebook, the associated kernel for the chosen language starts automatically.

**Code Execution:** When you run a code cell in the notebook, the kernel processes the code and produces the results.

**Kernel Selection:** You can choose the kernel when creating a new notebook or switch between kernels in an existing notebook. In Skills Network Labs, several kernels (Python, Apache, Julia, R, Swift) are pre-installed. For local installations, you might need to install kernels for specific languages manually.

### Jupyter Architecture
Jupyter uses a **two-process model** consisting of a **kernel** and a **client**.
* The **client** is the user interface (your web browser) where you write and execute code.
* The **kernel** is a separate process that runs the code and returns the results to the client.

#### Components of Jupyter architecture
* **Client (Browser):** The interface where you interact with the notebook.
* **Notebook Server:** Handles saving and loading notebooks, managing kernels, and other backend tasks.
* **Kernel:** Executes the code in the notebook cells and returns the output.
* **Notebook file (ipynb):** Stores your code, metadata, content, and outputs in a JSON format.

#### File conversion with NBConvert
Jupyter uses the NBConvert tool to convert notebooks into other formats. (e.g., HTML, PDF)

The conversion process involves:
* **Preprocessor:** Modifies the notebook before conversion.
* **Exporter:** Converts the notebook into the target format.
* **Postprocessor:** Performs final adjustments on the exported file.

### Additional Anaconda Jupyter Environments
* **Anaconda:** A free and open-source distribution of Python and R, widely used in data science and machine learning. It simplifies package management and deployment and includes a suite of tools for data science tasks.
* **Anaconda Navigator:** A graphical user interface (GUI) included in Anaconda that allows users to easily manage packages, environments, and launch applications like JupyterLab and VS Code.
* **JupyterLab:** 
    * A web based interactive development environment for Jupyter Notebooks, offering a more modern and extensible interface compared to the classic Jupyter Notebook.
    * Comes pre-installed with Anaconda and includes popular data science libraries like NumPy, Pandas, and Matplotlib.
* **VS Code (Visual Studio Code):** 
    * A free and open-source code editor that supports various programming languages and offers features like debugging, task running, and extensions for enhanced functionality.
    * Can be launched from Anaconda Navigator or installed separately.
    * Requires additional extensions to be configured for PYthon and Jupyter Notebooks.

### Additional Cloud Based Jupyter Environments
**Cloud-based Jupyter environments** are online platforms that host Jupyter Notebooks, allowing you to access and run them without any local installation. They often provide additional features like collaboration, sharing, and access to powerful computing resources.

#### JupyterLite
* A lightweight version of JupyterLab that runs entirely on your web browser.
* No need for a server, it can be deployed as a static website.
* Supports interactive visualizations and common visualization libraries (Altair, Plotly, etc.)
* Includes the lates JupyterLab features and improvements.
* Uses Python kernels like Pyodide (for running Python in the browser) and Pyolite (optimized for faster execution)

#### Google Colab
* A free cloud-based Jupyter environment provided by Google.
* Notebooks run in the browser, and projects can be stored on Google Drive and GitHub.
* Offers easy sharing and collaboration features.
* Comes with pre-installed machine learning and visualization libraries (scikit-learn, matplotlib, etc.).
* Enables quick development and experimentation with data science applications.

### Jupyter Notebooks on the internet
There are thousands of interesting Jupyter Notebooks available on the internet for you to learn from. One of the best sources is: https://github.com/jupyter/jupyter/wiki

# Module 5: RStudio and GitHub <a name="module-5"></a>

## RStudio IDE

### Introduction to R and RStudio

#### R Language
R is a powerful statistical programming language widely used in academia, healthcare, and government for data analysis, statistical inference, and machine learning.

**Capabilities of R:**  
* Data import from various sources (flat files, databases, statistical software)
* Easy-to-use functions for data manipulation and analysis
* Strong data visualization capabilities
* Extensive packages for advanced statistical modelling and machine learning

#### RStudio
RStudio is a popular integrated development environment (IDE) that enhances productivity when working with R.

**Key features of RStudio:**  
* Syntax-highlighting editor for writing and executing code.
* Console for interactive command execution.
* Workspace and History tabs to track objects and commands.
* Files, Plots, Packages, and Help tabs for managing files, visualizations, libraries, and documentation.

#### Popular R libraries for data science
* **dplyr:** Provides a grammar of data manipulation, making it easier to work with data frames.
* **stringr:** Offers tools for string manipulation and processing.
* **ggplot2:** A powerful and versatile library for creating high-quality data visualizations.
* **care:** Simplifies the process of training and evaluating machine learning models.

### Plotting in RStudio

#### R Data Visualization Packages:
* **ggplot2:** A versatile and widely used package for creating various types of plots and charts, known for its layered approach to visualization.
* **plotly:** Creates interactive, web-based visualizations that can be embedded in web pages or saved as HTML files.
* **lattice:** A high-level graphics package for visualizing multivariate data, often used for creating trellis plots.
* **leaflet:** Creates interactive maps and geospatial visualizations.

#### Inbuilt R Plot Function:
* R provides a basic `plot()` function for creating simple scatterplots.
* You can customize the plot by adding lines `(type="l")` and titles `(main="Title")`.

#### ggplot2 Library:
* Offers a more powerful and flexible way to create visualizations.
* Uses a "grammar of graphics" approach, allowing you to build plots layer by layer.
* `ggplot()` function initializes the plot, and `geom_point()` adds data points as a scatterplot.
* `ggtitle()` adds a title to the plot.
* `labs()` customizes axis labels and other plot elements.

#### GGally Extension:
* Extends ggplot2 with additional functions to simplify complex visualizations and analysis.
* Provides tools for creating scatterplot matrices, parallel coordinate plots, and other advanced visualizations.

## GitHub

### Overview of Git/GitHub

#### Version Control
**Version control** is a system that tracks changes to files over time, allowing you to revert to previous versions, collaborate with others, and manage different versions of your project. Think of it like having a "time machine" for your files.

#### Git
**Git** is a free and open-source distributed version control system. "Distributed" means that every developer has a complete copy of the project history on their local machine, enabling offline work and flexible collaboration.

#### GitHub
**GitHub** is a popular web-based platform that provides hosting for Git repositories. It offers tools for collaboration, code review, issue tracking, and project management.

#### Key Git/GitHub terminology:
* **SSH:** A secure protocol for remote login and communication.
* **Repository:** A directory containing your project files and the history of changes.
* **Fork:** A copy of a repository, allowing you to experiment with changes without affecting the original.
* **Pull request:** A request to merge your changes into another branch or repository, initiating a code review process.
* **Working directory:** The current state of your project files on your local machine.

#### Essential Git commands:
* `git init`: Initializes a new Git repository.
* `git add`: Stages changes for commit.
* `git status`: Shows the status of your working directory and stated changes
* `git commit`: Saves a snapshot of your changes with a message
* `git reset`: Undoes changes
* `git log`: Shows the history of communities
* `git branch`: Creates or lists branches
* `git checkout`: Switches between branches
* `git merge`: Combines changes from different branches

### Introduction to GitHub

#### Source Repositories
Centralized storage locations for managing and tracking changes to files, especially source code during software development. They help maintain version history, facilitate collaboration, and ensure code integrity.

#### Key characteristics of Git
* Strong support for non-linear development
* Distributed development, allowing each developer to have a local copy of the entire project history.
* Compatibility with existing systems and protocols.
* Efficient handling of large projects.
* Cryptographic authentication of history to ensure data integrity.
* Flexible merge strategies for handling complex code integrations.

#### GitHub
A web-based hosting service for Git repositories, providing a platform for collaboration, code review, and project management.

#### Benefits of using GitHub
* Centralized platform for managing Git repositories.
* Facilitates collaboration among developers through features like pull requests, code reviews, and issue tracking.
* Offers various account types (free, professional, enterprise) to cater to different needs.
* Provides a user-friendly interface for interacting with Git repositories.



