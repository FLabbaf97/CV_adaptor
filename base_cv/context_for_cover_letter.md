Here you can find context about my motivation, my transferable skills, and some of the projects I have worked on during my master's and professional roles. You can use anything you want for motivation letter / cover letter.

## Reflection about myself

I consider myself a versatile ML engineer and software developer who has worked with ML/AI for several years, most of which is within healthcare, med-tech, and biological environments. I also have a solid software engineering background from earlier roles in mobile and DevOps. I have a Bachelor's degree in Computer Science and a Master's focused on computational biology. In my master's degree I became familiar with a diverse range of biological data and worked with bioinformatics tools, multi-omics data, biological images, and graphs, which built the foundation for me to work in multidisciplinary teams.

In my work experience, I learned about regulated medical software development and became more interested in regulated AI. I also learned about medical device software standards including ISO 13485, IEC 62304, and ISO 14971. More recently, I have applied LLMs not only inside ML products (e.g. speech post-processing, experiment automation) but also in how I build software—through AI-assisted development workflows, reusable agent rules, and configuration-driven ML infrastructure that keeps experimentation reproducible and auditable. I've gained hands-on experience with AI agents and Model Context Protocol (MCP) for building intelligent automation systems, and I continue to explore how these emerging technologies can enhance software development productivity while maintaining code quality and traceability.

I worked in academic labs, companies, and fast-paced startups, which allowed me to experience a diverse range of working environments and cultures. My experience in startups allowed me to develop a strong sense of ownership and responsibility. I learned about the importance of delivering value to the company and the impact of my work on the business. I also learned about the importance of collaboration and communication with different stakeholders. I have experience working in interdisciplinary teams and I am comfortable communicating complex technical concepts to non-technical stakeholders. I am also a strong team player and I believe that effective collaboration is essential for the success of any project.

**Ideal working environment.** I am highly interested (but not limited) in working within healthcare and med-tech companies where I can apply my technical skills and contribute to the team. I also like to work in fast-paced startups, research groups, and R&D teams where I can learn about the business and the impact of my work. I am also interested in working in a mission-driven company where I can make a difference. Roles that combine production ML, LLM integration, and rigorous software engineering—especially in regulated or high-stakes domains—are a strong fit for me. I'm particularly excited about positions involving AI system design, orchestrating AI agents, building MCP-based integrations, and developing RAG systems, as these represent the cutting edge of AI engineering where I can continuously learn and contribute.

---

# Some of my work experience

## ML Engineer at Precise Health SA

**Summary:** Worked as a software engineer and machine learning engineer in a health-tech startup, leading end-to-end platform development for personalized phage therapy. Designed ML models for genomic data analysis, built scalable cloud infrastructure, and collaborated with cross-functional teams including bioinformatics, engineering, and regulatory specialists.

### Platform Development and Quality Standards

**Situation**

The startup required a production-ready healthcare AI platform that met high standards for traceability, reliability, and clinical data handling while supporting rapid development and iteration.

**Action**

- Led cross-functional platform development, coordinating between backend, frontend, ML, and domain expert teams
- Worked in a regulated environment with exposure to healthcare software standards (ISO 13485, IEC 62304, ISO 14971) and quality management processes
- Implemented ML system boundaries and validation practices to ensure models operated within intended scope and data constraints
- Supervised and coordinated outsourced frontend development while maintaining platform architecture integrity
- Emphasized production readiness through systematic traceability, testing, and validation-oriented development practices

**Result**

- Delivered a robust, scalable AI platform architecture suitable for healthcare applications
- Established development practices balancing rapid iteration with quality and compliance requirements
- Improved cross-team coordination and alignment on technical and product requirements

### Backend Developer, DevOps Engineer, and Cloud Architect

**Situation**

The platform required a scalable, secure, and cost-efficient cloud infrastructure capable of handling genomic data processing, real-time API requests, and batch analysis workloads.

**Action**

- Designed and implemented AWS cloud architecture including networking, routing, ECS services, EC2, S3, RDS, and ECR
- Led backend and infrastructure development using FastAPI and SQLModel
- Built and deployed containerized services using Docker and Amazon ECS for scalable microservices
- Designed secure networking architecture including service segmentation, routing, and frontend-backend integration
- Developed batch processing pipelines using ECS tasks for large-scale genomic data analysis
- Managed cloud infrastructure migration and operations across AWS and Azure environments
- Optimized compute, storage, and networking usage to improve efficiency and system scalability
- Reduced cloud operational costs by ~25% through infrastructure optimization and resource management

**Result**

- Delivered a production-grade, scalable cloud platform supporting AI-driven healthcare workloads
- Enabled reliable batch and real-time processing of large genomic datasets
- Improved system scalability, maintainability, and cost efficiency across cloud infrastructure

### AI and ML Engineer

**Situation**

The core product required accurate, interpretable machine learning models capable of analyzing complex genomic and microbial data for personalized phage therapy recommendations.

**Action**

- Designed and developed ML models for personalized phage cocktail recommendation using bacterial and phage whole-genome sequencing (WGS) data
- Collaborated with bioinformatics and microbiology teams to translate genomic data into ML-ready features and clinical insights
- Performed feature engineering, feature selection, and data preprocessing on large-scale biological datasets
- Leveraged bioinformatics tools such as Prokka and MMseqs2 for genome annotation and feature extraction
- Applied AutoGluon to accelerate model experimentation, benchmarking, and baseline development
- Built automated model validation pipelines with performance thresholds, evaluation metrics, and systematic benchmarking strategies
- Implemented monitoring and governance practices including data drift detection, model scope definition, and input data validation
- Applied rigorous ML practices emphasizing traceability, reproducibility, and systematic model development
- Designed AI-assisted experimentation workflows that use LLMs to generate experiment configurations, execute training pipelines, analyze results, and summarize findings with minimal manual intervention
- Built modular, configuration-driven ML infrastructure that enables rapid experimentation and seamless integration with AI coding assistants
- Established AI-assisted development practices by defining reusable Cursor rules and specialized workflows for code generation, code review, production readiness, and collaborative software development
- Implemented AI agent workflows using Model Context Protocol (MCP) for automating data analysis tasks and connecting LLMs to internal systems and databases
- Built retrieval-augmented generation (RAG) systems to enhance model responses with domain-specific knowledge from company documentation and research papers
- Developed multi-agent orchestration patterns where specialized agents handle different aspects of ML pipeline management, from data validation to model evaluation reporting

**Result**

- Delivered production-ready ML models integrated into a scalable healthcare platform
- Improved robustness and reliability of predictions through structured validation and benchmarking
- Established a reproducible ML lifecycle with systematic validation and quality controls
- Accelerated experimentation and development velocity through LLM-assisted workflows while preserving traceability and auditability
- Enhanced productivity through AI agent integration while maintaining high software quality standards

### AI Agents and Intelligent Automation

**Situation**

As ML experiments grew in complexity and the team needed faster iteration cycles, manual experiment management and analysis became a bottleneck. Additionally, integrating LLMs with internal systems required robust, standardized connection patterns.

**Action**

- Developed AI agent systems using Model Context Protocol (MCP) to automate repetitive ML experiment analysis and reporting tasks
- Built multi-agent workflows where specialized agents handle different aspects of the ML pipeline: data validation agents, experiment configuration generators, and results analysis agents
- Implemented RAG systems that enhanced experiment analysis by incorporating domain knowledge from internal documentation, research papers, and historical experiment data
- Created agent orchestration patterns that coordinate between data processing, model training, and evaluation reporting while maintaining comprehensive audit trails
- Integrated MCP-based agents with existing FastAPI services and cloud infrastructure to enable seamless automation without disrupting core platform functionality

**Result**

- Reduced manual experiment analysis time by approximately 30% through automated reporting and insights generation
- Established reusable patterns for AI agent integration that other team members could adopt for their workflows
- Maintained high standards for traceability and quality control while increasing development velocity through intelligent automation

---

## AI Software Developer at Bearmind

**Summary:** Built and deployed a production-ready speech recognition system for a clinical assessment workflow, combining transformer-based ASR, LLM post-processing, and robust data pipelines on AWS.

### AI-based Speech Recognition Pipeline

**Situation**

Bearmind needed to automate a medical assessment that relied on spoken responses. Conventional word-level transcription accuracy was insufficient; the product required semantically correct outputs for counting and structured clinical tasks.

**Action**

- Designed and deployed a production-ready transformer-based Automatic Speech Recognition (ASR) pipeline to automate a medical assessment
- Customized open-source Hugging Face speech recognition models through inference-time adaptation, contextual inputs, and domain-specific post-processing for clinical use cases
- Integrated LLM-based post-processing to normalize and refine transcription outputs for downstream medical analysis and task-specific formatting
- Developed a high-precision data quality filter, achieving 86% accuracy in identifying unusable recordings prior to inference
- Designed task-specific evaluation metrics and validation pipelines focused on semantic correctness for counting tasks rather than conventional word-level transcription accuracy
- Evaluated model adaptation strategies, including transfer learning and fine-tuning approaches for domain-specific speech recognition tasks
- Deployed production-ready speech recognition models on AWS, enabling scalable real-time inference
- Delivered comprehensive unit test coverage for ML components, increasing reliability, maintainability, and deployment confidence

**Result**

- Delivered a clinically usable ASR system that prioritized task correctness over raw transcription metrics
- Reduced wasted inference on low-quality recordings through upstream data filtering
- Established a production deployment pattern for speech ML on AWS with tested, maintainable components

### Data lifecycle pipeline

**Situation**

The speech recognition system needed reliable, automated ingestion and orchestration across multiple heterogeneous data sources for both inference and evaluation.

**Action**

- Orchestrated automated ML data pipelines with Dagster, integrating data from three heterogeneous sources for model inference and evaluation
- Built pipelines that supported both production inference and systematic model evaluation
- Ensured ML components were covered by unit tests to support safe iteration and deployment

**Result**

- Enabled reproducible, automated data flows from ingestion through inference and evaluation
- Improved reliability and confidence in production ML operations through tested pipeline components

---

## ML Engineer / Data Scientist at EPFL

**Summary:** Developed ML and image-processing tools for yeast microscopy analysis, including a published GNN-based cell-tracking method.

### Yeast Microscopic Movie Analysis

**Situation**

Laboratory yeast microscopy workflows required manual analysis of long time-lapse movies, which was slow and limited throughput for research teams.

**Action**

- Created a Python package leveraging machine learning and image processing to automate analysis of yeast microscopic movies
- Reduced analysis time by 50% compared with previous manual workflows
- Led the full development lifecycle of an ML pipeline, including labeling, model training, and deployment

**Result**

- Delivered a reusable software package that significantly accelerated microscopy analysis for researchers
- Demonstrated ability to translate research needs into maintainable ML tooling

### ML Pipeline for Cell Tracking

**Situation**

Accurate cell tracking across frames was critical for lineage tracing and quantitative biology experiments involving hundreds of cells per movie.

**Action**

- Implemented a Graph Neural Network (GNN) model, achieving a 99% F1-score in cell tracking
- Developed an object tracking system for 400+ cells, achieving 90% accuracy via feature optimization
- Contributed to research that led to a peer-reviewed publication on neural networks for tracking and lineage tracing in budding yeast (*Bioinformatics Advances*, 2026)

**Result**

- Achieved state-of-the-art tracking performance on challenging microscopy data
- Produced publishable research combining graph ML, computer vision, and biological imaging

---

## Master thesis: Computational drug response prediction

**Situation**

Personalized cancer treatment requires predicting how combinations of drugs affect individual cell lines, integrating heterogeneous molecular and drug data at scale.

**Action**

- Conducted pioneering deep-learning research on drug combinations' effect on cancer cell lines
- Combined multi-omics data and molecular drug data to develop personalized drug combination predictions
- Performed data quality checks and visualization to ensure high-quality, reliable datasets
- Used cluster computing for efficient ML model training and data-intensive tasks
- Engineered a novel data cleaning algorithm for embedded gene expression profiles, resolving 10+ data anomalies and increasing precision by 4%

**Result**

- Built a rigorous computational pipeline for multi-omics drug response modeling
- Improved data quality and model reliability through targeted preprocessing innovations

---

## Gene expression data analysis

**Situation**

Thyroid cancer research required large-scale gene expression analysis linked to pathway and drug-target discovery.

**Action**

- Obtained and preprocessed gene expression data from the NCBI database for over 10,000 thyroid cancer cells and related information, with quality control
- Performed statistical analysis, data processing, and quality improvement using R and Python
- Identified potential drugs and critical cellular pathways using gene co-expression and protein interaction networks, with visualization in Cytoscape

**Result**

- Delivered interpretable network-based insights from large-scale omics data
- Strengthened foundation in genomics, statistics, and biological data integration

---

## Software Developer at Hamravesh

**Summary:** Early-career software engineering and DevOps experience building mobile applications and CI/CD infrastructure in an Agile startup environment.

### Mobile software development and DevOps

**Situation**

Hamravesh needed reliable mobile delivery across multiple Agile projects with consistent quality and deployment practices.

**Action**

- Worked as a DevOps Engineer and front-end software developer, supporting development and deployment of scalable mobile applications
- Developed and maintained React Native mobile apps across 5 Agile projects
- Designed and implemented robust CI/CD pipelines with automated testing, code quality checks, and Docker-based builds, reducing production bugs by 80%
- Deployed and managed containerized services using Docker and Kubernetes

**Result**

- Delivered stable mobile products with significantly fewer production defects
- Built foundational experience in CI/CD, containerization, and cross-functional Agile delivery that supports my later MLOps work

---

## Transferable skills and themes for cover letters

Use these as hooks when tailoring letters to specific roles:

- **Healthcare software standards:** Quality management systems, validation-oriented development, traceability, systematic testing practices
- **Genomics and bioinformatics:** WGS, NGS, multi-omics integration, Prokka/MMseqs2, phage therapy, clinical data handling
- **Production ML engineering:** FastAPI, Dagster, AWS/Azure, Docker, ECS, model validation, monitoring, drift detection
- **LLM and modern AI:** Hugging Face, RAG, prompt engineering, LLM post-processing, AI agents, MCP, AI-assisted software development, multi-agent orchestration, intelligent automation systems
- **Speech and multimodal ML:** Transformer ASR, domain adaptation, semantic evaluation beyond word error rate
- **Research-to-product:** EPFL microscopy ML, published GNN work, master's thesis in computational drug response
- **Ownership in startups:** End-to-end platform leadership, outsourced team coordination, cost optimization, business impact
